SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND u.Id = b.UserId 
AND c.Score=0 
AND v.BountyAmount>=0 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp 
AND u.DownVotes<=57 
AND u.CreationDate>='2010-08-26 09:01:31'::timestamp 
AND u.CreationDate<='2014-08-10 11:01:39'::timestamp;