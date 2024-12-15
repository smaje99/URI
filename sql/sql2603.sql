/*
 * Beecrowd exercise 2603.
 * Customer Addresses.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2603
 */

select
  name,
  street
from
  customers
where
  city = 'Porto Alegre'
