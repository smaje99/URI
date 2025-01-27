/*
 * Beecrowd exercise 2745.
 * Taxes.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2745
 */

select
  p.name as "name",
  round(p.salary * 0.1, 2) as "tax"
from
  people p
where
  p.salary > 3000;
