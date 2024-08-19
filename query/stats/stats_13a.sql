SELECT COUNT(*) 
FROM posts as p,
 postLinks as pl,
 postHistory as ph 
WHERE p.Id = pl.PostId 
AND pl.PostId = ph.PostId 
AND p.CreationDate>='2010-07-19 20:08:37'::timestamp 
AND ph.CreationDate>='2010-07-20 00:30:00'::timestamp;