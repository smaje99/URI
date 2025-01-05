/*
 * Beecrowd exercise 2625.
 * CPF Validation.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2625
 */

select
  format(
    '%s.%s.%s-%s',
    left(cpf, 3),
    substring(cpf from 4 for 3),
    substring(cpf from 7 for 3),
    right(cpf, 2)
  ) as cpf
from
  natural_person;
