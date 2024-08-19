SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE b.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.PostHistoryTypeId=5 
AND p.ViewCount>=0 
AND p.ViewCount<=2024 
AND u.Reputation>=1 
AND u.Reputation<=750 
AND b.Date>='2010-07-20 10:34:10'::timestamp;