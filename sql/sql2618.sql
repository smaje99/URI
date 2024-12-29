/*
 * Beecrowd exercise 2618.
 * Imported Products.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2618
 */

select
  products.name,
  providers.name,
  categories.name
from
  products
  join providers on products.id_providers = providers.id
  join categories on products.id_categories = categories.id
where
  providers.name like 'Sansul SA'
  and categories.name like 'Imported';
