SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = c.UserId 
AND c.CreationDate<='2014-08-28 00:18:24'::timestamp 
AND b.Date>='2010-09-15 02:50:48'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=1443 
AND u.DownVotes>=0 
AND u.DownVotes<=3;