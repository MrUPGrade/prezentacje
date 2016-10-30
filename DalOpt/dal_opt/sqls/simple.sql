SELECT *
FROM users
WHERE id = 1;

SELECT *
FROM users
WHERE id = 1 OR id = 2;

SELECT *
FROM emails
WHERE user_id = 1;

SELECT *
FROM users
  LEFT JOIN emails ON users.id = emails.user_id
WHERE user_id = 3;