SELECT COUNT(*) 
FROM comments as c,
 postLinks as pl,
 posts as p,
 users as u,
 badges as b 
WHERE p.Id = pl.RelatedPostId 
AND p.Id = c.PostId 
AND u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND c.CreationDate<='2014-09-08 15:58:08'::timestamp 
AND p.ViewCount>=0 
AND u.Reputation>=1;