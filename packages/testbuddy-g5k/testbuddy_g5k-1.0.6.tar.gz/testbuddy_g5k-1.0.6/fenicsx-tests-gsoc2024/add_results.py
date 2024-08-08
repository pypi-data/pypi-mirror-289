#!/usr/bin/env python3

# This script creates some fake data

import sqlite3
import sys
import datetime
import random

def main():
    database = sys.argv[1]
    con = sqlite3.connect(database)
    cur = con.cursor()
    columns = '"date","grid5000.site","grid5000.cluster",' \
    '"experiment.cores","experiment.libblas","experiment.libblas_version","experiment.mpi","experiment.mpi_version",' \
    '"experiment.problem_type","experiment.scaling_type","software.packages.fenicsx-performance-tests","timings.zzz_solve.wall_tot"'
    cur.execute(f"SELECT {columns} FROM results ORDER BY date ASC")
    res = cur.fetchone()
    cur2 = con.cursor()
    while res:
        if not res[11]:
            res = cur.fetchone()
            continue
        t = datetime.timedelta(days=0)
        record = list(res)
        for i in range(1,209):
            t += datetime.timedelta(days=7)
            if i > 100 and i < 105:
                f = random.uniform(1.7, 2.3)
            else:
                f = random.uniform(1, 1.05)
            d = datetime.datetime.fromisoformat(res[0]) + t
            record[0] = d.isoformat()
            record[11] = f"{f * float(res[11]):.9f}"
            cur2.execute(
                f"INSERT INTO results({columns}) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                record,
            )
        res = cur.fetchone()
    con.commit()

if __name__ == "__main__":
    main()
