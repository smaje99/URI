/*
 * Beecrowd exercise 2616.
 * No Rental.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2616
 */

select
  c.id as id,
  c.name as name
from
  customers c
where
  c.id not in (
    select
      l.id_customers
    from
      locations l
  );
