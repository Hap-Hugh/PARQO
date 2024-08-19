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
AND c.Score=0 
AND p.Score<=67 
AND ph.PostHistoryTypeId=34 
AND b.Date<='2014-08-20 12:16:56'::timestamp;