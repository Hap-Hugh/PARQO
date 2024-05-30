
    SELECT MIN(an.name) AS alternative_name,
       MIN(chn.name) AS character_name,
       MIN(t.title) AS movie
    FROM aka_name AS an,
        char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        movie_companies AS mc,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE ci.note LIKE '%(producer)%'
    AND cn.country_code = '[us]' AND cn.name = 'YouTube'
    AND mc.note LIKE '%(200%)%' AND mc.note LIKE '%(worldwide)%'
    AND n.name LIKE '%Downey%Robert%'
    AND rt.role = 'actor'
    AND t.production_year > 1950
    AND ci.movie_id = t.id
    AND t.id = mc.movie_id
    AND ci.movie_id = mc.movie_id
    AND mc.company_id = cn.id
    AND ci.role_id = rt.id
    AND n.id = ci.person_id
    AND chn.id = ci.person_role_id
    AND an.person_id = n.id
    AND an.person_id = ci.person_id;

    