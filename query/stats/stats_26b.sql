SELECT COUNT(*) 
FROM postLinks as pl,
 posts as p,
 users as u,
 badges as b 
WHERE p.Id = pl.RelatedPostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND pl.CreationDate<='2014-08-17 01:23:50'::timestamp 
AND p.Score>=-1 
AND p.Score<=10 
AND p.AnswerCount<=5 
AND p.CommentCount=2 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=6 
AND u.Views<=33 
AND u.DownVotes>=0 
AND u.CreationDate>='2010-08-19 17:31:36'::timestamp 
AND u.CreationDate<='2014-08-06 07:23:12'::timestamp 
AND b.Date<='2014-09-10 22:50:06'::timestamp;