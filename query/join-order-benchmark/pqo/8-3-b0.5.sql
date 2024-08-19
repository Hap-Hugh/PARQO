
    SELECT MIN(an1.name) AS actress_pseudonym,
       MIN(t.title) AS japanese_movie_dubbed
    FROM aka_name AS an1,
        cast_info AS ci,
        company_name AS cn,
        movie_companies AS mc,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE ci.note IN ('(voice)', '(voice: Japanese version)', '(voice) (uncredited)', '(voice: English version)')
    AND cn.country_code ='[us]'
    AND mc.note LIKE '%(Blu-ray)%'
    AND n.name LIKE '%Downey%Robert%'
    AND rt.role ='actress'
    AND an1.person_id = n.id
    AND n.id = ci.person_id
    AND ci.movie_id = t.id
    AND t.id = mc.movie_id
    AND mc.company_id = cn.id
    AND ci.role_id = rt.id
    AND an1.person_id = ci.person_id
    AND ci.movie_id = mc.movie_id;
    