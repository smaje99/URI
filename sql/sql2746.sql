/*
 * Beecrowd exercise 2746.
 * Viruses.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2746
 */

select
  replace(v.name, 'H1', 'X') as "name"
from
  virus v;
