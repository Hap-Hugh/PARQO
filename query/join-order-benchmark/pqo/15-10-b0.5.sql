
    SELECT MIN(mi.info) AS release_date,
       MIN(t.title) AS internet_movie
    FROM aka_title AS aka_t,
        company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        keyword AS k,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        title AS t
    WHERE cn.country_code !='[pl]' AND (cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')
    AND it1.info = 'countries'
    AND mc.note LIKE '%(200%)%' AND mc.note LIKE '%(worldwide)%'
    AND mi.info = 'Horror'
    AND t.production_year > 2010 AND (t.title LIKE '%murder%' OR t.title LIKE '%Murder%' OR t.title LIKE '%Mord%')
    AND t.id = aka_t.movie_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mc.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mc.movie_id
    AND mk.movie_id = aka_t.movie_id
    AND mi.movie_id = mc.movie_id
    AND mi.movie_id = aka_t.movie_id
    AND mc.movie_id = aka_t.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id;
    