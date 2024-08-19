SELECT COUNT(*) 
FROM votes as v,
 badges as b,
 users as u 
WHERE u.Id = v.UserId 
AND v.UserId = b.UserId 
AND u.DownVotes>=0 
AND u.DownVotes<=0;