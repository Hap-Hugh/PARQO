
        SELECT MIN(k.keyword) AS movie_keyword,
       MIN(n.name) AS actor_name,
       MIN(t.title) AS marvel_movie
FROM cast_info AS ci,
     keyword AS k,
     movie_keyword AS mk,
     name AS n,
     title AS t
WHERE k.keyword IN ('hero', 'martial-arts', 'hand-to-hand-combat')
  AND n.gender ='f' AND n.name LIKE '%Angel%'
  AND t.production_year >2000 AND (t.title LIKE 'Birdemic%' OR t.title LIKE '%Movie%')
  AND k.id = mk.keyword_id
  AND t.id = mk.movie_id
  AND t.id = ci.movie_id
  AND ci.movie_id = mk.movie_id
  AND n.id = ci.person_id;
        