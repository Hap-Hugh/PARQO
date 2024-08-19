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
AND c.CreationDate>='2010-08-01 12:12:41'::timestamp 
AND p.Score<=44 
AND p.FavoriteCount>=0 
AND p.FavoriteCount<=3 
AND p.CreationDate>='2010-08-11 13:53:56'::timestamp 
AND p.CreationDate<='2014-09-03 11:52:36'::timestamp 
AND pl.LinkTypeId=1 
AND pl.CreationDate<='2014-08-11 17:26:31'::timestamp 
AND ph.CreationDate>='2010-09-20 19:11:45'::timestamp 
AND v.CreationDate<='2014-09-11 00:00:00'::timestamp;