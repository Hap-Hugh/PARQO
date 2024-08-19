SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u 
WHERE p.OwnerUserId = u.Id 
AND ph.UserId = u.Id 
AND p.Score>=-1 
AND p.CommentCount>=0 
AND p.CommentCount<=23 
AND u.DownVotes=0 
AND u.UpVotes>=0 
AND u.UpVotes<=244;