/*
 * Beecrowd exercise 2608.
 * Higher and Lower Price.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2608
 */

select
  max(products.price) as higher_price,
  min(products.price) as lower_price
from
  products;
