SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 users as u 
WHERE v.UserId = u.Id 
AND c.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND c.Score=2 
AND p.AnswerCount>=0 
AND p.AnswerCount<=9 
AND p.CreationDate>='2010-07-20 18:17:25'::timestamp 
AND p.CreationDate<='2014-08-26 12:57:22'::timestamp 
AND ph.CreationDate<='2014-09-02 07:58:47'::timestamp 
AND v.BountyAmount>=0 
AND v.CreationDate>='2010-05-19 00:00:00'::timestamp 
AND u.UpVotes<=230 
AND u.CreationDate>='2010-09-22 01:07:10'::timestamp 
AND u.CreationDate<='2014-08-15 05:52:23'::timestamp;