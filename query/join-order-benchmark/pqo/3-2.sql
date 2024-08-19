
    SELECT MIN(t.title) AS movie_title
    FROM keyword AS k,
        movie_info AS mi,
        movie_keyword AS mk,
        title AS t
    WHERE k.keyword IN ('sequel', 'revenge', 'based-on-novel')
    AND mi.info IN ('Drama', 'Horror')
    AND t.title != '' AND (t.title LIKE 'Champion%' OR t.title LIKE 'Loser%')
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND mk.movie_id = mi.movie_id
    AND k.id = mk.keyword_id;
    