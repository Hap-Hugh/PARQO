SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u 
WHERE ph.PostId = p.Id 
AND p.OwnerUserId = u.Id 
AND ph.CreationDate<='2014-08-17 21:24:11'::timestamp 
AND p.CreationDate>='2010-07-26 19:26:37'::timestamp 
AND p.CreationDate<='2014-08-22 14:43:39'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=6524 
AND u.Views>=0;