/*
 * Beecrowd exercise 2606.
 * Categories.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2606
 */

select
  p.id,
  p.name
from
  products p
inner join
  categories c
  on p.id_categories = c.id
where
  lower(c.name) like 'super%'
