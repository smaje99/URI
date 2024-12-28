/*
 * Beecrowd exercise 2617.
 * Provider Ajax SA.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2617
 */

select
  pt.name,
  pr.name
from
  products pt
  inner join providers pr on pr.id = pt.id_providers
where
  pr.name like 'Ajax SA';
