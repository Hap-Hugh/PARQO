SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = v.UserId 
AND c.Score=0 
AND c.CreationDate<='2014-09-13 20:12:15'::timestamp 
AND p.CreationDate>='2010-07-27 01:51:15'::timestamp 
AND v.BountyAmount<=50 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND u.UpVotes>=0 
AND u.UpVotes<=12 
AND u.CreationDate>='2010-07-19 19:09:39'::timestamp;