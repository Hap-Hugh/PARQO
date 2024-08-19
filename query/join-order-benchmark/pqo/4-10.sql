
    SELECT MIN(mi_idx.info) AS rating,
       MIN(t.title) AS movie_title
    FROM info_type AS it,
        keyword AS k,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        title AS t
    WHERE it.info = 'top 250 rank'
    AND k.keyword IN ('murder', 'murder-in-title', 'blood', 'violence')
    AND mi_idx.info > '9.0'
    AND t.production_year BETWEEN 1950 AND 2000
    AND t.id = mi_idx.movie_id
    AND t.id = mk.movie_id
    AND mk.movie_id = mi_idx.movie_id
    AND k.id = mk.keyword_id
    AND it.id = mi_idx.info_type_id;
    