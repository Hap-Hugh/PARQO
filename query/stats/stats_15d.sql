SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u 
WHERE p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.CreationDate>='2010-08-21 05:30:40'::timestamp 
AND p.Score>=0 
AND u.Reputation>=1 
AND u.UpVotes<=198 
AND u.CreationDate>='2010-07-19 20:49:05'::timestamp;