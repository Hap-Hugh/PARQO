SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = v.UserId 
AND u.Id = b.UserId 
AND c.Score=0 
AND v.BountyAmount>=0 
AND v.BountyAmount<=300 
AND v.CreationDate>='2010-07-29 00:00:00'::timestamp 
AND u.UpVotes>=0 
AND u.UpVotes<=18;