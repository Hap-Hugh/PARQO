SELECT COUNT(*) 
FROM tags as t,
 posts as p,
 users as u,
 votes as v,
 badges as b 
WHERE u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND u.Id = v.UserId 
AND p.Id = t.ExcerptPostId 
AND p.CommentCount>=0 
AND p.CommentCount<=13 
AND u.Reputation>=1 
AND b.Date<='2014-09-06 17:33:22'::timestamp;