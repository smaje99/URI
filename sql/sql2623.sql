/*
 * Beecrowd exercise 2623.
 * Categories with Various Products.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2623
 */

select
  p.name,
  c.name
from
  products p
  inner join categories c on p.id_categories = c.id
where
  p.amount > 100
  and p.id_categories in (1, 2, 3, 6, 9);
