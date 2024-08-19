SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id =c.UserId 
AND c.UserId = p.OwnerUserId 
AND p.OwnerUserId = v.UserId 
AND v.UserId = b.UserId 
AND c.Score=1 
AND p.Score>=-1 
AND p.Score<=29 
AND p.CreationDate>='2010-07-19 20:40:36'::timestamp 
AND p.CreationDate<='2014-09-10 20:52:30'::timestamp 
AND v.BountyAmount<=50 
AND b.Date<='2014-08-25 19:05:46'::timestamp 
AND u.DownVotes<=11 
AND u.CreationDate>='2010-07-31 17:32:56'::timestamp 
AND u.CreationDate<='2014-09-07 16:06:26'::timestamp;