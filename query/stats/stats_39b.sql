SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 votes as v,
 badges as b,
 users as u 
WHERE p.Id = c.PostId 
AND p.Id = pl.RelatedPostId 
AND p.Id = v.PostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND c.CreationDate>='2010-08-06 12:21:39'::timestamp 
AND c.CreationDate<='2014-09-11 20:55:34'::timestamp 
AND p.Score>=0 
AND p.Score<=13 
AND p.FavoriteCount>=0 
AND pl.LinkTypeId=1 
AND pl.CreationDate>='2011-03-11 18:50:29'::timestamp 
AND v.VoteTypeId=2 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp 
AND u.Reputation>=1 
AND u.CreationDate>='2011-02-17 03:42:02'::timestamp 
AND u.CreationDate<='2014-09-01 10:54:39'::timestamp;