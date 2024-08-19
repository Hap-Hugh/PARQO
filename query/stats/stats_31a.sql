SELECT COUNT(*) 
FROM comments as c,
 posts as p,
 postHistory as ph,
 votes as v,
 users as u 
WHERE u.Id = c.UserId 
AND c.UserId = p.OwnerUserId 
AND p.OwnerUserId = ph.UserId 
AND ph.UserId = v.UserId 
AND p.Score<=13 
AND p.AnswerCount>=0 
AND p.AnswerCount<=4 
AND p.CommentCount>=0 
AND p.FavoriteCount<=2 
AND ph.PostHistoryTypeId=3 
AND v.BountyAmount<=50 
AND u.DownVotes>=0;