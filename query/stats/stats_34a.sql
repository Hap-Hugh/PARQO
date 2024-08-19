SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = ph.UserId 
AND u.Id = b.UserId 
AND c.CreationDate>='2010-07-31 05:18:59'::timestamp 
AND c.CreationDate<='2014-09-12 07:59:13'::timestamp 
AND p.Score>=-2 
AND p.ViewCount>=0 
AND p.ViewCount<=18281 
AND ph.PostHistoryTypeId=2 
AND b.Date>='2010-10-20 08:33:44'::timestamp 
AND u.Views>=0 
AND u.Views<=75;