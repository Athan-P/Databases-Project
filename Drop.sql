DROP SCHEMA IF EXISTS mydb ;

DROP TABLE IF EXISTS org;
DROP TABLE IF EXISTS researcher;
DROP TABLE IF EXISTS Executive;
DROP TABLE IF EXISTS Program;
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Scientific_domain;
DROP TABLE IF EXISTS Deliverable;
DROP TABLE IF EXISTS Phone;
DROP TABLE IF EXISTS works;
DROP TABLE IF EXISTS Project_has_Scientific_domain;

DROP VIEW IF EXISTS proj_res;
DROP VIEW IF EXISTS res_org;