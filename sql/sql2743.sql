/*
 * Beecrowd exercise 2743.
 * Number of Characters.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2743
 */

select
  name,
  length(name) as length
from
  people
order by
  length desc;
