
    SELECT MIN(t.title) AS typical_european_movie
    FROM company_type AS ct,
        info_type AS it,
        movie_companies AS mc,
        movie_info AS mi,
        title AS t
    WHERE ct.kind != 'production companies' AND ct.kind IS NOT NULL
    AND mc.note LIKE '%(VHS)%' AND mc.note LIKE '%(USA)%' AND mc.note LIKE '%(1994)%'
    AND mi.info IN ('Germany', 'German', 'USA', 'American')
    AND t.title != '' AND (t.title LIKE 'Champion%' OR t.title LIKE 'Loser%')
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND mc.movie_id = mi.movie_id
    AND ct.id = mc.company_type_id
    AND it.id = mi.info_type_id;
    