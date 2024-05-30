
    
    SELECT MIN(cn.name) AS movie_company,
       MIN(mi_idx.info) AS rating,
       MIN(t.title) AS drama_horror_movie
    FROM company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        info_type AS it2,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        title AS t
    WHERE cn.country_code = '[ru]'
    AND ct.kind = 'production companies'
    AND it1.info = 'countries'
    AND it2.info = 'rating'
    AND mi.info IN ('Sweden', 'Norway', 'Germany', 'Denmark', 'Swedish', 'Denish', 'Norwegian', 'German', 'USA', 'American')
    AND mi_idx.info < '3.5'
    AND t.production_year > 2000
  AND (t.title LIKE '%Freddy%'
       OR t.title LIKE '%Jason%'
       OR t.title LIKE 'Saw%')
    AND t.id = mi.movie_id
    AND t.id = mi_idx.movie_id
    AND mi.info_type_id = it1.id
    AND mi_idx.info_type_id = it2.id
    AND t.id = mc.movie_id
    AND ct.id = mc.company_type_id
    AND cn.id = mc.company_id
    AND mc.movie_id = mi.movie_id
    AND mc.movie_id = mi_idx.movie_id
    AND mi.movie_id = mi_idx.movie_id;
    