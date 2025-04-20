/*
 * Beecrowd exercise 3481.
 * Clasificación de un Árbol.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/3481
 */
--- Query
(
  select distinct
    n1.node_id,
    'ROOT' as "type"
  from
    nodes n1
    left join nodes n2 on n2.pointer = n1.node_id
  where
    n2.node_id is null
)
union all
(
  select distinct
    n1.node_id,
    'INNER' as "type"
  from
    nodes n1
    inner join nodes n2 on n1.node_id = n2.pointer
  where
    n1.pointer is not null
)
union all
(
  select distinct
    n1.node_id,
    'LEAF' as "type"
  from
    nodes n1
  where
    n1.pointer is null
)
order by
  node_id asc;
