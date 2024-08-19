SELECT COUNT(*) 
FROM postHistory as ph,
 votes as v,
 users as u,
 badges as b 
WHERE u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = v.UserId 
AND ph.PostHistoryTypeId=1 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND u.Reputation<=126 
AND u.Views<=11 
AND u.CreationDate>='2010-08-02 16:17:58'::timestamp 
AND u.CreationDate<='2014-09-12 00:16:30'::timestamp 
AND b.Date<='2014-09-03 16:13:12'::timestamp;