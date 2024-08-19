SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 badges as b,
 users as u 
WHERE u.Id = v.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND p.Score>=0 
AND p.Score<=30 
AND p.CommentCount=0 
AND p.CreationDate>='2010-07-27 15:30:31'::timestamp 
AND p.CreationDate<='2014-09-04 17:45:10'::timestamp;