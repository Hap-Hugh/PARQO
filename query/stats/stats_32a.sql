SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 votes as v,
 users as u 
WHERE u.Id =b.UserId 
AND b.UserId = ph.UserId 
AND ph.UserId = v.UserId 
AND v.UserId = c.UserId 
AND c.CreationDate>='2010-07-20 21:37:31'::timestamp 
AND ph.PostHistoryTypeId=12 
AND u.UpVotes=0;