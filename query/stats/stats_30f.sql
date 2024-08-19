SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postLinks as pl,
 postHistory as ph,
 votes as v 
WHERE p.Id = pl.PostId 
AND p.Id = v.PostId 
AND p.Id = ph.PostId 
AND p.Id = c.PostId 
AND c.Score=0 
AND p.FavoriteCount>=0 
AND p.CreationDate>='2010-07-23 02:00:12'::timestamp 
AND p.CreationDate<='2014-09-08 13:52:41'::timestamp 
AND pl.LinkTypeId=1 
AND pl.CreationDate>='2011-10-06 21:41:26'::timestamp 
AND v.VoteTypeId=2;