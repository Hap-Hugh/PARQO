
    SELECT MIN(cn.name) AS from_company,
       MIN(lt.link) AS movie_link_type,
       MIN(t.title) AS non_polish_sequel_movie
    FROM company_name AS cn,
        company_type AS ct,
        keyword AS k,
        link_type AS lt,
        movie_companies AS mc,
        movie_keyword AS mk,
        movie_link AS ml,
        title AS t
    WHERE cn.country_code ='[us]'
    AND ct.kind != 'production companies' AND ct.kind IS NOT NULL
    AND k.keyword IN ('hero', 'martial-arts', 'hand-to-hand-combat')
    AND lt.link ='features'
    AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
    AND t.title = 'Shrek 2'
  AND t.production_year BETWEEN 2000 AND 2010
    AND lt.id = ml.link_type_id
    AND ml.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_type_id = ct.id
    AND mc.company_id = cn.id
    AND ml.movie_id = mk.movie_id
    AND ml.movie_id = mc.movie_id
    AND mk.movie_id = mc.movie_id;
    