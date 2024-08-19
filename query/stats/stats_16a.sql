SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 users as u 
WHERE v.PostId = p.Id 
AND v.UserId = u.Id 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND p.Score>=-1 
AND p.CreationDate>='2010-10-21 13:21:24'::timestamp 
AND p.CreationDate<='2014-09-09 15:12:22'::timestamp 
AND u.UpVotes>=0 
AND u.CreationDate>='2010-07-27 17:15:57'::timestamp 
AND u.CreationDate<='2014-09-03 12:47:42'::timestamp;