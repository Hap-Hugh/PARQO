SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 votes as v,
 users as u 
WHERE ph.UserId = u.Id 
AND v.UserId = u.Id 
AND c.UserId = u.Id 
AND b.UserId = u.Id 
AND b.Date>='2010-09-26 12:17:14'::timestamp 
AND v.BountyAmount>=0 
AND v.CreationDate>='2010-07-20 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp 
AND u.DownVotes>=0 
AND u.DownVotes<=0 
AND u.UpVotes>=0 
AND u.UpVotes<=31 
AND u.CreationDate<='2014-08-06 20:38:52'::timestamp;