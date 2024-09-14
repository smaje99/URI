/*
 * Beecrowd exercise 2613.
 * Cheap movies.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2613
 */

select
  m.id as id,
  m.name as name
from
  movies m
join
  prices p on p.id = m.id_prices
where
  p.value < 2.00;
