SELECT COUNT(*) 
FROM comments as c,
 votes as v 
WHERE c.UserId = v.UserId 
AND c.Score=0;