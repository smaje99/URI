/*
 * Beecrowd exercise 2605.
 * Executive Representative.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2605
 */

select
  products.name,
  providers.name
from
  products
inner join
  providers
  on products.id_providers = providers.id
where
  products.id_categories = 6;
