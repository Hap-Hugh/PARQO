SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 users as u 
WHERE u.Id = c.UserId 
AND c.UserId = ph.UserId 
AND u.Reputation>=1 
AND u.Reputation<=487 
AND u.UpVotes<=27 
AND u.CreationDate>='2010-10-22 22:40:35'::timestamp 
AND u.CreationDate<='2014-09-10 17:01:31'::timestamp;