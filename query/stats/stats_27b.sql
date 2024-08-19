SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 votes as v,
 users as u 
WHERE u.Id = p.OwnerUserId 
AND p.Id = ph.PostId 
AND p.Id = v.PostId 
AND ph.CreationDate>='2010-07-21 00:44:08'::timestamp 
AND p.ViewCount>=0 
AND p.CommentCount>=0 
AND v.VoteTypeId=2 
AND u.Views>=0 
AND u.Views<=34 
AND u.UpVotes>=0;