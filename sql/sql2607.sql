/*
 * Beecrowd exercise 2607.
 * Providers' City in Alphabetical Order.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2607
 */

select distinct
  providers.city
from
  providers
order by
  providers.city;
