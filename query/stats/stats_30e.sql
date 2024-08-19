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
AND pl.LinkTypeId=1 
AND pl.CreationDate>='2011-06-14 13:31:35'::timestamp 
AND v.CreationDate>='2010-07-19 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-10 00:00:00'::timestamp;