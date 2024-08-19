
    SELECT MIN(t.title) AS movie_title
    FROM company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        title AS t
    WHERE cn.country_code !='[pl]' AND (cn.name LIKE '20th Century Fox%' OR cn.name LIKE 'Twentieth Century Fox%')
    AND k.keyword IN ('murder', 'murder-in-title', 'blood', 'violence')
    AND cn.id = mc.company_id
    AND mc.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND mc.movie_id = mk.movie_id;
    