
    SELECT MIN(t.title) AS movie_title
    FROM company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        title AS t
    WHERE cn.country_code ='[us]'
  AND cn.name = 'DreamWorks Animation'
    AND k.keyword IN ('superhero', 'marvel-comics', 'based-on-comic', 'tv-special', 'fight', 'violence', 'magnet', 'web', 'claw', 'laser')
    AND cn.id = mc.company_id
    AND mc.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND mc.movie_id = mk.movie_id;
    