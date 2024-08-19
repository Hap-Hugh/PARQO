SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 users as u 
WHERE c.UserId = u.Id 
AND ph.UserId = u.Id 
AND u.Reputation>=1 
AND u.Reputation<=7931 
AND u.Views<=109 
AND u.DownVotes>=0 
AND u.CreationDate<='2014-09-12 13:12:56'::timestamp;