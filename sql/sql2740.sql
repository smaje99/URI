/*
 * Beecrowd exercise 2740.
 * League.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2740
 */

with podium as (
  select concat('Podium: ', team) as name
  from league where position <= 3
),
demoted as (
  select concat('Demoted: ', team) as name
  from league where position >= 14
)
select name from podium
union all
select name from demoted;
