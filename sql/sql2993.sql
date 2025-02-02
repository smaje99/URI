/*
 * Beecrowd exercise 2993.
 * Most Frequent.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2993
 */

--- Query 1 - Time: 0.005s - Complexity: O(n + m log m) - Space: O(m)
select
  amount as "most_frequent_value"
from
  value_table
group by
  amount
order by
  count(*) desc
limit 1;

--- Query 2 - Time: 0.003s - Complexity: O(n) - Space: O(m)
select
  mode() within group (order by amount) as "most_frequent_value"
from
  value_table;

--- Schemas and data
CREATE TABLE
  value_table (amount integer);

GRANT
SELECT
  ON value_table TO sql_user;

insert into
  value_table (amount)
values
  (4),
  (6),
  (7),
  (1),
  (1),
  (2),
  (3),
  (2),
  (3),
  (1),
  (5),
  (6),
  (1),
  (7),
  (8),
  (9),
  (10),
  (11),
  (12),
  (4),
  (5),
  (5),
  (3),
  (6),
  (2),
  (2),
  (1);

/*  Execute this query to drop the tables */
-- DROP TABLE value_table;