/*
 * Beecrowd exercise 2739.
 * Payday.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2739
 */

select
  l.name as name,
  (extract(day from l.payday))::integer as day
from
  loan l;
