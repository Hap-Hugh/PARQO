SELECT COUNT(*) 
FROM postHistory as ph,
 votes as v,
 users as u,
 badges as b 
WHERE u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = v.UserId 
AND v.CreationDate<='2014-09-10 00:00:00'::timestamp 
AND u.DownVotes>=0 
AND u.DownVotes<=3 
AND u.UpVotes>=0 
AND u.UpVotes<=71 
AND b.Date>='2010-07-19 21:54:06'::timestamp;