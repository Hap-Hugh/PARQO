SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = b.UserId 
AND u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.Score=1 
AND c.CreationDate>='2010-07-20 23:17:28'::timestamp 
AND u.CreationDate>='2010-07-20 01:27:29'::timestamp;