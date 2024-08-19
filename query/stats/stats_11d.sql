SELECT COUNT(*) 
FROM comments as c,
 badges as b,
 users as u 
WHERE c.UserId = u.Id 
AND b.UserId = u.Id 
AND c.Score=0 
AND c.CreationDate>='2010-07-24 06:46:49'::timestamp 
AND b.Date>='2010-07-19 20:34:06'::timestamp 
AND b.Date<='2014-09-12 15:11:36'::timestamp 
AND u.UpVotes>=0;