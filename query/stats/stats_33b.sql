SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 votes as v,
 badges as b,
 users as u 
WHERE u.Id =c.UserId 
AND c.UserId = p.OwnerUserId 
AND p.OwnerUserId = v.UserId 
AND v.UserId = b.UserId 
AND c.Score=1 
AND p.Score>=-2 
AND p.Score<=23 
AND p.ViewCount<=2432 
AND p.CommentCount=0 
AND p.FavoriteCount>=0 
AND u.Reputation>=1 
AND u.Reputation<=113 
AND u.Views>=0 
AND u.Views<=51;