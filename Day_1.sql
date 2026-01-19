-- create database college;
-- use college;

-- create table day_1_lab_1(
select sysdate();
select now();
select current_date();
select year(current_date());
select month(current_date());
select date(current_date());
select day(current_date());
select monthname(current_date());
select dayname(current_date());
select datediff('2025-10-05',current_date());
select date_add('2025-05-25',interval 10 day);
select date_sub('2025-05-25',interval 3 month);
select last_day('2024-2-25');
select str_to_date('20-12-2013','%d-%m-%y');
select date_format('2025-05-25','%d-%m-%y');
select concat('Hello ','World');
select concat_ws('+','Hello','World','This','is','Sahith');
select length(current_date());

select upper('hello');

select lower('HELlo');

