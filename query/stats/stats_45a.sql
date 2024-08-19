SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = pl.RelatedPostId 
AND b.UserId = u.Id 
AND c.UserId = u.Id 
AND p.Id = v.PostId 
AND p.Id = c.PostId 
AND p.Id = ph.PostId 
AND c.Score=0 
AND p.ViewCount>=0 
AND p.AnswerCount<=5 
AND p.CommentCount<=12 
AND p.FavoriteCount>=0 
AND pl.LinkTypeId=1 
AND pl.CreationDate>='2011-02-16 20:04:50'::timestamp 
AND pl.CreationDate<='2014-09-01 16:48:04'::timestamp 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND v.CreationDate<='2014-08-31 00:00:00'::timestamp 
AND b.Date>='2010-08-06 10:36:45'::timestamp 
AND b.Date<='2014-09-12 07:19:35'::timestamp;