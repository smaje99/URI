/*
 * Beecrowd exercise 2741.
 * Students Grades.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2741
 */

select
  'Approved: ' || name,
  grade
from
  students
where
  grade >= 7
order by
  grade desc,
  name asc;
