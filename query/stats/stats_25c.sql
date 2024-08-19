SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = c.UserId 
AND c.CreationDate<='2014-09-10 00:33:30'::timestamp 
AND u.DownVotes<=0 
AND u.UpVotes<=47;