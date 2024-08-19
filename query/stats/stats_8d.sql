SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND c.UserId = u.Id 
AND c.Score=0 
AND p.AnswerCount<=5 
AND p.CommentCount>=0 
AND p.CommentCount<=11 
AND p.FavoriteCount<=27 
AND u.Reputation>=1;