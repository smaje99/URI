/*
 * Beecrowd exercise 2621.
 * Amounts Between 10 and 20.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2621
 */

select
  pt.name
from
  products pt
  inner join providers pr on pt.id_providers = pr.id
where
  pt.amount between 10 and 20
  and pr.name like 'P%';
