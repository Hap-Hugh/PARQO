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
AND c.CreationDate>='2010-07-22 01:19:43'::timestamp 
AND p.Score>=-1 
AND p.ViewCount>=0 
AND p.CommentCount<=9 
AND ph.CreationDate>='2010-09-20 17:45:15'::timestamp 
AND ph.CreationDate<='2014-08-07 01:00:45'::timestamp 
AND v.VoteTypeId=15;