SELECT COUNT(*) 
FROM tags as t,
 posts as p,
 users as u,
 votes as v,
 badges as b 
WHERE p.Id = t.ExcerptPostId 
AND u.Id = v.UserId 
AND u.Id = b.UserId 
AND u.Id = p.OwnerUserId 
AND u.Views>=0 
AND u.Views<=515 
AND u.UpVotes>=0 
AND u.CreationDate<='2014-09-07 13:46:41'::timestamp 
AND v.BountyAmount>=0 
AND v.BountyAmount<=200 
AND b.Date<='2014-09-12 12:56:22'::timestamp;