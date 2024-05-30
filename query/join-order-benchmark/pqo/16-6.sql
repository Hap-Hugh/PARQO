
    SELECT MIN(an.name) AS cool_actor_pseudonym,
       MIN(t.title) AS series_named_after_char
    FROM aka_name AS an,
        cast_info AS ci,
        company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        name AS n,
        title AS t
    WHERE cn.country_code !='[pl]' AND (cn.name LIKE '20th Century Fox%' OR cn.name LIKE 'Twentieth Century Fox%')
    AND k.keyword IN ('murder', 'murder-in-title', 'blood', 'violence')
    AND t.production_year > 2005
    AND an.person_id = n.id
    AND n.id = ci.person_id
    AND ci.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_id = cn.id
    AND an.person_id = ci.person_id
    AND ci.movie_id = mc.movie_id
    AND ci.movie_id = mk.movie_id
    AND mc.movie_id = mk.movie_id;