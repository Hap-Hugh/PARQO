SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 votes as v,
 posts as p 
WHERE ph.PostId = p.Id 
AND c.PostId = p.Id 
AND v.PostId = p.Id 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp;