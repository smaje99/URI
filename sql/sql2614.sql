/*
 * Beecrowd exercise 2614.
 * September Rentals.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2614
 */

select
  c.name as name,
  r.rentals_date as rentals_date
from
  customers c
join
  rentals r on r.id_customers = c.id
where
  extract(month from r.rentals_date) = 9 and
  extract(year from r.rentals_date) = 2016;
