/*
 * Beecrowd exercise 2603.
 * Under 10 or Greater Than 100.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2603
 */

SELECT
  id,
  name
from
  products
where
  price < 10 or price > 100
