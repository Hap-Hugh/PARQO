
    SELECT MIN(n.name) AS of_person,
       MIN(t.title) AS biography_movie
    FROM aka_name AS an,
        cast_info AS ci,
        info_type AS it,
        link_type AS lt,
        movie_link AS ml,
        name AS n,
        person_info AS pi,
        title AS t
    WHERE an.name like '%a%'
    AND it.info ='mini biography'
    AND lt.link LIKE '%follows%'
    AND n.name LIKE 'B%'
    AND pi.note ='Volker Boehm'
    AND t.production_year > 2000
  AND (t.title LIKE '%Freddy%'
       OR t.title LIKE '%Jason%'
       OR t.title LIKE 'Saw%')
    AND n.id = an.person_id
    AND n.id = pi.person_id
    AND ci.person_id = n.id
    AND t.id = ci.movie_id
    AND ml.linked_movie_id = t.id
    AND lt.id = ml.link_type_id
    AND it.id = pi.info_type_id
    AND pi.person_id = an.person_id
    AND pi.person_id = ci.person_id
    AND an.person_id = ci.person_id
    AND ci.movie_id = ml.linked_movie_id;
    