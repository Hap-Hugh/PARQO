SELECT COUNT(*) 
FROM comments as c,
 badges as b 
WHERE c.UserId = b.UserId 
AND c.Score=0 
AND b.Date<='2014-09-11 14:33:06'::timestamp;