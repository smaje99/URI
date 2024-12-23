/*
 * Beecrowd exercise 2609.
 * Product by Categories.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2609
 */

select
  c.name as name,
  sum(p.amount) as sum
from
  categories c
join
  products p on c.id = p.id_categories
group by
  c.name;
