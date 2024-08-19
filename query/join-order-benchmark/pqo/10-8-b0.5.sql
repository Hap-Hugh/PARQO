
    SELECT MIN(chn.name) AS uncredited_voiced_character,
       MIN(t.title) AS russian_movie
    FROM char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        company_type AS ct,
        movie_companies AS mc,
        role_type AS rt,
        title AS t
    WHERE ci.note IN ('(voice)', '(voice: Japanese version)', '(voice) (uncredited)', '(voice: English version)')
    AND cn.country_code !='[pl]'
  AND (cn.name LIKE '%Film%'
       OR cn.name LIKE '%Warner%')
    AND rt.role ='actress'
    AND t.title = 'Shrek 2'
  AND t.production_year BETWEEN 2000 AND 2005
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND ci.movie_id = mc.movie_id
    AND chn.id = ci.person_role_id
    AND rt.id = ci.role_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id;
    