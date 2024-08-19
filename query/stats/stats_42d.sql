SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND p.Id = c.PostId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND p.ViewCount>=0 
AND p.AnswerCount>=0 
AND p.AnswerCount<=7 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=17 
AND v.VoteTypeId=5 
AND b.Date>='2010-08-01 02:54:53'::timestamp 
AND u.Reputation>=1 
AND u.Views>=0 
AND u.CreationDate>='2010-08-19 06:26:34'::timestamp 
AND u.CreationDate<='2014-09-11 05:22:26'::timestamp;