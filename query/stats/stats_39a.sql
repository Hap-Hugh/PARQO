SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.Id = v.PostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND u.Views<=190 
AND u.CreationDate>='2010-07-20 08:05:39'::timestamp 
AND u.CreationDate<='2014-08-27 09:31:28'::timestamp;