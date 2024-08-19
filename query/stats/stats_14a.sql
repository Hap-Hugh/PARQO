SELECT COUNT(*) 
FROM posts as p,
 postLinks as pl,
 users as u 
WHERE p.Id = pl.PostId 
AND p.OwnerUserId = u.Id 
AND p.CommentCount<=17 
AND u.CreationDate<='2014-09-12 07:12:16'::timestamp;