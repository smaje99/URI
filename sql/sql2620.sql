/*
 * Beecrowd exercise 2620.
 * Orders in First Half.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2620
 */

select
  c.name as name,
  o.id as order
from
  customers c
  inner join orders o on o.id_customers = c.id
where
  o.orders_date between '2016-01-01' and '2016-06-30';
