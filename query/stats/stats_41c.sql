SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 badges as b 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND b.UserId = c.UserId 
AND c.CreationDate>='2010-07-26 20:21:15'::timestamp 
AND c.CreationDate<='2014-09-13 18:12:10'::timestamp 
AND p.Score<=61 
AND p.ViewCount<=3627 
AND p.AnswerCount>=0 
AND p.AnswerCount<=5 
AND p.CommentCount<=8 
AND p.FavoriteCount>=0 
AND v.VoteTypeId=2 
AND v.CreationDate>='2010-07-27 00:00:00'::timestamp 
AND b.Date>='2010-07-30 03:49:24'::timestamp;