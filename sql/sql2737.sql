/*
 * Beecrowd exercise 2737.
 * Lawyers.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2737
 */

select name, customers_number
from lawyers
where customers_number = (select max(customers_number) from lawyers)
union all
select name, customers_number
from lawyers
where customers_number = (select min(customers_number) from lawyers)
union all
select 'Average' as name, round(avg(customers_number), 0) as customers_number
from lawyers;
