SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u 
WHERE p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.CreationDate>='2011-05-20 18:43:03'::timestamp 
AND p.FavoriteCount<=5 
AND u.Views>=0 
AND u.UpVotes>=0 
AND u.CreationDate>='2010-11-27 21:46:49'::timestamp 
AND u.CreationDate<='2014-08-18 13:00:22'::timestamp;