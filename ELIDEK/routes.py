from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from ELIDEK import app, db ## initially created by __init__.py, need to be used here
from ELIDEK.forms import ProjectCreate, ResearcherCreate, OrganisationCreate, ExecutiveCreate, ProgramCreate, Scientific_DomainCreate, DeliverableCreate, ProjectUpdate, ResearcherUpdate, OrganisationUpdate, ExecutiveUpdate, ProgramUpdate, Scientific_DomainUpdate, DeliverableUpdate, ProjectFilter, PhoneCreate, WorksCreate, ProjectHasDomainCreate, PhoneUpdate, WorksUpdate, ProjectHasDomainUpdate, ProjResCreate, ResOrgCreate, Get33, Get34, Get35, Get36, Get37, Get38

@app.route("/")
def index():
    try:
        ## create connection to database
        cur = db.connection.cursor()
        ## execute query
        
        return render_template("index.html",
                               pageTitle = "ELIDEK")
    except Exception as e:
        print(e)
        return render_template("index.html", pageTitle = "ELIDEK")


#3.1============================================================================



@app.route("/Projects/Project_Filters", methods = ["GET", "POST"]) ## "GET" by default
def getProjectFilters( Project_starting = None, Project_ending = None, Executive_idExecutive = None):
	#Project_starting = 0, Project_ending = 0,
	
	form = ProjectFilter()
	if(request.method == "POST"):
		new = form.__dict__
		Project_starting = new['Project_starting'].data
		Project_ending =  new['Project_ending'].data
		Executive_idExecutive = new['Executive_idExecutive'].data
		if Executive_idExecutive != None:
			if(Project_ending != None):
				if(Project_starting != None):
					query = "SELECT * FROM project WHERE Project_starting >= '{}' AND Project_ending <= '{}' AND Executive_idExecutive = '{}';".format(Project_starting, Project_ending, Executive_idExecutive)
				else:
					query = "SELECT * FROM project WHERE Project_ending <= '{}' AND Executive_idExecutive = '{}';".format(Project_ending,Executive_idExecutive)
			else:
				if(Project_starting != None):
					query = "SELECT * FROM project WHERE Project_starting >= '{}' AND Executive_idExecutive = '{}';".format(Project_starting, Executive_idExecutive)
				else:
					query = "SELECT * FROM project WHERE Executive_idExecutive = '{}';".format(Executive_idExecutive)
		else:
			if(Project_ending != None):
				if(Project_starting != None):
					query = "SELECT * FROM project WHERE Project_starting >= '{}' AND Project_ending <= '{}';".format(Project_starting, Project_ending)
				else:
					query = "SELECT * FROM project WHERE Project_ending <= '{}';".format(Project_ending)
			else:
				if(Project_starting != 0):
					query = "SELECT * FROM project WHERE Project_starting >= '{}';".format(Project_starting)
				else:
					query = "SELECT * FROM project;"
		try:
			
			cur = db.connection.cursor()
			cur.execute(query)
			column_names = [i[0] for i in cur.description]
			Projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
			cur.close()
			return render_template("Project_Filters_Show.html", Projects = Projects, pageTitle = "Projects Filter Show Page", form = form)
		except Exception as e: ## OperationalError
			flash(str(e), "danger")
	
	
	return render_template("Project_Filters.html", pageTitle = "Projects Filter Page", form = form)





#3.2VIEWS========================================================================

@app.route("/ViewProjRes")
def getViewProjRes():
    """
    #Retrieve ViewProjRes from database
    """
    try:
        form = ProjResCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM proj_res")
        column_names = [i[0] for i in cur.description]
        ProjRes = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Views/ViewProjRes.html", ProjRes = ProjRes, pageTitle = "View from Researchers by projects Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/ViewResOrg")
def getViewResOrg():
    """
    #Retrieve ViewResOrg from database
    """
    try:
        form = ResOrgCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM res_org")
        column_names = [i[0] for i in cur.description]
        ResOrgs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Views/ViewResOrg.html", ResOrgs = ResOrgs, pageTitle = "View from Researchers by organisations Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


#3.3=============================================================================

@app.route("/Get33" , methods = ["GET", "POST"])
def get33(Scientific_domain_Scientific_domain_name = 'Law'):
    """
    #Retrieve 3.3 from database
    """
    form = Get33()
    if(request.method == "POST"):
        new = form.__dict__
        Scientific_domain_Scientific_domain_name = new['Scientific_domain_Scientific_domain_name'].data
        try:
            cur = db.connection.cursor()
            cur.execute("select  s.Scientific_domain_Scientific_domain_name,p.idProject,p.Project_starting,p.researcher_idresearcher,p.Project_ending,r.idresearcher,r.Researcher_name,r.Researcher_surname from Project_has_Scientific_domain s inner join Project p on s.Project_idProject=p.idProject inner join works w on w.Project_idProject=p.idProject inner join researcher r on r.idresearcher=w.researcher_idresearcher  where s.Scientific_domain_Scientific_domain_name='{}' and p.Project_starting<curdate() and p.Project_ending>curdate() union select s.Scientific_domain_Scientific_domain_name,p.idProject,p.Project_starting,p.researcher_idresearcher,p.Project_ending,r.idresearcher,r.Researcher_name,r.Researcher_surname from Project_has_Scientific_domain s inner join Project p on s.Project_idProject=p.idProject inner join researcher r on r.idresearcher=p.researcher_idresearcher where s.Scientific_domain_Scientific_domain_name='{}' and p.Project_starting<curdate() and p.Project_ending>curdate() order by idProject;".format(Scientific_domain_Scientific_domain_name, Scientific_domain_Scientific_domain_name))
            column_names = [i[0] for i in cur.description]
            Get33s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()
            return render_template("Queries/Get33.html", Get33s = Get33s, pageTitle = "View 3.3 Page", form = form)
        except Exception as e:
            ## if the connection to the database fails, return HTTP response 500
            flash(str(e), "danger")
            abort(500)
    return render_template("ScieDomChoose.html", pageTitle = "Choose Scientific Domain Page", form = form)

#3.4=============================================================================

@app.route("/Get34")
def get34():
    """
    #Retrieve 3.4 from database
    """
    try:
        form = Get34()
        cur = db.connection.cursor()
        cur.execute("SELECT distinct po.idorg,po.cnt FROM ((select   o.idorg, EXTRACT(YEAR FROM p.Project_starting) as pyear,count(distinct idProject) as cnt from org o inner join Project p on o.idorg=p.org_idorg group by idorg,pyear )  po inner join (select   o.idorg, EXTRACT(YEAR FROM p.Project_starting) as pyear,count(distinct idProject) as cnt  from org o inner join Project p on o.idorg=p.org_idorg group by idorg,pyear ) l on l.idorg=po.idorg) where ((po.pyear=l.pyear+1 or po.pyear=l.pyear-1)and po.cnt=l.cnt and po.cnt>=10)  ;")
        column_names = [i[0] for i in cur.description]
        Get34s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Queries/Get34.html", Get34s = Get34s, pageTitle = "View 3.4 Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


#3.5=============================================================================

@app.route("/Get35")
def get35():
    """
    #Retrieve 3.5 from database
    """
    try:
        form = Get35()
        cur = db.connection.cursor()
        cur.execute("select t.Scientific_domain_Scientific_domain_name AS Scientific_domain_Scientific_domain_name1 ,s.Scientific_domain_Scientific_domain_name AS Scientific_domain_Scientific_domain_name2,count(*) AS count from Project_has_Scientific_domain s inner join Project_has_Scientific_domain t on t.Project_idProject=s.Project_idProject where t.Scientific_domain_Scientific_domain_name<s.Scientific_domain_Scientific_domain_name group by t.Scientific_domain_Scientific_domain_name ,s.Scientific_domain_Scientific_domain_name order by count(*) DESC	LIMIT 3;")
        column_names = [i[0] for i in cur.description]
        Get35s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Queries/Get35.html", Get35s = Get35s, pageTitle = "View 3.5 Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



#3.6=============================================================================

@app.route("/Get36")
def get36():
    """
    #Retrieve 3.6 from database
    """
    try:
        form = Get36()
        cur = db.connection.cursor()
        cur.execute("select st.researcher_idresearcher,st.researcher_date_of_birth,count(st.researcher_idresearcher) as cnt  from( select w.researcher_idresearcher,r.researcher_date_of_birth,w.Project_idProject from researcher r inner join works w on w.researcher_idresearcher=r.idresearcher inner join Project p on p.idProject=w.Project_idProject where p.Project_starting<curdate() and p.Project_ending>curdate() and DATEDIFF(curdate(),r.researcher_date_of_birth)<40*365  union select p.researcher_idresearcher,r.researcher_date_of_birth,p.idProject from Project p inner join researcher r on r.idresearcher=p.researcher_idresearcher where p.Project_starting<curdate() and p.Project_ending>curdate() and  DATEDIFF(curdate(),r.researcher_date_of_birth)<40*365) st  group by st.researcher_idresearcher,st.researcher_date_of_birth order by count(st.researcher_idresearcher) DESC LIMIT 5;")
        column_names = [i[0] for i in cur.description]
        Get36s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Queries/Get36.html", Get36s = Get36s, pageTitle = "View 3.6 Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


#3.7=============================================================================

@app.route("/Get37")
def get37():
    """
    #Retrieve 3.7 from database
    """
    try:
        form = Get37()
        cur = db.connection.cursor()
        cur.execute("SELECT sl.Executive_name, sl.Orgname, sum(sl.Project_budget) as sumb FROM (SELECT DISTINCT e.Executive_name, o.Orgname, o.typec, p.Project_budget, e.idExecutive, o.idorg FROM Executive e INNER JOIN Project p ON e.idExecutive = p.Executive_idExecutive INNER JOIN org o ON o.idorg = p.org_idorg)sl WHERE(sl.typec = 'Comp') GROUP BY sl.idExecutive,sl.Orgname  ORDER BY sumb DESC LIMIT 5;")
        column_names = [i[0] for i in cur.description]
        Get37s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Queries/Get37.html", Get37s = Get37s, pageTitle = "View 3.7 Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)


#3.8=============================================================================

@app.route("/Get38")
def get38():
    """
    #Retrieve 3.8 from database
    """
    try:
        form = Get38()
        cur = db.connection.cursor()
        cur.execute("select * from (SELECT CONCAT(l.researcher_name , ' ' , l.researcher_surname) as Full_name, l.idresearcher, count(distinct l.idProject) as cnt FROM ((SELECT r.idresearcher,r.researcher_name,r.researcher_surname,p.idProject from  works w INNER JOIN researcher r ON r.idresearcher = w.researcher_idresearcher INNER JOIN Project p ON p.idProject = w.Project_idProject WHERE p.idProject not in (select d.Project_idProject from Deliverable d)) union (select r.idresearcher,r.researcher_name,r.researcher_surname,p.idProject from Project p inner join researcher r on r.idresearcher=p.researcher_idresearcher  WHERE p.idProject not in (select d.Project_idProject from Deliverable d))) l GROUP BY l.idresearcher,l.researcher_name,l.researcher_surname) m where m.cnt>=5;")
        column_names = [i[0] for i in cur.description]
        Get38s = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Queries/Get38.html", Get38s = Get38s, pageTitle = "View 3.8 Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



#CRUD===========================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================


#Projects=========================================================================


@app.route("/Projects")
def getProjects():
    """
    #Retrieve projects from database
    """
    try:
        form = ProjectCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM project")
        column_names = [i[0] for i in cur.description]
        Projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Projects.html", Projects = Projects, pageTitle = "Projects Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Projects/Create", methods = ["GET", "POST"]) ## "GET" by default
def createProject():
    """
    #Create new Project in the database
    """
    form = ProjectCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        print(1)
        newProject = form.__dict__
        query = "INSERT INTO project(Project_title, Project_summary, Project_starting, Project_ending, Project_budget, org_idorg, researcher_idresearcher, Executive_idExecutive, Program_idProgram, researcher_ideval, EvalGrade, EvalDate) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(newProject['Project_title'].data, newProject['Project_summary'].data, newProject['Project_starting'].data, newProject['Project_ending'].data, newProject['Project_budget'].data, newProject['org_idorg'].data, newProject['researcher_idresearcher'].data, newProject['Executive_idExecutive'].data, newProject['Program_idProgram'].data, newProject['researcher_ideval'].data, newProject['EvalGrade'].data, newProject['EvalDate'].data)
        try:
            print(2)
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Project inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_project.html", pageTitle = "Create Project", form = form)



@app.route("/Projects/update/<int:idProject>", methods = ["POST"])
def updateProject(idProject):
    """
    #Update a Project in the database, by id
    """
    form = ProjectUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE project SET Project_title = '{}', Project_summary = '{}', Project_starting = '{}', Project_ending = '{}', Project_budget = '{}', org_idorg = '{}', researcher_idresearcher = '{}', Executive_idExecutive = '{}', Program_idProgram = '{}', researcher_ideval = '{}', EvalGrade = '{}', EvalDate = '{}' WHERE idProject = '{}';".format(updateData['Project_title'].data, updateData['Project_summary'].data, updateData['Project_starting'].data, updateData['Project_ending'].data, updateData['Project_budget'].data, updateData['org_idorg'].data, updateData['researcher_idresearcher'].data, updateData['Executive_idExecutive'].data, updateData['Program_idProgram'].data, updateData['researcher_ideval'].data, updateData['EvalGrade'].data, updateData['EvalDate'].data,  idProject)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Project updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getProjects"))

@app.route("/Projects/delete/<int:idProject>", methods = ["POST"])
def deleteStudent(idProject):
    """
    #Delete Project by id from database
    """
    query = f"DELETE FROM project WHERE idProject = {idProject};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getProjects"))



#Researchers======================================================================

@app.route("/Researchers")
def getResearchers():
    """
    #Retrieve researdhers from database
    """
    try:
        form = ResearcherCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM Researcher")
        column_names = [i[0] for i in cur.description]
        Researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Researchers.html", Researchers = Researchers, pageTitle = "Researchers Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Researchers/Create", methods = ["GET", "POST"]) ## "GET" by default
def createResearcher():
    """
    #Create new Researcher in the database
    """
    form = ResearcherCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newResearcher = form.__dict__
        query = "INSERT INTO researcher(Researcher_name, Researcher_surname, Researcher_gender, researcher_date_of_birth, researcher_hire_date, org_idorg) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(newResearcher['Researcher_name'].data, newResearcher['Researcher_surname'].data, newResearcher['Researcher_gender'].data, newResearcher['researcher_date_of_birth'].data, newResearcher['researcher_hire_date'].data, newResearcher['org_idorg'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_researcher.html", pageTitle = "Create Researcher", form = form)

@app.route("/Researchers/update/<int:idresearcher>", methods = ["POST"])
def updateResearcher(idresearcher):
    """
    #Update a Researcher in the database, by id
    """
    form = ResearcherUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE researcher SET Researcher_name = '{}', Researcher_surname = '{}', Researcher_gender = '{}', researcher_date_of_birth = '{}', researcher_hire_date = '{}', org_idorg = '{}' WHERE idresearcher = {};".format(updateData['Researcher_name'].data, updateData['Researcher_surname'].data, updateData['Researcher_gender'].data, updateData['researcher_date_of_birth'].data, updateData['researcher_hire_date'].data, updateData['org_idorg'].data,  idresearcher)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getResearchers"))

@app.route("/Researchers/delete/<int:idresearcher>", methods = ["POST"])
def deleteResearcher(idresearcher):
    """
    #Delete Researcher by id from database
    """
    query = f"DELETE FROM researcher WHERE idresearcher = {idresearcher};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getResearchers"))




#Organisations====================================================================

@app.route("/Organisations")
def getOrganisations():
    """
    #Retrieve Organisations from database
    """
    try:
        form = OrganisationCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM org")
        column_names = [i[0] for i in cur.description]
        Organisations = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Organisations.html", Organisations = Organisations, pageTitle = "Organisations Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/Organisations/Create", methods = ["GET", "POST"]) ## "GET" by default
def createOrganisation():
    """
    #Create new Organisation in the database
    """
    form = OrganisationCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newOrganisation = form.__dict__
        query = "INSERT INTO org(Orgname, Abbreviation, City, Street_name, Postal_code, typec, Research_facility_Budget_MoE, Research_facility_Budget_private_sector, Company_Budget, University_Budget_MoE) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(newOrganisation['Orgname'].data, newOrganisation['Abbreviation'].data, newOrganisation['City'].data, newOrganisation['Street_name'].data, newOrganisation['Postal_code'].data, newOrganisation['typec'].data, newOrganisation['Research_facility_Budget_MoE'].data, newOrganisation['Research_facility_Budget_private_sector'].data, newOrganisation['Company_Budget'].data, newOrganisation['University_Budget_MoE'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Organisation inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_organisation.html", pageTitle = "Create Organisation", form = form)

@app.route("/Organisations/update/<int:idorg>", methods = ["POST"])
def updateOrganisation(idorg):
    """
    #Update a Organisation in the database, by id
    """
    form = OrganisationUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE org SET  Orgname = '{}', Abbreviation = '{}', City = '{}', Street_name = '{}', Postal_code = '{}', typec = '{}', Research_facility_Budget_MoE = '{}', Research_facility_Budget_private_sector = '{}', Company_Budget = '{}', University_Budget_MoE = '{}' WHERE idorg = {};".format( updateData['Orgname'].data, updateData['Abbreviation'].data, updateData['City'].data, updateData['Street_name'].data, updateData['Postal_code'].data, updateData['typec'].data, updateData['Research_facility_Budget_MoE'].data, updateData['Research_facility_Budget_private_sector'].data, updateData['Company_Budget'].data, updateData['University_Budget_MoE'].data,  idorg)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Organisation updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getOrganisations"))

@app.route("/Organisations/delete/<int:idorg>", methods = ["POST"])
def deleteOrganisation(idorg):
    """
    #Delete Organisation by id from database
    """
    query = f"DELETE FROM org WHERE idorg = {idorg};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Organisation deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getOrganisations"))



#Programs==========================================================================

@app.route("/Programs")
def getPrograms():
    """
    #Retrieve Programs from database
    """
    try:
        form = ProgramCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM program")
        column_names = [i[0] for i in cur.description]
        Programs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Programs.html", Programs = Programs, pageTitle = "Programs Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Programs/Create", methods = ["GET", "POST"]) ## "GET" by default
def createProgram():
    """
    #Create new Program in the database
    """
    form = ProgramCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newProgram = form.__dict__
        query = "INSERT INTO program(Program_name, Program_dept) VALUES ('{}', '{}');".format(newProgram['Program_name'].data, newProgram['Program_dept'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Program inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_program.html", pageTitle = "Create Program", form = form)

@app.route("/Programs/update/<int:idProgram>", methods = ["POST"])
def updateProgram(idProgram):
    """
    #Update a Program in the database, by id
    """
    form = ProgramUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE program SET Program_name = '{}', Program_dept = '{}' WHERE idProgram = {};".format(updateData['Program_name'].data, updateData['Program_dept'].data,  idProgram)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Program updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getPrograms"))

@app.route("/Programs/delete/<int:idProgram>", methods = ["POST"])
def deleteProgram(idProgram):
    """
    #Delete Program by id from database
    """
    query = f"DELETE FROM program WHERE idProgram = {idProgram};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Program deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getPrograms"))



#Executives==========================================================================

@app.route("/Executives")
def getExecutives():
    """
    #Retrieve Executives from database
    """
    try:
        form = ExecutiveCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM executive")
        column_names = [i[0] for i in cur.description]
        Executives = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Executives.html", Executives = Executives, pageTitle = "Executives Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Executives/Create", methods = ["GET", "POST"]) ## "GET" by default
def createExecutive():
    """
    #Create new Executive in the database
    """
    form = ExecutiveCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newExecutive = form.__dict__
        query = "INSERT INTO executive(Executive_name) VALUES ('{}');".format(newExecutive['Executive_name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Executive inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_Executive.html", pageTitle = "Create Executive", form = form)

@app.route("/Executives/update/<int:idExecutive>", methods = ["POST"])
def updateExecutive(idExecutive):
    """
    #Update a Executive in the database, by id
    """
    form = ExecutiveUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE executive SET Executive_name = '{}' WHERE idExecutive = {};".format(updateData['Executive_name'].data,  idExecutive)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Executive updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getExecutives"))

@app.route("/Executives/delete/<int:idExecutive>", methods = ["POST"])
def deleteExecutive(idExecutive):
    """
    #Delete Executive by id from database
    """
    query = f"DELETE FROM executive WHERE idExecutive = {idExecutive};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Executive deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getExecutives"))


#Deliverables==========================================================================

@app.route("/Deliverables")
def getDeliverables():
    """
    #Retrieve Deliverables from database
    """
    try:
        form = DeliverableCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM deliverable")
        column_names = [i[0] for i in cur.description]
        Deliverables = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Deliverables.html", Deliverables = Deliverables, pageTitle = "Deliverables Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Deliverables/Create", methods = ["GET", "POST"]) ## "GET" by default
def createDeliverable():
    """
    #Create new Deliverable in the database
    """
    form = DeliverableCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newDeliverable = form.__dict__
        query = "INSERT INTO deliverable(Deliverable_title, Deliverable_summary, Deliverable_date, Project_idProject) VALUES ('{}', '{}', '{}','{}');".format(newDeliverable['Deliverable_title'].data, newDeliverable['Deliverable_summary'].data, newDeliverable['Deliverable_date'].data, newDeliverable['Project_idProject'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Deliverable inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_deliverable.html", pageTitle = "Create Deliverable", form = form)

@app.route("/Deliverables/update/<int:idDeliverable>", methods = ["POST"])
def updateDeliverable(idDeliverable):
    """
    #Update a Deliverable in the database, by id
    """
    form = DeliverableUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE deliverable SET Deliverable_title = '{}', Deliverable_summary = '{}', Deliverable_date = '{}', Project_idProject = '{}' WHERE idDeliverable = {};".format(updateData['Deliverable_title'].data, updateData['Deliverable_summary'].data, updateData['Deliverable_date'].data, updateData['Project_idProject'].data,  idDeliverable)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Deliverable updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getDeliverables"))

@app.route("/Deliverables/delete/<int:idDeliverable>", methods = ["POST"])
def deleteDeliverable(idDeliverable):
    """
    #Delete Deliverable by id from database
    """
    query = f"DELETE FROM deliverable WHERE idDeliverable = {idDeliverable};"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Deliverable deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getDeliverables"))

#Phones=====================================================================


@app.route("/Phones")
def getPhones():
    """
    #Retrieve Phones from database
    """
    try:
        form = PhoneCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM phone ORDER BY org_idorg")
        column_names = [i[0] for i in cur.description]
        Phones = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Phones.html", Phones = Phones, pageTitle = "Phones Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Phones/Create", methods = ["GET", "POST"]) ## "GET" by default
def createPhone():
    """
    #Create new Phone in the database
    """
    form = PhoneCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newPhone = form.__dict__
        query = "INSERT INTO phone(Phone_number, org_idorg) VALUES ('{}', '{}');".format(newPhone['Phone_number'].data, newPhone['org_idorg'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Phone inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_phone.html", pageTitle = "Create Phone", form = form)

@app.route("/Phones/update/<string:Phone_number>", methods = ["POST"])
def updatePhone(Phone_number):
    """
    #Update a Phone in the database, by id
    """
    form = PhoneUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE phone SET Phone_number = '{}', org_idorg = '{}' WHERE Phone_number = '{}';".format(updateData['Phone_number'].data, updateData['org_idorg'].data,  Phone_number)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Phone updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getPhones"))

@app.route("/Phones/delete/<string:Phone_number>", methods = ["POST"])
def deletePhone(Phone_number):
    """
    #Delete Deliverable by id from database
    """
    query = f"DELETE FROM phone WHERE Phone_number  = '{Phone_number}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Phone deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getPhones"))


#Scientific_Domains=====================================================================


@app.route("/ScientificDomains")
def getScientificDomains():
    """
    #Retrieve Scientific_Domains from database
    """
    try:
        form = Scientific_DomainCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM scientific_domain")
        column_names = [i[0] for i in cur.description]
        ScientificDomains = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/ScientificDomains.html", ScientificDomains = ScientificDomains, pageTitle = "Scientific Domains Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/ScientificDomains/Create", methods = ["GET", "POST"]) ## "GET" by default
def createScientific_Domain():
    """
    #Create new Scientific_Domain in the database
    """
    form = Scientific_DomainCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newScientific_Domain = form.__dict__
        query = "INSERT INTO scientific_domain(Scientific_domain_name) VALUES ('{}');".format(newScientific_Domain['Scientific_domain_name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Scientific Domain inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_scientific_domain.html", pageTitle = "Create Scientific_Domain", form = form)

@app.route("/ScientificDomains/update/<string:Scientific_domain_name>", methods = ["POST"])
def updateScientific_Domain(Scientific_domain_name):
    """
    #Update a Scientific_domain in the database, by id
    """
    form = Scientific_DomainUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE scientific_domain SET Scientific_domain_name = '{}' WHERE Scientific_domain_name = '{}';".format(updateData['Scientific_domain_name'].data,  Scientific_domain_name)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Scientific_Domain updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getScientificDomains"))

@app.route("/ScientificDomains/delete/<string:Scientific_domain_name>", methods = ["POST"])
def deleteScientific_Domain(Scientific_domain_name):
    """
    #Delete scientific_domain by id from database
    """
    query = f"DELETE FROM scientific_domain WHERE Scientific_domain_name  = '{Scientific_domain_name}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Scientific Domain deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getScientificDomains"))






#Works=====================================================================


@app.route("/Works")
def getWorks():
    """
    #Retrieve Works from database
    """
    try:
        form = WorksCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM works")
        column_names = [i[0] for i in cur.description]
        Works = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/Works.html", Works = Works, pageTitle = "Which researcher works on which project", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/Works/Create", methods = ["GET", "POST"]) ## "GET" by default
def createWork():
    """
    #Create new Work in the database
    """
    form = WorksCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newWork = form.__dict__
        query = "INSERT INTO works(Project_idProject, researcher_idresearcher) VALUES ('{}', '{}');".format(newWork['Project_idProject'].data, newWork['researcher_idresearcher'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Work inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_work.html", pageTitle = "Create Work", form = form)

@app.route("/Works/<int:Project_idProject>/update/<int:researcher_idresearcher>", methods = ["POST"])
def updateWork(Project_idProject, researcher_idresearcher):
    """
    #Update a Work in the database, by id
    """
    form = WorksUpdate()
    updateData = form.__dict__
    
    if(form.validate_on_submit()):
        query = "UPDATE works SET Project_idProject = '{}', researcher_idresearcher = '{}' WHERE Project_idProject = '{}' AND researcher_idresearcher = '{}';".format(updateData['Project_idProject'].data, updateData['researcher_idresearcher'].data,  Project_idProject, researcher_idresearcher)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash(" Work updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getWorks"))

@app.route("/Works/<int:Project_idProject>/delete/<int:researcher_idresearcher>", methods = ["POST"])
def deleteWork(Project_idProject, researcher_idresearcher):
    """
    #Delete Deliverable by id from database
    """
    query = f"DELETE FROM works WHERE Project_idProject  = '{Project_idProject}' AND researcher_idresearcher = '{researcher_idresearcher}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Work deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getWorks"))



#ProjectHasScientificDomains=====================================================================


@app.route("/ProjectHasDomains")
def getProjectHasDomains():
    """
    #Retrieve ProjectHasDomains from database
    """
    try:
        form = ProjectHasDomainCreate()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM project_has_scientific_domain")
        column_names = [i[0] for i in cur.description]
        ProjectHasDomains = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("Get/ProjectHasDomains.html", ProjectHasDomains = ProjectHasDomains, pageTitle = "Which researcher works on which project", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)



@app.route("/ProjectHasDomains/Create", methods = ["GET", "POST"]) ## "GET" by default
def createProjectHasDomain():
    """
    #Create new ProjectHasDomain in the database
    """
    form = ProjectHasDomainCreate()
    ## when the form is submitted
    if(request.method == "POST"):
        newProjectHasDomain = form.__dict__
        query = "INSERT INTO project_has_scientific_domain(Project_idProject, Scientific_domain_Scientific_domain_name) VALUES ('{}', '{}');".format(newProjectHasDomain['Project_idProject'].data, newProjectHasDomain['Scientific_domain_Scientific_domain_name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Project Has Domain inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("Create/create_projectHasDomain.html", pageTitle = "Create Project Has Domain", form = form)

@app.route("/ProjectHasDomains/<int:Project_idProject>/update/<string:Scientific_domain_Scientific_domain_name>", methods = ["POST"])
def updateProjectHasDomain(Project_idProject, Scientific_domain_Scientific_domain_name):
    """
    #Update a Project Has Domain in the database, by id
    """
    form = ProjectHasDomainUpdate()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE project_has_scientific_domain SET Project_idProject = '{}', Scientific_domain_Scientific_domain_name = '{}' WHERE Project_idProject = '{}' AND Scientific_domain_Scientific_domain_name = '{}';".format(updateData['Project_idProject'].data, updateData['Scientific_domain_Scientific_domain_name'].data,  Project_idProject, Scientific_domain_Scientific_domain_name)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Project Has Domain updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getProjectHasDomains"))

@app.route("/ProjectHasDomains/<int:Project_idProject>/delete/<string:Scientific_domain_Scientific_domain_name>", methods = ["POST"])
def deleteProjectHasDomain(Project_idProject, Scientific_domain_Scientific_domain_name):
    """
    #Delete Project Has Domain by id from database
    """
    query = f"DELETE FROM project_has_scientific_domain WHERE Project_idProject  = '{Project_idProject}' AND Scientific_domain_Scientific_domain_name = '{Scientific_domain_Scientific_domain_name}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project Has Domain deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getProjectHasDomains"))

#Errors===================================================================


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
