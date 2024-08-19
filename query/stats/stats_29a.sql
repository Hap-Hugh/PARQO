SELECT COUNT(*) 
FROM postHistory as ph,
 votes as v,
 users as u,
 badges as b 
WHERE u.Id = ph.UserId 
AND u.Id = v.UserId 
AND u.Id = b.UserId 
AND ph.PostHistoryTypeId=2 
AND u.Views=5 
AND u.DownVotes>=0 
AND u.UpVotes>=0 
AND u.UpVotes<=224 
AND u.CreationDate<='2014-09-04 04:41:22'::timestamp 
AND b.Date>='2010-07-19 19:39:10'::timestamp 
AND b.Date<='2014-09-05 18:37:48'::timestamp;