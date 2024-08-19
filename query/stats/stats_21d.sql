SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 badges as b,
 users as u 
WHERE u.Id = v.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND v.CreationDate<='2014-09-06 00:00:00'::timestamp 
AND p.Score<=48 
AND p.AnswerCount<=8 
AND b.Date>='2011-01-03 20:50:19'::timestamp 
AND b.Date<='2014-09-02 15:35:07'::timestamp 
AND u.CreationDate>='2010-11-16 06:03:04'::timestamp;