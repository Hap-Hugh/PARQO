SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 votes as v,
 users as u 
WHERE u.Id = v.UserId 
AND v.UserId = ph.UserId 
AND ph.UserId =c.UserId 
AND c.CreationDate>='2010-08-12 20:33:46'::timestamp 
AND c.CreationDate<='2014-09-13 19:26:55'::timestamp 
AND ph.CreationDate>='2011-04-11 14:46:09'::timestamp 
AND ph.CreationDate<='2014-08-17 16:37:23'::timestamp 
AND v.CreationDate>='2010-07-26 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-12 00:00:00'::timestamp 
AND u.Views>=0 
AND u.Views<=783 
AND u.DownVotes>=0 
AND u.DownVotes<=1 
AND u.UpVotes<=123;