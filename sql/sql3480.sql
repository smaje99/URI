/*
 * Beecrowd exercise 3480.
 * Sillas Adyacentes.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/3480
 */

--- Query psql > 9.4
select
  c.queue,
  c.id as left,
  lead(c.id) over (partition by c.queue order by c.id) as right
from
  chairs c
where
  c.available = true
  and lead(available) over (partition by c.queue order by c.id) = true
order by
  left;

-- Query psql <= 9.4
select
  sub.queue as "queue",
  sub.id as "left",
  sub.next_id as "right"
from (
  select
    c.queue,
    c.id,
    c.available,
    lead(c.id) over (partition by c.queue order by c.id) as next_id,
    lead(c.available) over (partition by c.queue order by c.id) as next_available
  from
    chairs c
) as sub
where
  sub.available = true and sub.next_available = true
order by
  "left";
