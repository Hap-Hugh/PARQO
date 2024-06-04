## Postgres Configuration
https://github.com/Hap-Hugh/PG16


## Full Paper Link
https://github.com/Hap-Hugh/PARQO/blob/main/PARQO-Full-Paper.pdf

[Jun 3 Updated]Arxiv is available now: https://arxiv.org/abs/2406.01526


## Instructions to run PARQO
1. Download PostgreSQL 16.2 and modify it following the link above.
2. Install PostgreSQL
3. Install pg_hint_plan (newest version that working with PG 16.2)
4. Use pg_ctl to initdb and modify the postgresql.conf file
- Our conf file is present in https://github.com/Hap-Hugh/PG16

5. Make database (JOB, DSB and STATS)
- JOB: please follow Balsa <https://github.com/balsa-project/balsa> to download and load data to your database
- DSB: please follow https://github.com/Hap-Hugh/dsb-linux-pg/tree/main/scripts to generate data and workload
- STATS: please follow https://github.com/Nathaniel-Han/End-to-End-CardEst-Benchmark to download data and load data to your database

6. Run PARQO's code:
- install numpy, psycopg2, matplotlib, scikit-learn, SALib, tqdm
- RQO: python robustness.py --query_id=17a
- PQO: python robustness.py --query_id=17a --pqo
- Others:
    - Sobols: python robustness.py --query_id=17a --cal_sen=sobols
    - Morris: python robustness.py --query_id=17a --cal_sen=morris
