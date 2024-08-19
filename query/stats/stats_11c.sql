SELECT COUNT(*) 
FROM comments as c,
 badges as b,
 users as u 
WHERE c.UserId = u.Id 
AND b.UserId = u.Id 
AND c.CreationDate>='2010-08-12 20:27:30'::timestamp 
AND c.CreationDate<='2014-09-12 12:49:19'::timestamp 
AND u.Views>=0 
AND u.DownVotes>=0 
AND u.DownVotes<=2;