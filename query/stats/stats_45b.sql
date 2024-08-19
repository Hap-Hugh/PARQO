SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = pl.RelatedPostId 
AND b.UserId = u.Id 
AND c.UserId = u.Id 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND p.Id = ph.PostId 
AND p.Score<=40 
AND p.CommentCount>=0 
AND p.CreationDate>='2010-07-28 17:40:56'::timestamp 
AND p.CreationDate<='2014-09-11 04:22:44'::timestamp 
AND pl.LinkTypeId=1;