SELECT COUNT(*) 
FROM postHistory as ph,
 posts as p,
 users as u,
 badges as b 
WHERE u.Id = p.OwnerUserId 
AND p.OwnerUserId = ph.UserId 
AND ph.UserId = b.UserId 
AND ph.PostHistoryTypeId=3 
AND p.Score>=-7 
AND u.Reputation>=1 
AND u.UpVotes>=0 
AND u.UpVotes<=117;