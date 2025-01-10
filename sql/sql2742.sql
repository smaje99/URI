/*
 * Beecrowd exercise 2742.
 * Richard's Multiverse.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2742
 */

select
  l.name as name,
  round(l.omega * 1.618, 3) as "The N Factor"
from
  life_registry l
  inner join dimensions d on l.dimensions_id = d.id
where
  d.name in ('C774', 'C875')
  and l.name like 'Richard%'
order by
  l.omega asc;