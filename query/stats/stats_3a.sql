SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph 
WHERE c.UserId = ph.UserId 
AND c.Score=0 
AND ph.PostHistoryTypeId=1;