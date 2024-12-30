/*
 * Beecrowd exercise 2619.
 * Super Luxury.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2619
 */

select
  pt.name,
  pr.name,
  pt.price
from
  products pt
  inner join providers pr on pt.id_providers = pr.id
  inner join categories ct on pt.id_categories = ct.id
where
  ct.name = 'Super Luxury'
  and pt.price > 1000;
