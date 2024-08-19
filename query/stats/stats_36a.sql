SELECT COUNT(*) 
FROM tags as t,
 posts as p,
 users as u,
 postHistory as ph,
 badges as b 
WHERE p.Id = t.ExcerptPostId 
AND u.Id = ph.UserId 
AND u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND p.CommentCount>=0 
AND u.DownVotes<=0 
AND b.Date<='2014-08-22 02:21:55'::timestamp;