
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
    AND cn.country_code ='[us]'
    AND mc.note NOT LIKE '%(USA)%'
  AND mc.note LIKE '%(200%)%'
    AND n.gender = 'm'
    AND rt.role ='writer'
    AND t.production_year >2000 AND (t.title LIKE 'Birdemic%' OR t.title LIKE '%Movie%')
    AND ci.movie_id = t.id
    AND t.id = mc.movie_id
    AND ci.movie_id = mc.movie_id
    AND mc.company_id = cn.id
    AND ci.role_id = rt.id
    AND n.id = ci.person_id
    AND chn.id = ci.person_role_id
    AND an.person_id = n.id
    AND an.person_id = ci.person_id;

    