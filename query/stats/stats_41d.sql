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
AND p.CommentCount>=0 
AND ph.PostHistoryTypeId=2 
AND v.VoteTypeId=5;