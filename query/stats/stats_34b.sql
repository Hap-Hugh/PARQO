SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = ph.UserId 
AND u.Id = b.UserId 
AND p.PostTypeId=1 
AND p.Score<=35 
AND p.AnswerCount=1 
AND p.CommentCount<=17 
AND p.FavoriteCount>=0 
AND b.Date>='2010-07-27 17:58:45'::timestamp 
AND b.Date<='2014-09-06 17:33:22'::timestamp 
AND u.Views<=233 
AND u.DownVotes<=2 
AND u.CreationDate>='2010-09-16 16:00:55'::timestamp 
AND u.CreationDate<='2014-08-24 21:12:02'::timestamp;