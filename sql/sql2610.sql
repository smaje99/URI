/*
 * Beecrowd exercise 2610.
 * Average Value of Products.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2610
 */

select
  round(avg(p.price), 2) as price
from
  products p;
