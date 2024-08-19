SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE b.UserId = u.Id 
AND p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND ph.PostHistoryTypeId=2 
AND ph.CreationDate>='2011-01-08 03:03:48'::timestamp 
AND ph.CreationDate<='2014-08-25 14:04:43'::timestamp 
AND p.AnswerCount<=4 
AND p.CommentCount>=0 
AND p.CommentCount<=12 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=89 
AND p.CreationDate<='2014-09-02 10:21:04'::timestamp 
AND u.Reputation<=705 
AND u.CreationDate>='2010-07-28 23:56:00'::timestamp 
AND u.CreationDate<='2014-09-02 10:04:41'::timestamp 
AND b.Date>='2010-07-20 20:47:27'::timestamp 
AND b.Date<='2014-09-09 13:24:28'::timestamp;