SELECT COUNT(*) 
FROM badges as b,
 users as u 
WHERE b.UserId= u.Id 
AND u.UpVotes>=0;