import subprocess
import psycopg2
import os
from psql_explain_decoder import *
import numpy as np


def DropBufferCache(cursor_):
    # WARNING: no effect if PG is running on another machine
    subprocess.check_output(['free', '&&', 'sync'])
    subprocess.check_output(
        ['sudo', 'sh', '-c', 'echo 3 > /proc/sys/vm/drop_caches'])
    subprocess.check_output(['free'])

    cursor_.execute('DISCARD ALL;')


def get_real_latency(db_name, sql, hint=None, times=5, inject=False, output_plan=False, query_id=None, return_json=False, limit_time=10000, limit_worker=False, drop_buffer=True):
    # TODO inject or not is meaning less
    conn = psycopg2.connect(host="/tmp", dbname=db_name, user="hx68")
    conn.set_session(autocommit=True)
    cursor_ = conn.cursor()
    os.system("cp ~/robust-vcm/cardinality/new_single.txt ~/imdb/")

    explain = "EXPLAIN (ANALYZE, SUMMARY, COSTS, FORMAT JSON)"
    latency_list = []
    rows_list = []
    
    for i in range(times):
        if drop_buffer: DropBufferCache(cursor_)
        if inject:
            cursor_.execute("SET ml_cardest_enabled=true;")
            cursor_.execute("SET query_no=0;")
            cursor_.execute("SET ml_cardest_fname='new_single.txt';")
        cursor_.execute("LOAD 'pg_hint_plan';")
        cursor_.execute('SET enable_material = off;')
        # cursor_.execute('SET top_n = 0;')
        if limit_time:
            cursor_.execute(f'SET statement_timeout = {limit_time};')
        if limit_worker:
            cursor_.execute('SET max_parallel_workers_per_gather = 0;')

            
        
        if hint:
            hint = hint
        else:
            hint = ""
        to_execute_ = explain + '\n' + hint + sql

        try:
            cursor_.execute(to_execute_)
            query_plan = cursor_.fetchall()
            if return_json:
                return query_plan
        except psycopg2.errors.QueryCanceled as e:
            # return float('inf')
            return 0.0
            pass

        cursor_.execute("SET query_no=0;")
        cur_latency = query_plan[0][0][0]['Plan']['Actual Total Time']
        latency_list.append(cur_latency)
        if cur_latency > 600000:
            return cur_latency
    
    if output_plan:
        join_order, _, scan_mtd = decode(query_plan[0][0][0]['Plan']['Plans'], query_plan[0][0][0]['Plan']['Node Type'])
        print(join_order)
        # json_object = json.dumps(query_plan, indent=4)
        # with open(f"log/explain/{query_id}_explain.json", "a") as outfile:
        #     outfile.write(json_object)
    conn.close()
    return np.median(np.array(latency_list))



def get_plan_cost_simple(cursor, sql, hint=None, debug=None, explain=None):
    cursor.execute('DISCARD ALL;')
    cursor.execute('SET enable_material = off')
    # cursor.execute('SET top_n = 0')
    cursor.execute("SET ml_cardest_enabled=false;")
    cursor.execute("LOAD 'pg_hint_plan';")
    cursor.execute("SET ml_joinest_enabled=false;")


    try:
        if hint:
            to_execute_ = explain + '\n' + hint + sql
        else:
            to_execute_ = explain + '\n' + sql
        cursor.execute(to_execute_)
        query_plan = cursor.fetchall()
        cost = query_plan[0][0][0]['Plan']['Total Cost']
        join_order, _, scan_mtd = decode(query_plan[0][0][0]['Plan']['Plans'], query_plan[0][0][0]['Plan']['Node Type'])

    except psycopg2.OperationalError as e:            
        print(to_execute_)
    except psycopg2.errors.SyntaxError as e:            
        print(to_execute_)
    if debug:
        return cost, join_order, scan_mtd
    return cost



def get_plan_cost(cursor, sql, hint=None, debug=None, explain=None):
    os.system("cp ~/robust-vcm/cardinality/join.txt ~/imdb/")
    os.system("cp ~/robust-vcm/cardinality/new_single.txt ~/imdb/")
    os.system("cp ~/robust-vcm/cardinality/pointers.txt ~/imdb")
    cursor.execute('DISCARD ALL;')
    cursor.execute('SET enable_material = off')
    # cursor.execute('SET top_n = 0')
    cursor.execute("SET ml_cardest_enabled=true;")
    cursor.execute("SET query_no=0;")
    cursor.execute("SET ml_cardest_fname='new_single.txt';")
    cursor.execute("LOAD 'pg_hint_plan';")

    cursor.execute("SET ml_joinest_enabled=true;")
    cursor.execute("SET join_est_no=0;")
    cursor.execute("SET ml_joinest_fname='join.txt';")
    
    os.system("rm ~/imdb/join_est_record_job.txt")
    os.system("rm ~/imdb/single_tbl_est_record.txt")
    cursor.execute("SET print_single_tbl_queries=true;")
    cursor.execute("SET print_sub_queries=true;")

    try:
        if hint:
            to_execute_ = explain + '\n' + hint + sql
        else:
            to_execute_ = explain + '\n' + sql
        cursor.execute(to_execute_)
        query_plan = cursor.fetchall()
        cost = query_plan[0][0][0]['Plan']['Total Cost']
        join_order, _, scan_mtd = decode(query_plan[0][0][0]['Plan']['Plans'], query_plan[0][0][0]['Plan']['Node Type'])

    except psycopg2.OperationalError as e:            
        print(to_execute_)
    except psycopg2.errors.SyntaxError as e:            
        print(to_execute_)
    if debug:
        return cost, join_order, scan_mtd
    return cost


def get_all_predicates(cursor, sql, explain):
    cursor.execute('DISCARD ALL;')
    cursor.execute('SET enable_material = off')
    # cursor.execute('SET top_n = 0')
    cursor.execute("SET query_no=0;")
    cursor.execute("SET join_est_no=0;")
    cursor.execute("SET print_single_tbl_queries=true;")
    cursor.execute("SET print_sub_queries=true;")

    try:
        to_execute_ = explain + '\n' + sql
        cursor.execute(to_execute_)
    except psycopg2.OperationalError as e:            
        print(to_execute_)
    except psycopg2.errors.SyntaxError as e:            
        print(to_execute_)
        

def get_all_plan_cost(cursor, sql, explain, cur_plan_list, debug=False):
    ### At current card, which plan is the best
    opt_cost_list = []    
    for hint_id in range(len(cur_plan_list)):
        hint = cur_plan_list[hint_id]
        cost_with_hint, join_order_with_hint, scan_mtd_with_hint = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain, debug=True)
        if debug:
            print(hint_id, ": ", cost_with_hint, join_order_with_hint, scan_mtd_with_hint)
        opt_cost_list.append(cost_with_hint)
    return opt_cost_list