SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp 
AND u.CreationDate>='2010-07-19 20:11:48'::timestamp 
AND u.CreationDate<='2014-07-09 20:37:10'::timestamp;