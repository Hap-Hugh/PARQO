SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.CreationDate>='2010-08-10 17:55:45'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=691;