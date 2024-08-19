SELECT COUNT(*) 
FROM comments as c,
 postLinks as pl,
 postHistory as ph,
 votes as v,
 posts as p 
WHERE pl.PostId = p.Id 
AND c.PostId = p.Id 
AND v.PostId = p.Id 
AND ph.PostId = p.Id 
AND c.Score=0 
AND pl.CreationDate>='2011-11-21 22:39:41'::timestamp 
AND pl.CreationDate<='2014-09-01 16:29:56'::timestamp 
AND v.CreationDate>='2010-07-22 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-14 00:00:00'::timestamp;