SELECT COUNT(*) 
FROM tags as t,
 posts as p,
 users as u,
 votes as v,
 badges as b 
WHERE p.Id = t.ExcerptPostId 
AND u.Id = v.UserId 
AND u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND u.DownVotes>=0;