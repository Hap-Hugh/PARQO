SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.CreationDate>='2010-07-27 15:46:34'::timestamp 
AND c.CreationDate<='2014-09-12 08:15:14'::timestamp 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-10 00:00:00'::timestamp 
AND u.CreationDate<='2014-09-03 01:06:41'::timestamp;