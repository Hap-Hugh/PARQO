SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 users as u 
WHERE c.UserId = u.Id 
AND ph.UserId = u.Id 
AND c.CreationDate>='2010-08-09 07:24:50'::timestamp 
AND c.CreationDate<='2014-09-10 03:46:02'::timestamp 
AND u.Reputation>=1 
AND u.Views<=80 
AND u.UpVotes>=0 
AND u.CreationDate>='2010-08-02 20:31:12'::timestamp;