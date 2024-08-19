SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE b.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.CreationDate>='2010-07-19 19:52:31'::timestamp 
AND p.Score>=0 
AND u.CreationDate>='2010-07-27 02:56:06'::timestamp 
AND u.CreationDate<='2014-09-10 10:44:00'::timestamp;