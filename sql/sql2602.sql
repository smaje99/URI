/*
 * Beecrowd exercise 2602.
 * Basic select.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2602
 */

select
  name
from
  customers
where
  upper(state) = 'RS'
