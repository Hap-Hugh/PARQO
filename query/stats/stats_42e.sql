SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND p.Id = c.PostId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND p.PostTypeId=1 
AND p.CommentCount>=0 
AND p.CommentCount<=12 
AND p.FavoriteCount>=0 
AND v.BountyAmount<=50;