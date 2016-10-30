SELECT count(*)
FROM good_users;

SELECT count(*)
FROM bad_users;


SELECT
  relname                                                                 AS "Table",
  pg_size_pretty(pg_relation_size(relid))                                 AS "Table only size",
  pg_size_pretty(pg_indexes_size(relid))                                  AS "Index",
  pg_size_pretty(pg_total_relation_size(relid))                           AS "Size",
  pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) AS "External Size"
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid ) DESC;