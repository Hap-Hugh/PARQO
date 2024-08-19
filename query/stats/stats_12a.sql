SELECT COUNT(*) 
FROM posts as p,
 tags as t,
 votes as v 
WHERE p.Id = t.ExcerptPostId 
AND p.OwnerUserId = v.UserId 
AND p.CreationDate>='2010-07-20 02:01:05'::timestamp;