SELECT COUNT(*) 
FROM comments as c,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND c.UserId = b.UserId 
AND c.Score=0 
AND b.Date>='2010-07-19 20:54:06'::timestamp 
AND u.DownVotes>=0 
AND u.UpVotes>=0 
AND u.UpVotes<=17 
AND u.CreationDate>='2010-08-06 07:03:05'::timestamp 
AND u.CreationDate<='2014-09-08 04:18:44'::timestamp;