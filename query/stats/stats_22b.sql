SELECT COUNT(*) 
FROM comments as c,
 postHistory as ph,
 votes as v,
 users as u 
WHERE u.Id = v.UserId 
AND v.UserId = ph.UserId 
AND ph.UserId =c.UserId 
AND v.BountyAmount>=0 
AND v.CreationDate>='2010-07-26 00:00:00'::timestamp 
AND v.CreationDate<='2014-09-08 00:00:00'::timestamp 
AND u.Reputation>=1 
AND u.Views>=0 
AND u.Views<=110 
AND u.UpVotes=0 
AND u.CreationDate>='2010-07-28 19:29:11'::timestamp 
AND u.CreationDate<='2014-08-14 05:29:30'::timestamp;