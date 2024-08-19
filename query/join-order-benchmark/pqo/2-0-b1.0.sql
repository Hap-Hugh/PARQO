
    SELECT MIN(t.title) AS movie_title
    FROM company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        title AS t
    WHERE cn.country_code ='[us]'
    AND k.keyword IN ('superhero', 'sequel', 'second-part', 'marvel-comics', 'based-on-comic', 'tv-special', 'fight', 'violence')
    AND cn.id = mc.company_id
    AND mc.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND mc.movie_id = mk.movie_id;
    