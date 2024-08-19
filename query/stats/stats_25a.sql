SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = ph.UserId 
AND u.Id = b.UserId 
AND c.Score=0 
AND c.CreationDate>='2010-09-05 16:04:35'::timestamp 
AND c.CreationDate<='2014-09-11 04:35:36'::timestamp 
AND ph.PostHistoryTypeId=1 
AND ph.CreationDate>='2010-07-26 20:01:58'::timestamp 
AND ph.CreationDate<='2014-09-13 17:29:23'::timestamp 
AND b.Date<='2014-09-04 08:54:56'::timestamp;