SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 badges as b 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND b.UserId = c.UserId 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-10 00:00:00'::timestamp;