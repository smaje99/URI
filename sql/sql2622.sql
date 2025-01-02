/*
 * Beecrowd exercise 2622.
 * Legal Person.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2622
 */

select
  c.name
from
  customers c
  inner join legal_person lp on lp.id_customers = c.id;
