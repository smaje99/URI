/*
 * Beecrowd exercise 2624.
 * Number of Cities per Customers.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2624
 */

select
  count(distinct city) as number_of_cities
from
  customers;
