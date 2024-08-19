SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE b.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.CreationDate>='2010-07-27 18:08:19'::timestamp 
AND ph.CreationDate<='2014-09-10 08:22:43'::timestamp 
AND p.PostTypeId=2;