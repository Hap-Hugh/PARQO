SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND u.Id = c.UserId 
AND u.Id = v.UserId 
AND c.CreationDate>='2010-07-27 12:03:40'::timestamp 
AND p.Score>=0 
AND p.Score<=28 
AND p.ViewCount>=0 
AND p.ViewCount<=6517 
AND p.AnswerCount>=0 
AND p.AnswerCount<=5 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=8 
AND p.CreationDate>='2010-07-27 11:29:20'::timestamp 
AND p.CreationDate<='2014-09-13 02:50:15'::timestamp 
AND u.Views>=0 
AND u.CreationDate>='2010-07-27 09:38:05'::timestamp;