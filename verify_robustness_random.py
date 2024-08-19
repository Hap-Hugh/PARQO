import psycopg2
import json
from postgres import *
from utility import modify_query, get_count


random_seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_count(cursor_, table_name):
    query_ = f"select count(*) from {table_name};"
    cursor_.execute(query_)
    result = cursor_.fetchall()
    return result[0][0]


def verify_by_multiple_random_instances(i, window_size):
    db_name = "imdbloadbase"
    conn = psycopg2.connect("host=/tmp dbname=" + db_name)
    conn.set_session(autocommit=True)
    cursor_ = conn.cursor()
    cache = {}


    # Define the number of samples and the sampling range
    raw_size_title = 2528312
    new_tables = []

    # Loop over the samples and generate the sampled tables for all the required tables
    tables_to_sample_by_title = ["movie_companies", "movie_keyword", "cast_info", "movie_link", "movie_info",
                                 "complete_cast", "aka_title", "movie_info_idx"]


    try:


        # Construct the SQL query to generate the random_title table for the current sample
        query = f"""
            CREATE TABLE random_title_{i} AS 
            SELECT * FROM title 
            TABLESAMPLE BERNOULLI({window_size}) 
            REPEATABLE({random_seeds[i]}) 
            ORDER BY production_year;
        """
        
        # Execute the query
        new_tables.append(f"random_title_{i}")
        cursor_.execute(query)
        print(f"Generated random_title_{i} with random seed {random_seeds[i]}, window_size = {window_size}")
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        # Generate sampled tables based on title
        for table_name in tables_to_sample_by_title:
            query_ = f"""
                CREATE TABLE random_{table_name}_{i} AS
                SELECT *
                FROM {table_name}
                WHERE {table_name}.movie_id IN (
                    SELECT id
                    FROM random_title_{i}
                );
            """
            new_tables.append(f"random_{table_name}_{i}")
            cursor_.execute(query_)
            print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
            cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        # Generate sampled keyword based on movie_keyword
        query_ = f"""
            CREATE TABLE random_keyword_{i} AS
            SELECT *
            FROM keyword
            WHERE keyword.id IN (
                SELECT keyword_id
                FROM random_movie_keyword_{i}
            );
        """
        new_tables.append(f"random_keyword_{i}")
        cursor_.execute(query_)
        
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])




        # Generate sampled company_name based on movie_companies
        query_ = f"""
            CREATE TABLE random_company_name_{i} AS
            SELECT *
            FROM company_name
            WHERE company_name.id IN (
                SELECT company_id
                FROM random_movie_companies_{i}
            );
        """
        new_tables.append(f"random_company_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate sampled aka_name based on cast_info
        query_ = f"""
            CREATE TABLE random_aka_name_{i} AS
            SELECT *
            FROM aka_name
            WHERE aka_name.id IN (
                SELECT person_id
                FROM random_cast_info_{i}
            );
        """
        new_tables.append(f"random_aka_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])



        # Generate sampled name based on aka_name
        query_ = f"""
            CREATE TABLE random_name_{i} AS
            SELECT *
            FROM name
            WHERE name.id IN (
                SELECT id
                FROM random_aka_name_{i}
            );
        """
        new_tables.append(f"random_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])



        # Generate sampled person_info based on name
        query_ = f"""
            CREATE TABLE random_person_info_{i} AS
            SELECT *
            FROM person_info
            WHERE person_info.person_id IN (
                SELECT id
                FROM random_name_{i}
            );
        """
        new_tables.append(f"random_person_info_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])




        # Generate sampled link_type based on movie_link
        query_ = f"""
            CREATE TABLE random_link_type_{i} AS
            SELECT *
            FROM link_type
            WHERE link_type.id IN (
                SELECT link_type_id
                FROM random_movie_link_{i}
            );
        """
        new_tables.append(f"random_link_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])




        # Generate sampled info_type based on person_info and movie_info
        query_ = f"""
            CREATE TABLE random_info_type_{i} AS
            SELECT *
            FROM info_type
            WHERE info_type.id IN (
                SELECT info_type_id
                FROM random_movie_info_{i}
            ) OR info_type.id IN (
                SELECT info_type_id
                FROM random_person_info_{i}
            ) OR info_type.id IN (
                SELECT info_type_id
                FROM random_movie_info_idx_{i}
            );
        """
        new_tables.append(f"random_info_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        
        # Generate company_type
        query_ = f"""
            CREATE TABLE random_company_type_{i} AS
            SELECT *
            FROM company_type
            WHERE company_type.id IN (
                SELECT company_type_id
                FROM random_movie_companies_{i}
            );
        """
        new_tables.append(f"random_company_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate random_kind_type
        query_ = f"""
            CREATE TABLE random_kind_type_{i} AS
            SELECT *
            FROM kind_type
            WHERE kind_type.id IN (
                SELECT kind_id
                FROM random_title_{i}
            );
        """
        new_tables.append(f"random_kind_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate char_name
        query_ = f"""
            CREATE TABLE random_char_name_{i} AS
            SELECT *
            FROM char_name
            WHERE char_name.id IN (
                SELECT person_role_id
                FROM random_cast_info_{i}
            );
        """
        new_tables.append(f"random_char_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate role_type
        query_ = f"""
            CREATE TABLE random_role_type_{i} AS
            SELECT *
            FROM role_type
            WHERE role_type.id IN (
                SELECT role_id
                FROM random_cast_info_{i}
            );
        """
        new_tables.append(f"random_role_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate comp_cast_type
        query_ = f"""
            CREATE TABLE random_comp_cast_type_{i} AS
            SELECT *
            FROM comp_cast_type
            WHERE comp_cast_type.id IN (
                SELECT status_id
                FROM random_complete_cast_{i}
            ) OR comp_cast_type.id IN (
                SELECT subject_id
                FROM random_complete_cast_{i}
            );
        """
        new_tables.append(f"random_comp_cast_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # create primary key
        for t in new_tables:
            query_ = f"ALTER TABLE {t} ADD PRIMARY KEY (id);"
            cursor_.execute(query_)


        # create index for fk
        index_query = f'''create index company_id_movie_companies on movie_companies(company_id);
                        create index company_type_id_movie_companies on movie_companies(company_type_id);
                        create index info_type_id_movie_info_idx on movie_info_idx(info_type_id);
                        create index info_type_id_movie_info on movie_info(info_type_id);
                        create index info_type_id_person_info on person_info(info_type_id);
                        create index keyword_id_movie_keyword on movie_keyword(keyword_id);
                        create index kind_id_aka_title on aka_title(kind_id);
                        create index kind_id_title on title(kind_id);
                        create index linked_movie_id_movie_link on movie_link(linked_movie_id);
                        create index link_type_id_movie_link on movie_link(link_type_id);
                        create index movie_id_aka_title on aka_title(movie_id);
                        create index movie_id_cast_info on cast_info(movie_id);
                        create index movie_id_complete_cast on complete_cast(movie_id);
                        create index subject_id_complete_cast on complete_cast(subject_id);
                        create index status_id_complete_cast on complete_cast(status_id);
                        create index movie_id_movie_companies on movie_companies(movie_id);
                        create index movie_id_movie_info_idx on movie_info_idx(movie_id);
                        create index movie_id_movie_keyword on movie_keyword(movie_id);
                        create index movie_id_movie_link on movie_link(movie_id);
                        create index movie_id_movie_info on movie_info(movie_id);
                        create index person_id_aka_name on aka_name(person_id);
                        create index person_id_cast_info on cast_info(person_id);
                        create index person_id_person_info on person_info(person_id);
                        create index person_role_id_cast_info on cast_info(person_role_id);
                        create index role_id_cast_info on cast_info(role_id);'''

        index_query = index_query.replace('(', f'_{i}(')
        index_query = index_query.replace(' on ', f'_random_{i} on random_')
        cursor_.execute(index_query)
        print(index_query)

        # add fk
        fk_query = '''
                ALTER TABLE title ADD FOREIGN KEY (kind_id) REFERENCES kind_type;
                ALTER TABLE aka_name ADD FOREIGN KEY (id) REFERENCES name;
                -- psql:add_fks.sql:3: ERROR:  insert or update on table "cast_info" violates foreign key constraint "cast_info_person_id_fkey"
                --   DETAIL:  Key (person_id)=(901344) is not present in table "aka_name".
                -- ALTER TABLE cast_info ADD FOREIGN KEY (person_id) REFERENCES aka_name;
                ALTER TABLE cast_info ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE cast_info ADD FOREIGN KEY (person_role_id) REFERENCES char_name;
                ALTER TABLE cast_info ADD FOREIGN KEY (role_id) REFERENCES role_type;
                ALTER TABLE complete_cast ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE complete_cast ADD FOREIGN KEY (subject_id) REFERENCES comp_cast_type;
                ALTER TABLE complete_cast ADD FOREIGN KEY (status_id) REFERENCES comp_cast_type;
                ALTER TABLE movie_companies ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE movie_info ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE movie_info ADD FOREIGN KEY (info_type_id) REFERENCES info_type;
                ALTER TABLE movie_info_idx ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE movie_info_idx ADD FOREIGN KEY (info_type_id) REFERENCES info_type;
                ALTER TABLE movie_keyword ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE movie_keyword ADD FOREIGN KEY (keyword_id) REFERENCES keyword;
                ALTER TABLE movie_link ADD FOREIGN KEY (movie_id) REFERENCES title;
                ALTER TABLE movie_link ADD FOREIGN KEY (link_type_id) REFERENCES link_type;
                ALTER TABLE person_info ADD FOREIGN KEY (person_id) REFERENCES name;
                ALTER TABLE person_info ADD FOREIGN KEY (info_type_id) REFERENCES info_type;
            '''
        # TODO check if alter successfully
        fk_query = fk_query.replace(' ADD ', f'_{i} ADD ')
        fk_query = fk_query.replace(';', f'_{i};')
        fk_query = fk_query.replace('TABLE ', f'TABLE random_')
        fk_query = fk_query.replace('REFERENCES ', f'REFERENCES random_')
        cursor_.execute(fk_query)
        print(fk_query)


        # create histgram
        cursor_.execute("ANALYZE VERBOSE;")
        print("Done ANALYZE VERBOSE;")
    except Exception as e:
        print(e)
        drop_table(new_tables)

    if i != "base":
        conn.close()
        return new_tables
    print(cache)
        

    # Close the database connection
    conn.close()
    return cache


def drop_table(new_tables):
    db_name = "imdbloadbase"
    conn = psycopg2.connect("host=/tmp dbname=" + db_name)
    conn.set_session(autocommit=True)
    cursor_ = conn.cursor()
    for t in new_tables:
        try:
            cursor_.execute(f"drop table {t} CASCADE;")
            print(f"drop table {t} CASCADE;")
        except:
            continue
    return



''' backup
drop table random_title_0 CASCADE;
drop table random_movie_companies_0 CASCADE;
drop table random_movie_keyword_0 CASCADE;
drop table random_cast_info_0 CASCADE;
drop table random_movie_link_0 CASCADE;
drop table random_movie_info_0 CASCADE;
drop table random_complete_cast_0 CASCADE;
drop table random_aka_title_0 CASCADE;
drop table random_movie_info_idx_0 CASCADE;
drop table random_keyword_0 CASCADE;
drop table random_company_name_0 CASCADE;
drop table random_aka_name_0 CASCADE;
drop table random_name_0 CASCADE;
drop table random_person_info_0 CASCADE;
drop table random_link_type_0 CASCADE;
drop table random_info_type_0 CASCADE;
drop table random_company_type_0 CASCADE;
drop table random_kind_type_0 CASCADE;
drop table random_char_name_0 CASCADE;
drop table random_role_type_0 CASCADE;
drop table random_comp_cast_type_0 CASCADE;
'''



'''
SELECT column_name
FROM information_schema.constraint_column_usage
WHERE table_name = 'random_keyword_0'
AND constraint_name = (
    SELECT constraint_name
    FROM information_schema.table_constraints
    WHERE table_name = 'random_keyword_0'
    AND constraint_type = 'PRIMARY KEY'
);
'''



result_for_print = []
on_sample = "on-random/"

for s in range(0, 4):
    # verify_by_multiple_random_instances(i, 20)
    for query_id in ["17a"]:
    # for query_id in ["1a", "2a","3a","4a","5a","6a","7a", "14a", "15a", "16a", "17a", "18a", "25a"]:
        os.system("rm -rf ~/imdb/recordx.log")
        print(query_id)
        db_name = "imdbloadbase"
        explain = "EXPLAIN (SUMMARY, COSTS, FORMAT JSON)"
        with open('./query/join-order-benchmark/' + query_id + '.sql') as p:
            sql = p.read()
        
        tmp_plan_dict_file = './plan/' + on_sample + 'tmp_plan_dict_' + db_name + '_' + query_id + '.txt'
        plan_hint_dict = json.load(open(tmp_plan_dict_file))
        cur_plan_list = []
        for i in plan_hint_dict.values():
            cur_plan_list = cur_plan_list + i
        cur_plan_list = list(sorted(set(cur_plan_list)))
        # print(cur_plan_list)
        print(f"Total plan set has: {len(cur_plan_list)} plans.")
        new_sql = modify_query("random_", f"_{s}", sql)
        print(new_sql)
        robust_plans = {"1a": [15, 22], "2a":[0, 7], "3a": [3, 4, 0], "4a": [15, 0, 22, 16], "5a": [9, 21, 19, 22, 25], "6a": [0, 3], "7a":[4, 13, 15],
            "13a": [14], "14a": [0, 16, 13, 10],
            "15a": [22, 0, 35, 27], "16a": [10, 12, 13, 14],  "17a":[15, 19], "18a":[21, 18, 0], 
            "20a": [31, 59, 55], "25a": [33, 22, 37, 1, 30]}
        ori_plan = {"6a": [0], "5a": [1], "4a": [0], "3a": [1], "2a":[1], "7a":[0], "17a":[5],  "14a": [0], "15a": [3],
                    "19a": [2], "18a":[1], "1a": [2], "16a": [0], "25a": [0]}

        # ori_latency = get_real_latency(db_name, new_sql, hint=cur_plan_list[ori_plan[query_id][0]], times=31)
        f = open("log/"+ on_sample + "verify_" + query_id + ".txt", 'a+')
        # print(f"{s}: latency of original plan:\n {ori_latency}", file=f)
        
        new_pg_latency = get_real_latency(db_name, new_sql, times=31)
        print(f"{s}: latency of new optimal plan:\n {new_pg_latency}", file=f)
        our_latency = []
        
        for i in robust_plans[query_id]:
        # for i in range(len(cur_plan_list)):
            our_latency.append(get_real_latency(db_name, new_sql, hint=cur_plan_list[i], times=31))
        print(f"{s}: latency of robust plan:\n {our_latency}", file=f)
        get_real_latency(db_name, new_sql, hint=cur_plan_list[i], times=1, query_id=query_id, output_plan=True)

        # result = [ori_latency] +  + our_latency
        result = [new_pg_latency] + our_latency
        print(f"{s} result:\n {result}", file=f)
        result_for_print.append(result)
        f.close()
    # drop_table(new_tables)
for i in result_for_print:
    print(i, file=open("log/"+ on_sample + "verify_" + query_id + ".txt", 'a+'))