SELECT COUNT(*) 
FROM votes as v,
 posts as p,
 badges as b,
 users as u 
WHERE p.Id = v.PostId 
AND u.Id = p.OwnerUserId 
AND u.Id = b.UserId 
AND p.Score<=22 
AND u.Reputation>=1;