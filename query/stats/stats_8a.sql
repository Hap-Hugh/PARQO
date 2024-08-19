SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 users as u 
WHERE c.UserId = u.Id 
AND u.Id = p.OwnerUserId 
AND c.CreationDate>='2010-08-05 00:36:02'::timestamp 
AND c.CreationDate<='2014-09-08 16:50:49'::timestamp 
AND p.ViewCount>=0 
AND p.ViewCount<=2897 
AND p.CommentCount>=0 
AND p.CommentCount<=16 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=10;