import psycopg2
import json
from postgres import *
from utility import modify_query, get_count


def verify_by_movie_category(i):
    db_name = "imdbloadbase"
    conn = psycopg2.connect("host=/tmp dbname=" + db_name)
    conn.set_session(autocommit=True)
    cursor_ = conn.cursor()
    cache = {}


    new_tables = []

    # Loop over the samples and generate the cat tables for all the required tables
    tables_to_sample_by_title = ["movie_companies", "movie_keyword", "cast_info", "movie_link", "movie_info",
                                 "complete_cast", "aka_title", "movie_info_idx"]

    try:
        query = f"""
            CREATE TABLE cat_title_{i} AS
            SELECT *
            FROM title
            WHERE kind_id = {i};
        """

        # Execute the query
        new_tables.append(f"cat_title_{i}")
        cursor_.execute(query)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        # Generate cat tables based on title
        for table_name in tables_to_sample_by_title:
            query_ = f"""
                CREATE TABLE cat_{table_name}_{i} AS
                SELECT *
                FROM {table_name}
                WHERE {table_name}.movie_id IN (
                    SELECT id
                    FROM cat_title_{i}
                );
            """
            new_tables.append(f"cat_{table_name}_{i}")
            cursor_.execute(query_)
            print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
            cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])
        

        # Generate cat keyword based on movie_keyword
        query_ = f"""
            CREATE TABLE cat_keyword_{i} AS
            SELECT *
            FROM keyword
            WHERE keyword.id IN (
                SELECT keyword_id
                FROM cat_movie_keyword_{i}
            );
        """
        new_tables.append(f"cat_keyword_{i}")
        cursor_.execute(query_)
        
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        # Generate cat company_name based on movie_companies
        query_ = f"""
            CREATE TABLE cat_company_name_{i} AS
            SELECT *
            FROM company_name
            WHERE company_name.id IN (
                SELECT company_id
                FROM cat_movie_companies_{i}
            );
        """
        new_tables.append(f"cat_company_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate cat aka_name based on cast_info
        query_ = f"""
            CREATE TABLE cat_aka_name_{i} AS
            SELECT *
            FROM aka_name
            WHERE aka_name.id IN (
                SELECT person_id
                FROM cat_cast_info_{i}
            );
        """
        new_tables.append(f"cat_aka_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])



        # Generate cat name based on aka_name
        query_ = f"""
            CREATE TABLE cat_name_{i} AS
            SELECT *
            FROM name
            WHERE name.id IN (
                SELECT id
                FROM cat_aka_name_{i}
            );
        """
        new_tables.append(f"cat_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])



        # Generate cat person_info based on name
        query_ = f"""
            CREATE TABLE cat_person_info_{i} AS
            SELECT *
            FROM person_info
            WHERE person_info.person_id IN (
                SELECT id
                FROM cat_name_{i}
            );
        """
        new_tables.append(f"cat_person_info_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])




        # Generate cat link_type based on movie_link
        query_ = f"""
            CREATE TABLE cat_link_type_{i} AS
            SELECT *
            FROM link_type
            WHERE link_type.id IN (
                SELECT link_type_id
                FROM cat_movie_link_{i}
            );
        """
        new_tables.append(f"cat_link_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])




        # Generate cat info_type based on person_info and movie_info
        query_ = f"""
            CREATE TABLE cat_info_type_{i} AS
            SELECT *
            FROM info_type
            WHERE info_type.id IN (
                SELECT info_type_id
                FROM cat_movie_info_{i}
            ) OR info_type.id IN (
                SELECT info_type_id
                FROM cat_person_info_{i}
            ) OR info_type.id IN (
                SELECT info_type_id
                FROM cat_movie_info_idx_{i}
            );
        """
        new_tables.append(f"cat_info_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])

        
        # Generate company_type
        query_ = f"""
            CREATE TABLE cat_company_type_{i} AS
            SELECT *
            FROM company_type
            WHERE company_type.id IN (
                SELECT company_type_id
                FROM cat_movie_companies_{i}
            );
        """
        new_tables.append(f"cat_company_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate cat_kind_type
        query_ = f"""
            CREATE TABLE cat_kind_type_{i} AS
            SELECT *
            FROM kind_type
            WHERE kind_type.id IN (
                SELECT kind_id
                FROM cat_title_{i}
            );
        """
        new_tables.append(f"cat_kind_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate char_name
        query_ = f"""
            CREATE TABLE cat_char_name_{i} AS
            SELECT *
            FROM char_name
            WHERE char_name.id IN (
                SELECT person_role_id
                FROM cat_cast_info_{i}
            );
        """
        new_tables.append(f"cat_char_name_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate role_type
        query_ = f"""
            CREATE TABLE cat_role_type_{i} AS
            SELECT *
            FROM role_type
            WHERE role_type.id IN (
                SELECT role_id
                FROM cat_cast_info_{i}
            );
        """
        new_tables.append(f"cat_role_type_{i}")
        cursor_.execute(query_)
        print(f"\"{new_tables[-1]}\": {get_count(cursor_, new_tables[-1])},")
        cache[new_tables[-1]] = get_count(cursor_, new_tables[-1])


        # Generate comp_cast_type
        query_ = f"""
            CREATE TABLE cat_comp_cast_type_{i} AS
            SELECT *
            FROM comp_cast_type
            WHERE comp_cast_type.id IN (
                SELECT status_id
                FROM cat_complete_cast_{i}
            ) OR comp_cast_type.id IN (
                SELECT subject_id
                FROM cat_complete_cast_{i}
            );
        """
        new_tables.append(f"cat_comp_cast_type_{i}")
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
        index_query = index_query.replace(' on ', f'_cat_{i} on cat_')
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
        fk_query = fk_query.replace('TABLE ', f'TABLE cat_')
        fk_query = fk_query.replace('REFERENCES ', f'REFERENCES cat_')
        cursor_.execute(fk_query)
        print(fk_query)

        # create histgram
        cursor_.execute("ANALYZE VERBOSE;")
        print("Done ANALYZE VERBOSE;")
    except Exception as e:
        print(e)
        drop_table(new_tables)


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
drop table cat_title_0 CASCADE;
drop table cat_movie_companies_0 CASCADE;
drop table cat_movie_keyword_0 CASCADE;
drop table cat_cast_info_0 CASCADE;
drop table cat_movie_link_0 CASCADE;
drop table cat_movie_info_0 CASCADE;
drop table cat_complete_cast_0 CASCADE;
drop table cat_aka_title_0 CASCADE;
drop table cat_movie_info_idx_0 CASCADE;
drop table cat_keyword_0 CASCADE;
drop table cat_company_name_0 CASCADE;
drop table cat_aka_name_0 CASCADE;
drop table cat_name_0 CASCADE;
drop table cat_person_info_0 CASCADE;
drop table cat_link_type_0 CASCADE;
drop table cat_info_type_0 CASCADE;
drop table cat_company_type_0 CASCADE;
drop table cat_kind_type_0 CASCADE;
drop table cat_char_name_0 CASCADE;
drop table cat_role_type_0 CASCADE;
drop table cat_comp_cast_type_0 CASCADE;
'''


# for i in range(2, 8):
#     verify_by_movie_category(i)

# input()

result_for_print = []
for i in range(1, 8):
    # for query_id in ["2a", "15a", "17a", "26a"]:
    for query_id in ["2a"]:

        os.system("rm -rf ~/imdb/recordx.log")
        db_name = "imdbloadbase"
        explain = "EXPLAIN (SUMMARY, COSTS, FORMAT JSON)"
        with open('./query/join-order-benchmark/' + query_id + '.sql') as p:
            sql = p.read()

        on_sample = "on-cat/"   
        # tmp_plan_dict_file = './plan/' + 'on-cat/' + 'tmp_plan_dict_' + db_name + '_' + query_id + '_1.txt'
        # based on 7
        # tmp_plan_dict_file = './plan/' + 'on-cat/' + 'tmp_plan_dict_' + db_name + '_' + query_id + '_7.txt'
        
        # based on 6
        tmp_plan_dict_file = './plan/' + 'on-cat/' + 'tmp_plan_dict_' + db_name + '_' + query_id + '_6.txt'
        
        
        plan_hint_dict = json.load(open(tmp_plan_dict_file))
        cur_plan_list = []
        for m in plan_hint_dict.values():
            cur_plan_list = cur_plan_list + m
        cur_plan_list = list(sorted(set(cur_plan_list)))
        # print([(id, plan) for id, plan in enumerate(cur_plan_list)])
        print(f"Total plan set has: {len(cur_plan_list)} plans.")
        new_sql = modify_query("cat_", f"_{i}", sql)
        print(new_sql)
        # input()
        # continue

        # Postgres + SRQO
        # robust_plans = {"2a":[5],"15a": [42], "17a":[1], '26a': [6]}
        # ori_plan = { "2a":[0], "17a":[19], "15a": [23], '26a': [11]}

        # based on 7
        # robust_plans = {"2a":[0],"15a": [0], "17a":[28], '26a': [14, 3]}
        # ori_plan = { "2a":[1], "15a": [2], "17a":[8], '26a': [1]}


        # based on 6
        robust_plans = {"2a":[1],"15a": [12], "17a":[6], '26a': [3, 4, 5, 10, 16, 17, 18, 22]}
        ori_plan = { "2a":[2], "15a": [12], "17a":[4], '26a': [0]}

        # print(cur_plan_list[4])
        # print(tmp_plan_dict_file)

        f = open("log/" + on_sample + "verify_" + query_id + ".txt", 'a+')

        # new_pg_latency = get_real_latency(db_name, new_sql, times=1, limit_time=1000)
        new_pg_latency = 0

        print(f"{i}: latency of new optimal plan:\n {new_pg_latency}", file=f)
        print(new_pg_latency)
        our_latency = []
        ori_latency = []
        for m in robust_plans[query_id]:
        # for i in range(len(cur_plan_list)):
            cur_rob = get_real_latency(db_name, new_sql, hint=cur_plan_list[m], output_plan=True, times=5, limit_time=1000)
            print(cur_rob)
            our_latency.append(cur_rob)
        print(f"{i}: latency of robust plan:\n {our_latency}", file=f)
        print(our_latency)
        ori_latency.append(get_real_latency(db_name, new_sql, hint=cur_plan_list[ori_plan[query_id][0]], times=10, query_id=query_id, output_plan=True, limit_time=100000))
        # round(get_real_latency(db_name, new_sql, hint=None, times=3, limit_time=1000000), 1)
        print(f"{i}: latency of original plan:\n {ori_latency}", file=f)
        # result = [ori_latency] +  + our_latency
        result = [new_pg_latency] + our_latency + ori_latency
        print(f"{i} result:\n {result}", file=f)
        result_for_print.append(result)
        print(result_for_print)
        f.close()
    # for m in result_for_print:
    #     print(m, file=open("log/" + on_sample + 'verify_' + query_id + ".txt", 'a+'))