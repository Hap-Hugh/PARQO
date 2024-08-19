
    SELECT MIN(t.title) AS typical_european_movie
    FROM company_type AS ct,
        info_type AS it,
        movie_companies AS mc,
        movie_info AS mi,
        title AS t
    WHERE ct.kind != 'production companies' AND ct.kind IS NOT NULL
    AND mc.note IS NULL
    AND mi.info IN ('Sweden', 'Norway', 'Germany', 'Denmark', 'Swedish', 'Denish', 'Norwegian', 'German')
    AND t.title = 'Shrek 2'
  AND t.production_year BETWEEN 2000 AND 2010
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND mc.movie_id = mi.movie_id
    AND ct.id = mc.company_type_id
    AND it.id = mi.info_type_id;
    