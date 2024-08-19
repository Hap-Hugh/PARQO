SELECT COUNT(*) 
FROM comments as c,
 votes as v,
 users as u,
 posts as p 
WHERE c.PostId = p.Id 
AND u.Id = c.UserId 
AND v.PostId = p.Id 
AND c.Score=0 
AND u.Views>=0 
AND u.Views<=74;