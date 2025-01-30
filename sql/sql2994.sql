/*
 * Beecrowd exercise 2994.
 * How much does a Doctor earn?.
 * Data selection
 * https://www.urionlinejudge.com.br/judge/problems/view/2994
 */

select
  d.name as "name",
  round(sum((a.hours * 150) * (1 + ws.bonus /100.0)), 1) as "salary"
from
  attendances a
  inner join doctors d on a.id_doctor = d.id
  inner join work_shift ws on a.id_work_shift = ws.id
group by
  d.id,
  d.name
order by
  salary desc,
  name asc;

--- Schemas and data
CREATE TABLE doctors (
id integer PRIMARY KEY,
name varchar(50)
);

GRANT SELECT ON doctors TO sql_user;

CREATE TABLE work_shifts (
id integer PRIMARY KEY,
name varchar(50),
bonus numeric
);

GRANT SELECT ON work_shifts TO sql_user;

CREATE TABLE attendances (
id integer PRIMARY KEY,
id_doctor integer,
hours integer,
id_work_shift integer,
FOREIGN KEY (id_doctor) REFERENCES  doctors(id),
FOREIGN KEY (id_work_shift) REFERENCES  work_shifts(id)
);

GRANT SELECT ON attendances TO sql_user;

insert into doctors (id,name) values
(1,'Arlino'),
(2,'Tiago'),
(3,'Amanda'),
(4,'Wellington');

insert into work_shifts (id,name,bonus) values
(1,'nocturnal',15),
(2,'afternoon',2),
(3,'day',1);

insert into  attendances (id, id_doctor, hours, id_work_shift) values
(1,1,5,1),
(2,3,2,1),
(3,3,3,2),
(4,2,2,3),
(5,1,5,3),
(6,4,1,3),
(7,4,2,1),
(8,3,2,2),
(9,2,4,2);

/*  Execute this query to drop the tables */
-- DROP TABLE attendances;
-- DROP TABLE work_shifts;
-- DROP TABLE doctors;
