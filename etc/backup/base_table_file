create database hanul_site;
use hanul_site;
show tables;

drop table if exists department;
create table department (
    department_id int auto_increment primary key,
    department varchar(50)
);

drop table if exists position;
create table position (
    position_id int auto_increment primary key,
    position varchar(20)
);

drop table if exists location;
create table location (
    location_id int auto_increment primary key,
    location_name varchar(20),
    department_id int,
    foreign key (department_id) references department(department_id)
);

drop table if exists sensor;
create table sensor (
    sensor_id int auto_increment primary key,
    sensor_name varchar(20),
    sensor_type varchar(20),
    unit varchar(20),
    location_id int,
    foreign key (location_id) references location(location_id)
);

drop table if exists measurement;
create table measurement (
    measurement_datetime datetime,
    measurement decimal(10,2),
    sensor_id int,
    foreign key (sensor_id) references sensor(sensor_id)
);

drop table if exists employee;
create table employee (
    employee_id int auto_increment primary key,
    name varchar(20),
    last_name varchar(20),
    gender enum('male', 'female'),
    email varchar(40),
    address varchar(60),
    phone_number varchar(11),
    position_id int,
    department_id int,
    foreign key (position_id) references `position`(position_id),
    foreign key (department_id) references department(department_id)
);

show tables;
desc department;
desc position;
desc location;
desc sensor;
desc measurement;
desc employee;