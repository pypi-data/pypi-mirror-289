#!/usr/bin/env python3

import tomllib
import click
import pandas
import sqlite3
import jinja2
import pathlib
import shutil
import os
import plotly.express as px

PLOTLY_JS = pathlib.Path("./plotly-2.32.0.min.js")
INPUT_TEMPLATE = pathlib.Path("./graph.html.jinja")


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "-d",
    "--database",
    help="The database to load the results from",
    metavar="DATABASE",
    required=False,
    default=None,
    type=click.Path(dir_okay=False, exists=True),
)
@click.option(
    "-c",
    "--configuration",
    help="Use the output directory and database path from the testbuddy-g5k configuration",
    metavar="CONFIGURATION",
    default=None,
    type=click.File("rb"),
)
@click.argument("output_dir", nargs=1, required=False, default=None)
def main(database, configuration, output_dir):
    """Create HTML plots of the results of DATABASE."""
    if configuration:
        conf = tomllib.load(configuration)
        if not output_dir:
            output_dir = conf["extra"]["plot_dir"]
        if not database:
            database = conf["extra"]["database"]
    if not output_dir:
        raise click.ClickException("Must specify OUTPUT_DIR.")
    if not database:
        raise click.ClickException("Must specify DATABASE.")

    con = sqlite3.connect(database)
    tmp = pandas.read_sql(
        'SELECT "date","grid5000.site","grid5000.cluster",'
        '"experiment.cores","experiment.libblas","experiment.libblas_version","experiment.mpi","experiment.mpi_version",'
        '"experiment.problem_type","experiment.scaling_type","software.packages.fenicsx-performance-tests","timings.zzz_solve.wall_tot" '
        "FROM results",
        con,
    )
    con.close()
    df = tmp.rename(
        columns=dict(zip(tmp.columns, [x.split(".", 1)[-1] for x in tmp.columns]))
    )
    df["date"] = pandas.to_datetime(df["date"], format="ISO8601")
    for column in ["cores", "zzz_solve.wall_tot"]:
        df[column] = pandas.to_numeric(df[column])
    for problem_type in ["poisson", "elasticity"]:
        for scaling_type in ["weak", "strong"]:
            # The DataFrame for the speedup plot.
            tmp = df[
                (df["problem_type"] == problem_type)
                & (df["scaling_type"] == scaling_type)
            ]
            tmp = tmp.sort_values(by="cores")
            tmp["date"] = tmp["date"].transform(lambda d: d.strftime("%Y-%m-%d"))
            t1 = tmp["zzz_solve.wall_tot"].iloc[0]
            if scaling_type == "weak":
                tmpcol = tmp["zzz_solve.wall_tot"] / tmp["cores"]
                tmp["speedup"] = tmpcol.transform(lambda t: t1 / t)
            elif scaling_type == "strong":
                tmp["speedup"] = tmp["zzz_solve.wall_tot"].transform(lambda t: t1 / t)
            else:
                raise ValueError("Unimplemented scaling_type value.")
            tmp["cluster.site"] = tmp.apply(
                lambda row: f'{row["cluster"]}.{row["site"]}', axis="columns"
            )
            speedup_range = [
                tmp["speedup"].min() * 0.9 - 1,
                tmp["speedup"].max() * 1.1 + 1,
            ]
            runtime_range = [
                tmp["zzz_solve.wall_tot"].min() * 0.9 - 1,
                tmp["zzz_solve.wall_tot"].max() * 1.1 + 1,
            ]
            # Hover-over data
            tmp["BLAS"] = tmp["libblas"] + ":" + tmp["libblas_version"]
            tmp["MPI"] = tmp["mpi"] + ":" + tmp["mpi_version"]
            tmp["fenicsx-performance-tests"] = tmp["packages.fenicsx-performance-tests"]
            fig_sd = px.scatter(
                tmp,
                x="date",
                y="speedup",
                color="cluster.site",
                animation_frame="cores",
                title="speedup over time",
                range_y=speedup_range,
                labels={"speedup": "speedup %"},
                hover_data=[
                    "BLAS",
                    "MPI",
                    "fenicsx-performance-tests",
                ],
            )
            fig_sd.update_layout(yaxis_tickformat=".2%")
            fig_sd.update_xaxes(
                rangeslider_visible=True,
                tickformatstops=[
                    dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
                    dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
                    dict(dtickrange=[60000, 3600000], value="%H:%M m"),
                    dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
                    dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
                    dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
                    dict(dtickrange=["M1", "M12"], value="%b '%y M"),
                    dict(dtickrange=["M12", None], value="%Y Y"),
                ],
            )
            fig_rd = px.scatter(
                tmp,
                x="date",
                y="zzz_solve.wall_tot",
                color="cluster.site",
                animation_frame="cores",
                title="runtime over time",
                range_y=runtime_range,
                labels={"zzz_solve.wall_tot": "runtime (s)"},
                hover_data=[
                    "BLAS",
                    "MPI",
                    "fenicsx-performance-tests",
                ],
            )
            fig_rd.update_xaxes(
                rangeslider_visible=True,
                tickformatstops=[
                    dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
                    dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
                    dict(dtickrange=[60000, 3600000], value="%H:%M m"),
                    dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
                    dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
                    dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
                    dict(dtickrange=["M1", "M12"], value="%b '%y M"),
                    dict(dtickrange=["M12", None], value="%Y Y"),
                ],
            )
            tmp = tmp.sort_values(by="date")
            fig_sc = px.scatter(
                tmp,
                x="cores",
                y="speedup",
                color="cluster.site",
                animation_frame="date",
                range_y=speedup_range,
                labels={"speedup": "speedup  %"},
                title="speedup over cores",
                hover_data=[
                    "BLAS",
                    "MPI",
                    "fenicsx-performance-tests",
                ],
            )
            fig_sc.update_layout(yaxis_tickformat=".2%")
            fig_rc = px.scatter(
                tmp,
                x="cores",
                y="zzz_solve.wall_tot",
                color="cluster.site",
                animation_frame="date",
                title="runtime over cores",
                range_y=runtime_range,
                labels={"zzz_solve.wall_tot": "runtime (s)"},
                hover_data=[
                    "BLAS",
                    "MPI",
                    "fenicsx-performance-tests",
                ],
            )
            # The Jinja2 template.
            template = {
                "fig_speedup_cores": fig_sc.to_html(
                    full_html=False, include_plotlyjs=False, auto_play=False
                ),
                "fig_speedup_date": fig_sd.to_html(
                    full_html=False, include_plotlyjs=False, auto_play=False
                ),
                "fig_runtime_cores": fig_rc.to_html(
                    full_html=False, include_plotlyjs=False, auto_play=False
                ),
                "fig_runtime_date": fig_rd.to_html(
                    full_html=False, include_plotlyjs=False, auto_play=False
                ),
                "g5k_attribute": "Experiments presented in this page were "
                "carried out using the Grid'5000 testbed, supported by a "
                "scientific interest group hosted by Inria and including "
                "CNRS, RENATER and several Universities as well as other "
                "organizations (see <a "
                'href="https://www.grid5000.fr">https://www.grid5000.fr</a>).',
                "title": f"Grid'5000 FEniCS experiments, {scaling_type} {problem_type}",
                "plotly_js": PLOTLY_JS,
            }
            os.makedirs(output_dir, exist_ok=True)
            # Generate and write out to HTML file.
            shutil.copy(PLOTLY_JS, output_dir)
            with open(
                pathlib.Path(output_dir) / f"{scaling_type}_{problem_type}.html",
                "w",
                encoding="utf-8",
            ) as f:
                with open(INPUT_TEMPLATE) as template_file:
                    jinja_template = jinja2.Template(template_file.read())
                    f.write(jinja_template.render(template))


if __name__ == "__main__":
    main()
