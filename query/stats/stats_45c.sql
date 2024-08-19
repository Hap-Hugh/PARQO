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
AND c.CreationDate>='2010-07-26 17:09:48'::timestamp 
AND p.PostTypeId=1 
AND p.AnswerCount>=0 
AND p.CommentCount>=0 
AND p.CommentCount<=14 
AND pl.CreationDate>='2010-10-27 10:02:57'::timestamp 
AND pl.CreationDate<='2014-09-04 17:23:50'::timestamp 
AND ph.CreationDate<='2014-09-11 20:09:41'::timestamp 
AND v.CreationDate>='2010-07-21 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-14 00:00:00'::timestamp;