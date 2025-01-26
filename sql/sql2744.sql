/*
 * Beecrowd exercise 2744.
 * Password.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2744
 */

select
  a.id as id,
  a.password as "password",
  MD5(a.password) as "MD5"
from
  account a;
