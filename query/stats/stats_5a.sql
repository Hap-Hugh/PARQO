SELECT COUNT(*) 
FROM badges as b,
 posts as p 
WHERE b.UserId = p.OwnerUserId 
AND b.Date<='2014-09-11 08:55:52'::timestamp 
AND p.AnswerCount>=0 
AND p.AnswerCount<=4 
AND p.CommentCount>=0 
AND p.CommentCount<=17;