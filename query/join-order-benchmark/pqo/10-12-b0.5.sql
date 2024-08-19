
    SELECT MIN(chn.name) AS uncredited_voiced_character,
       MIN(t.title) AS russian_movie
    FROM char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        company_type AS ct,
        movie_companies AS mc,
        role_type AS rt,
        title AS t
    WHERE ci.note IN ('(writer)', '(head writer)', '(written by)', '(story)', '(story editor)')
    AND cn.country_code ='[us]'
    AND rt.role ='actress'
    AND t.title != '' AND (t.title LIKE 'Champion%' OR t.title LIKE 'Loser%')
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND ci.movie_id = mc.movie_id
    AND chn.id = ci.person_role_id
    AND rt.id = ci.role_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id;
    