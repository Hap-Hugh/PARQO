SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 users as u 
WHERE v.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND p.CommentCount>=0 
AND u.CreationDate>='2010-12-15 06:00:24'::timestamp;