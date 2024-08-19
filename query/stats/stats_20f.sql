SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND p.Score>=0 
AND p.Score<=16 
AND p.ViewCount>=0 
AND p.CreationDate<='2014-09-09 12:00:50'::timestamp 
AND u.Reputation>=1 
AND u.CreationDate>='2010-07-19 19:08:49'::timestamp 
AND u.CreationDate<='2014-08-28 12:15:56'::timestamp;