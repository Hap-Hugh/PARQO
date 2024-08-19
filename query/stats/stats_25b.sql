SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 badges as b,
 users as u 
WHERE u.Id = c.UserId 
AND u.Id = ph.UserId 
AND u.Id = b.UserId 
AND c.Score=0 
AND c.CreationDate>='2010-07-20 10:52:57'::timestamp 
AND ph.PostHistoryTypeId=5 
AND ph.CreationDate>='2011-01-31 15:35:37'::timestamp 
AND u.Reputation>=1 
AND u.Reputation<=356 
AND u.DownVotes<=34 
AND u.CreationDate>='2010-07-19 21:29:29'::timestamp 
AND u.CreationDate<='2014-08-20 14:31:46'::timestamp;