SELECT COUNT(*) 
FROM postHistory as ph,
 votes as v,
 users as u,
 badges as b 
WHERE u.Id = b.UserId 
AND u.Id = ph.UserId 
AND u.Id = v.UserId 
AND u.Views>=0;