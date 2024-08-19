SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND c.UserId = u.Id 
AND c.CreationDate>='2010-07-27 17:46:38'::timestamp 
AND p.AnswerCount>=0 
AND p.AnswerCount<=4 
AND p.CommentCount>=0 
AND p.CommentCount<=11 
AND p.CreationDate>='2010-07-26 09:46:48'::timestamp 
AND p.CreationDate<='2014-09-13 10:09:50'::timestamp 
AND u.Reputation>=1 
AND u.CreationDate>='2010-08-03 19:42:40'::timestamp 
AND u.CreationDate<='2014-09-12 02:20:03'::timestamp;