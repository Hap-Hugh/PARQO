SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.CreationDate>='2010-10-01 20:45:26'::timestamp 
AND c.CreationDate<='2014-09-05 12:51:17'::timestamp 
AND v.BountyAmount<=100 
AND u.UpVotes=0 
AND u.CreationDate<='2014-09-12 03:25:34'::timestamp;