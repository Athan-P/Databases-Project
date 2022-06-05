

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------

-- -----------------------------------------------------
DROP SCHEMA IF EXISTS mydb ;

-- -----------------------------------------------------

-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8mb4 ;
SHOW WARNINGS;
USE mydb ;

-- -----------------------------------------------------
-- 
-- -----------------------------------------------------
#DROP TABLE IF EXISTS org ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS org (
  idorg INT UNSIGNED NOT NULL AUTO_INCREMENT,
  City VARCHAR(20) NOT NULL,
  Street_name VARCHAR(30) NOT NULL,
  Postal_code INT(5) NOT NULL,
  typec ENUM('Uni', 'Comp', 'RF') NOT NULL,
  Research_facility_Budget_MoE FLOAT(10,2) NOT NULL DEFAULT 0.0,
  Research_facility_Budget_private_sector FLOAT(10,2) NOT NULL DEFAULT 0.0,
  Company_Budget  FLOAT(10,2) NOT NULL DEFAULT 0.0,
  University_Budget_MoE FLOAT(10,2) NOT NULL DEFAULT 0.0,
  Orgname VARCHAR(60) NOT NULL,
  Abbreviation VARCHAR(7) NOT NULL,
  PRIMARY KEY (idorg),
  CHECK (Research_facility_Budget_MoE>=0.0),
  CHECK(Research_facility_Budget_private_sector>=0.0), 
  CHECK(Company_Budget>=0.0),
  CHECK(University_Budget_MoE>=0.0 )
  )
ENGINE = InnoDB;
DELIMITER ;;
CREATE TRIGGER ins_org BEFORE INSERT ON org FOR EACH ROW BEGIN
    IF (new.typec = 'Uni') 
    THEN
    	#UPDATE org
    		SET new.Research_facility_Budget_MoE = 0.0,new.Company_Budget= 0.0,new.Research_facility_Budget_private_sector=0.0;
    		
		#WHERE idorg = new.idorg;
     END IF;
     IF (new.typec = 'Comp') 
    THEN
    	#UPDATE org
    		SET new.Research_facility_Budget_MoE = 0.0,new.Research_facility_Budget_private_sector= 0.0,new.University_Budget_MoE= 0.0;
    		
	#WHERE idorg = new.idorg;
     END IF;
     IF (new.typec = 'RF') 
    THEN
    	#UPDATE org
    		SET  new.Company_Budget= 0.0,new.University_Budget_MoE= 0.0
    		
    	;#WHERE idorg = new.idorg;
     END IF;
  END;;

DELIMITER ;


#DROP TABLE IF EXISTS researcher ;

CREATE TABLE IF NOT EXISTS researcher (
  idresearcher INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Researcher_name VARCHAR(30) NOT NULL,
  Researcher_surname VARCHAR(45) NOT NULL,
  Researcher_gender ENUM('M','F','NB') NOT NULL,
  researcher_date_of_birth DATE NOT NULL,
  researcher_hire_date DATE NOT NULL,
  org_idorg INT UNSIGNED NOT NULL,
  PRIMARY KEY (idresearcher),
  CONSTRAINT fk_researcher_org1
    FOREIGN KEY (org_idorg)
    REFERENCES org (idorg)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
     CONSTRAINT research_dates
  CHECK (researcher_date_of_birth<researcher_hire_date AND researcher_date_of_birth< 20011010))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_researcher_org1_idx ON researcher (org_idorg ASC) ;

SHOW WARNINGS;



-- -----------------------------------------------------
# Table `mydb`.`Executive`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Executive ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Executive (
  idExecutive INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Executive_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (idExecutive))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX idExecutive_UNIQUE ON Executive (idExecutive ASC) ;

SHOW WARNINGS;

-- -----------------------------------------------------
# Table `mydb`.`Program`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Program ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Program (
  idProgram INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Program_name VARCHAR(45) NOT NULL,
  Program_dept VARCHAR(30) NOT NULL,
  PRIMARY KEY (idProgram))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX Program_name_UNIQUE ON Program (Program_name ASC) ;

SHOW WARNINGS;
CREATE UNIQUE INDEX idProgram_UNIQUE ON Program (idProgram ASC) ;

SHOW WARNINGS;

-- -----------------------------------------------------

-- -----------------------------------------------------
#DROP TABLE IF EXISTS Project ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Project (
  idProject INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Project_title VARCHAR(45) NOT NULL,
  Project_summary MEDIUMTEXT NOT NULL,
  Project_starting DATE NOT NULL,
  Project_ending DATE NOT NULL,
  Project_budget FLOAT(20,2) NOT NULL,
  org_idorg INT UNSIGNED NOT NULL,
  researcher_idresearcher INT UNSIGNED NOT NULL,
  Executive_idExecutive INT UNSIGNED NOT NULL,
  Program_idProgram INT UNSIGNED NOT NULL,
  researcher_ideval INT UNSIGNED NOT NULL,
  EvalGrade INT UNSIGNED NOT NULL,
  EvalDate DATE NOT NULL,
  PRIMARY KEY (idProject),
  CONSTRAINT fk_Project_org1
    FOREIGN KEY (org_idorg)
    REFERENCES org (idorg)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_Project_researcher1
    FOREIGN KEY (researcher_idresearcher)
    REFERENCES researcher (idresearcher)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_Project_Executive1
    FOREIGN KEY (Executive_idExecutive)
    REFERENCES Executive (idExecutive)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_Project_Program1
    FOREIGN KEY (Program_idProgram)
    REFERENCES Program (idProgram)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
    CONSTRAINT fk_Project_researcheval
    FOREIGN KEY (researcher_ideval)
    REFERENCES researcher (idresearcher)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
	CONSTRAINT project_dates
  CHECK (Project_starting<Project_ending ),
   CONSTRAINT durmax
  CHECK (datediff(Project_ending,Project_starting) < 1460),
  CONSTRAINT durmin
  CHECK (datediff(Project_ending , Project_starting) > 365),
   CONSTRAINT evalpass
  CHECK (EvalGrade>=50),
  CHECK (EvalGrade<=100 ),
   CONSTRAINT evaldatebefore
  CHECK (EvalDate<=Project_starting),
  CONSTRAINT projbudg
  CHECK (Project_budget>0.0)
 )
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_Project_org1_idx ON Project (org_idorg ASC) ;

SHOW WARNINGS;
CREATE INDEX fk_Project_researcher1_idx ON Project (researcher_idresearcher ASC) ;

SHOW WARNINGS;
CREATE INDEX fk_Project_Executive1_idx ON Project (Executive_idExecutive ASC) ;

SHOW WARNINGS;
CREATE INDEX fk_Project_Program1_idx ON Project (Program_idProgram ASC) ;

SHOW WARNINGS;
CREATE UNIQUE INDEX idProject_UNIQUE ON Project (idProject ASC) ;
SHOW WARNINGS;
CREATE INDEX fk_Project_researchereval_idx ON Project (researcher_ideval ASC) ;
SHOW WARNINGS;

DELIMITER ;;

CREATE TRIGGER ins_proj_resdates before insert on Project for each row 
 BEGIN 
 IF (new.org_idorg != 
(SELECT r.org_idorg
    FROM researcher r
    WHERE r.idresearcher= new.researcher_idresearcher))
     THEN SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
     END IF;
    
 IF (new.org_idorg  = 
(SELECT r.org_idorg
    FROM researcher r
    WHERE r.idresearcher= new.researcher_ideval))
     THEN SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
     END IF;
    

END;;

DELIMITER ;



DELIMITER ;;
CREATE TRIGGER ins_proj BEFORE INSERT ON Project FOR EACH ROW BEGIN
    IF (new.Project_ending<date_add(new.Project_starting,INTERVAL 1 year)) or (new.Project_ending>date_add(new.Project_starting,INTERVAL 1 year)) 
    THEN
        SET new.Project_ending= date_add(new.Project_starting,INTERVAL 3 year);
	END IF;
  END;;
CREATE TRIGGER upd_proj AFTER UPDATE ON Project FOR EACH ROW BEGIN
    IF (old.researcher_idresearcher != new.researcher_idresearcher) 
    THEN
        UPDATE works
            SET researcher_idresearcher = new.researcher_idresearcher
        WHERE researcher_idresearcher = old.researcher_idresearcher;
    END IF;
  END;;

DELIMITER ;
-- -----------------------------------------------------
# Table `mydb`.`Scientific_domain`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Scientific_domain ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Scientific_domain (
  Scientific_domain_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (Scientific_domain_name))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX Scientific_domain_name_UNIQUE ON Scientific_domain (Scientific_domain_name ASC) ;

SHOW WARNINGS;

-- -----------------------------------------------------
# Table `mydb`.`Evaluation`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Evaluation ;

SHOW WARNINGS;

SHOW WARNINGS;

-- -----------------------------------------------------
# Table `mydb`.`Deliverable`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Deliverable ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Deliverable (
  idDeliverable INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Deliverable_title VARCHAR(45) NOT NULL,
  Deliverable_summary MEDIUMTEXT NOT NULL,
  Deliverable_date DATE NOT NULL,
  Project_idProject INT UNSIGNED NOT NULL,
  PRIMARY KEY (idDeliverable, Project_idProject),
  CONSTRAINT `fk_Deliverable_Project1`
    FOREIGN KEY (Project_idProject)
    REFERENCES Project (idProject)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_Deliverable_Project1_idx ON Deliverable (Project_idProject ASC) ;

SHOW WARNINGS;
CREATE UNIQUE INDEX idDeliverable_UNIQUE ON Deliverable (idDeliverable ASC) ;

SHOW WARNINGS;






DELIMITER $$
CREATE trigger ins_deliv after insert on Deliverable for each row
BEGIN
	IF new.Deliverable_date<
  (
    SELECT p.Project_starting
    FROM Project p
    WHERE p.idProject=new.Project_idProject
) 
THEN 
SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
END IF;
IF new.Deliverable_date>
  (
    SELECT p.Project_ending
    FROM Project p
    WHERE p.idProject=new.Project_idProject
) 
THEN 
SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
END IF;


 END $$

DELIMITER ;

-- -----------------------------------------------------
# Table `mydb`.`Phone`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS Phone ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Phone (
  Phone_number  BIGINT(10) NOT NULL,
  org_idorg INT UNSIGNED NOT NULL,
  PRIMARY KEY (Phone_number, org_idorg),
  CONSTRAINT fk_Phone_org1
    FOREIGN KEY (org_idorg)
    REFERENCES org (idorg)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_Phone_org1_idx ON Phone (org_idorg ASC) ;

SHOW WARNINGS;
CREATE UNIQUE INDEX Phone_number_UNIQUE ON Phone (Phone_number ASC) ;

SHOW WARNINGS;

-- -----------------------------------------------------
# Table `mydb`.`works`
-- -----------------------------------------------------
#DROP TABLE IF EXISTS works ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS works (
  Project_idProject INT UNSIGNED NOT NULL,
  researcher_idresearcher INT UNSIGNED NOT NULL,
  PRIMARY KEY (Project_idProject, researcher_idresearcher),
  CONSTRAINT fk_works_Project1
    FOREIGN KEY (Project_idProject)
    REFERENCES Project (idProject)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_works_researcher1
    FOREIGN KEY (researcher_idresearcher)
    REFERENCES researcher (idresearcher)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_works_Project1_idx ON works (Project_idProject ASC) ;

SHOW WARNINGS;
CREATE INDEX fk_works_researcher1_idx ON works (researcher_idresearcher ASC) ;

SHOW WARNINGS;

drop view if exists proj_res;
CREATE VIEW proj_res AS
(SELECT 
r.idresearcher,

CONCAT(r.researcher_name," ", r.researcher_surname) as Full_name,
p.idProject,
p.Project_title
FROM researcher r
INNER JOIN works w ON r.idresearcher = w.researcher_idresearcher
INNER JOIN Project p ON p.idProject = w.Project_idProject )
union 
(SELECT DISTINCT
r.idresearcher,

CONCAT(r.researcher_name," ", r.researcher_surname) as Full_name,
p.idProject,
p.Project_title
FROM Project p
inner join researcher r on p.researcher_idresearcher=r.idresearcher
) order by idresearcher;

drop view if exists res_org;
CREATE VIEW res_org AS
SELECT 
r.idresearcher,
CONCAT(r.researcher_name," ", r.researcher_surname) as Full_name,
o.idorg,
o.Orgname,
o.Abbreviation
FROM researcher r
INNER JOIN org o ON r.org_idorg = o.idorg;


DELIMITER $$

CREATE trigger ins_work_res after insert on works for each row begin
	IF
    (SELECT p.org_idorg 
    FROM Project p
    WHERE p.idProject=new.Project_idProject)
    !=
    (Select r.org_idorg from researcher r where r.idresearcher=new.researcher_idresearcher)
    then SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
    END IF;
    
    
    IF
    (SELECT p.project_ending 
    FROM Project p
    WHERE p.idProject=new.Project_idProject)
    <
    (Select r.researcher_hire_date from researcher r where r.idresearcher=new.researcher_idresearcher)
    then SIGNAL sqlstate '45001' set message_text = "No way ! You cannot do this !";
    END IF;
    
 END $$

DELIMITER ;


-- -----------------------------------------------------

-- -----------------------------------------------------
#DROP TABLE IF EXISTS Project_has_Scientific_domain ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS Project_has_Scientific_domain (
  Project_idProject INT UNSIGNED NOT NULL,
  Scientific_domain_Scientific_domain_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (Project_idProject, Scientific_domain_Scientific_domain_name),
  CONSTRAINT fk_Project_has_Scientific_domain_Project1
    FOREIGN KEY (Project_idProject)
    REFERENCES Project (idProject)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_Project_has_Scientific_domain_Scientific_domain1
    FOREIGN KEY (Scientific_domain_Scientific_domain_name)
    REFERENCES Scientific_domain (Scientific_domain_name)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX fk_Project_has_Scientific_domain_Scientific_domain1_idx ON Project_has_Scientific_domain (Scientific_domain_Scientific_domain_name ASC) ;

SHOW WARNINGS;
CREATE INDEX fk_Project_has_Scientific_domain_Project1_idx ON Project_has_Scientific_domain (Project_idProject ASC) ;

SHOW WARNINGS;

#ALTER TABLE Project ADD CONSTRAINT resypeythmultorg CHECK ( resorgyp(researcher_idresearcher)!= org_idorg);
SHOW WARNINGS;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
