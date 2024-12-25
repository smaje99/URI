/*
 * Beecrowd exercise 2611.
 * Action movies.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2611
 */

select
  m.id as id,
  m.name as name
from
  movies m
join
  genres g on m.id_genres = g.id
where
  g.description = 'Action';
