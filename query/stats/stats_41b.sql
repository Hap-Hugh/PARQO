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
AND c.Score=0 
AND p.Score<=32 
AND p.ViewCount<=4146 
AND pl.LinkTypeId=1 
AND v.CreationDate<='2014-09-10 00:00:00'::timestamp;