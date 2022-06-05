from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Email, Optional, NumberRange, Length

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field


class ProjResCreate(FlaskForm):
    idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
    Project_title = StringField(label = "Project_title", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
    idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
    Full_name = StringField(label = "Full Name of Researcher", validators = [Optional()])
    submit = SubmitField("Create")

class ResOrgCreate(FlaskForm):
	idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
	Full_name = StringField(label = "Full Name of Researcher", validators = [Optional()])
	idorg = IntegerField(label = "idorg", validators = [Optional()])
	Orgname = StringField(label = "Orgname", validators = [Length(min=1, max=20), DataRequired(message="Organisation Name is a required field.")])
	Abbreviation = StringField(label = "Abbreviation", validators = [Length(min=1, max=7), DataRequired(message="Abbreviation is a required field.")])
	submit = SubmitField("Create")

class Get33(FlaskForm):
	Scientific_domain_Scientific_domain_name = StringField(label = "Scientific_domain_Scientific_domain_name", validators = [Optional()])
	idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
	Project_starting = DateField(label = "Project_starting", validators = [Optional()])
	researcher_idresearcher = IntegerField(label = "Select Manager ID", validators = [NumberRange(min=1)])
	Project_ending = DateField(label = "Project_ending", validators = [Optional()])
	idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
	Researcher_name = StringField(label = "Researcher_name", validators = [Length(min=1, max=30), DataRequired(message="Name is a required field.")])
	Researcher_surname = StringField(label = "Researcher_surname", validators = [Length(min=1, max=45), DataRequired(message="Surname is a required field.")])
	submit = SubmitField("Create")

class Get34(FlaskForm):
	idorg = IntegerField(label = "idorg", validators = [Optional()])
	cnt = IntegerField(label = "Count", validators = [NumberRange(min=0)])
	submit = SubmitField("Create")

class Get35(FlaskForm):
	Scientific_domain_Scientific_domain_name1 = StringField(label = "Scientific_domain_Scientific_domain_name", validators = [Optional()])
	Scientific_domain_Scientific_domain_name2 = StringField(label = "Scientific_domain_Scientific_domain_name", validators = [Optional()])
	count = IntegerField(label = "Count", validators = [NumberRange(min=0)])
	submit = SubmitField("Create")
    
class Get36(FlaskForm):
	researcher_idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
	researcher_date_of_birth = DateField(label = "researcher_date_of_birth", validators = [Optional()])
	cnt = IntegerField(label = "Count", validators = [NumberRange(min=0)]) 
	submit = SubmitField("Create")
    
class Get37(FlaskForm):
	Executive_name = StringField(label = "Executive_name", validators = [Length(min=1, max=20), DataRequired(message="Name is a required field.")])
	Orgname = StringField(label = "Orgname", validators = [Length(min=1), DataRequired(message="Organisation Name is a required field.")])
	sumb = IntegerField(label = "Sum Up", validators = [NumberRange(min=0)])
	submit = SubmitField("Create")

class Get38(FlaskForm):
    Full_name = StringField(label = "Full Name of Researcher", validators = [Optional()])
    idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
    cnt = IntegerField(label = "Count", validators = [NumberRange(min=0)])
    submit = SubmitField("Create")

#Create Classes
class ProjectCreate(FlaskForm):
    idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
    Project_title = StringField(label = "Project_title", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
    Project_summary = TextAreaField(label = "Project_summary", validators = [Length(min=1), DataRequired(message="Summary is a required field.")])
    Project_starting = DateField(label = "Project_starting", validators = [Optional()])
    Project_ending = DateField(label = "Project_ending", validators = [Optional()])
    Project_budget = FloatField(label = "Project_budget", validators =  [NumberRange(min=0), Optional()])
    org_idorg = IntegerField(label = "Organisation ID", validators = [NumberRange(min=1)])
    researcher_idresearcher = IntegerField(label = "Select Manager ID", validators = [NumberRange(min=1)])
    Executive_idExecutive = IntegerField(label = "Executive ID", validators = [NumberRange(min=1)])
    Program_idProgram = IntegerField(label = "Select Associated Program ID", validators = [NumberRange(min=1)])
    researcher_ideval = IntegerField(label = "Select Evaluator ID", validators = [NumberRange(min=1)])
    EvalGrade = IntegerField(label = "Grade of Evaluation", validators = [NumberRange(min=0, max=100), Optional()])
    EvalDate = DateField(label = "Date of Evaluation", validators = [Optional()])
    submit = SubmitField("Create")
    
class ResearcherCreate(FlaskForm):
	idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
	Researcher_name = StringField(label = "Researcher_name", validators = [Length(min=1, max=30), DataRequired(message="Name is a required field.")])
	Researcher_surname = StringField(label = "Researcher_surname", validators = [Length(min=1, max=45), DataRequired(message="Surname is a required field.")])
	Researcher_gender = RadioField(u'Researcher_gender', choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary')], validators = [Optional()])
	researcher_date_of_birth = DateField(label = "researcher_date_of_birth", validators = [Optional()])
	researcher_hire_date = DateField(label = "researcher_hire_date", validators = [Optional()])
	org_idorg = IntegerField(label = "Organisation ID", validators = [NumberRange(min=1)])
	submit = SubmitField("Create")

class OrganisationCreate(FlaskForm):
	idorg = IntegerField(label = "idorg", validators = [Optional()])
	City = StringField(label = "city", validators = [Length(min=1, max=20), DataRequired(message="City is a required field.")])
	Street_name = StringField(label = "Street_name", validators = [Length(min=1), DataRequired(message="Street Name is a required field.")])
	Postal_code = IntegerField(label = "Postal_code", validators = [NumberRange(min=00000, max=99999), DataRequired(message="Postal Code is a required field.")])
	typec = RadioField(u'Organisation Types: ', choices=[('Uni','University'), ('Comp','Company'), ('RF', 'Research Facility')], validators = [DataRequired(message="Type of Organisation is a required field")] )
	Research_facility_Budget_MoE = FloatField(label = "Research_facility_Budget_MoE", validators =  [NumberRange(min=0), Optional()])
	Research_facility_Budget_private_sector = FloatField(label = "Research_facility_Budget_private_sector", validators =  [NumberRange(min=0), Optional()])
	Company_Budget = FloatField(label = "Company_Budget", validators =  [NumberRange(min=0), Optional()])
	University_Budget_MoE = FloatField(label = "University_Budget_MoE", validators =  [NumberRange(min=0), Optional()])
	Orgname = StringField(label = "Orgname", validators = [Length(min=1), DataRequired(message="Organisation Name is a required field.")])
	Abbreviation = StringField(label = "Abbreviation", validators = [Length(min=1, max=7), DataRequired(message="Abbreviation is a required field.")])
	submit = SubmitField("Create")
	
class ExecutiveCreate(FlaskForm):
	idExecutive = IntegerField(label = "idExecutive", validators = [Optional()])
	Executive_name = StringField(label = "Executive_name", validators = [Length(min=1, max=20), DataRequired(message="Name is a required field.")])
	submit = SubmitField("Create")
	
class ProgramCreate(FlaskForm):
	idProgram = IntegerField(label = "idProgram", validators = [Optional()])
	Program_name = StringField(label = "Program_name", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
	Program_dept = StringField(label = "Program_dept", validators = [Length(min=1, max=30), DataRequired(message="Department is a required field.")])
	submit = SubmitField("Create")
	
class Scientific_DomainCreate(FlaskForm):
	Scientific_domain_name = StringField(label = "Scientific_domain_name", validators = [Length(min=1, max=50), DataRequired(message="Scientific Domain Name is a required field.")])
	submit = SubmitField("Create")
	
class DeliverableCreate(FlaskForm):
	idDeliverable = IntegerField(label = "idDeliverable", validators = [Optional()])
	Deliverable_title = StringField(label = "Deliverable_title", validators = [Length(min=1, max=45), DataRequired(message="Title is a required field.")])
	Deliverable_summary = TextAreaField(label = "Deliverable_summary", validators = [Length(min=1), DataRequired(message="Summary is a required field.")])
	Deliverable_date = DateField(label = "Deliverable_date", validators = [Optional()])
	Project_idProject = IntegerField(label = "Project_idProject", validators = [Optional()])
	submit = SubmitField("Create")

class PhoneCreate(FlaskForm):
	Phone_number = StringField(label ="Phone_number", validators = [Optional()])
	org_idorg = IntegerField(label = "org_idorg", validators = [NumberRange(min=0)])
	submit = SubmitField("Create")
	
class WorksCreate(FlaskForm):
	Project_idProject = IntegerField(label = "idProject", validators = [Optional()])
	researcher_idresearcher = IntegerField(label = "idresearcher", validators = [Optional()])
	submit = SubmitField("Create")

class ProjectHasDomainCreate(FlaskForm):
	Project_idProject = IntegerField(label = "idProject", validators = [Optional()])
	Scientific_domain_Scientific_domain_name = StringField(label = "Scientific_domain_Scientific_domain_name", validators = [Optional()])
	submit = SubmitField("Create")

#UpdateClasses

class ProjectUpdate(FlaskForm):
    idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
    Project_title = StringField(label = "Project_title", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
    Project_summary = TextAreaField(label = "Project_summary", validators = [Length(min=1), DataRequired(message="Summary is a required field.")])
    Project_budget = FloatField(label = "Project_budget", validators =  [NumberRange(min=0), Optional()])
    Project_starting = DateField(label = "Project_starting", validators = [Optional()])
    Project_ending = DateField(label = "Project_ending", validators = [Optional()])
    org_idorg = IntegerField(label = "Organisation ID", validators = [NumberRange(min=1)])
    researcher_idresearcher = IntegerField(label = "Select Manager ID", validators = [NumberRange(min=1)])
    Executive_idExecutive = IntegerField(label = "Executive ID", validators = [NumberRange(min=1)])
    Program_idProgram = IntegerField(label = "Select Associated Program ID", validators = [NumberRange(min=1)])
    researcher_ideval = IntegerField(label = "Select Evaluator ID", validators = [NumberRange(min=1)])
    EvalGrade = IntegerField(label = "Grade of Evaluation", validators = [NumberRange(min=0, max=100), Optional()])
    EvalDate = DateField(label = "Date of Evaluation", validators = [Optional()])
    submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

    
class ResearcherUpdate(FlaskForm):
	idresearcher = IntegerField(label = "idresearcher", validators = [NumberRange(min=1)])
	Researcher_name = StringField(label = "Researcher_name", validators = [Length(min=1, max=30), DataRequired(message="Name is a required field.")])
	Researcher_surname = StringField(label = "Researcher_surname", validators = [Length(min=1, max=45), DataRequired(message="Surname is a required field.")])
	Researcher_gender = RadioField(u'Researcher_gender', choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary')], validators = [Optional()])
	researcher_date_of_birth = DateField(label = "researcher_date_of_birth", validators = [Optional()])
	researcher_hire_date = DateField(label = "researcher_hire_date", validators = [Optional()])
	org_idorg = IntegerField(label = "Organisation ID", validators = [NumberRange(min=1)])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])


class OrganisationUpdate(FlaskForm):
	idorg = IntegerField(label = "idorg", validators = [NumberRange(min=1)])
	City = StringField(label = "city", validators = [Length(min=1, max=20), DataRequired(message="City is a required field.")])
	Street_name = StringField(label = "Street_name", validators = [Length(min=1, max=20), DataRequired(message="Street Name is a required field.")])
	Postal_code = IntegerField(label = "Postal_code", validators = [NumberRange(min=00000, max=99999), DataRequired(message="Postal Code is a required field.")])
	typec = RadioField(u'Organisation Types: ', choices=[('Uni','University'), ('Comp','Company'), ('RF', 'Research Facility')], validators = [DataRequired(message="Type of Organisation is a required field")] )
	Research_facility_Budget_MoE = FloatField(label = "Research_facility_Budget_MoE", validators =  [NumberRange(min=0), Optional()])
	Research_facility_Budget_private_sector = FloatField(label = "Research_facility_Budget_private_sector", validators =  [NumberRange(min=0), Optional()])
	Company_Budget = FloatField(label = "Company_Budget", validators =  [NumberRange(min=0), Optional()])
	University_Budget_MoE = FloatField(label = "University_Budget_MoE", validators =  [NumberRange(min=0), Optional()])
	Orgname = StringField(label = "Orgname", validators = [Length(min=1), DataRequired(message="Organisation Name is a required field.")])
	Abbreviation = StringField(label = "Abbreviation", validators = [Length(min=1), DataRequired(message="Abbreviation is a required field.")])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

	
class ExecutiveUpdate(FlaskForm):
	idExecutive = IntegerField(label = "idExecutive", validators = [NumberRange(min=1)])
	Executive_name = StringField(label = "Executive_name", validators = [Length(min=1, max=20), DataRequired(message="Name is a required field.")])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

	
class ProgramUpdate(FlaskForm):
	Program_name = StringField(label = "Program_name", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
	Program_dept = StringField(label = "Program_dept", validators = [Length(min=1, max=30), DataRequired(message="Department is a required field.")])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

class Scientific_DomainUpdate(FlaskForm):
	Scientific_domain_name = StringField(label = "Scientific_domain_name", validators = [Length(min=1, max=50), DataRequired(message="Scientific Domain Name is a required field.")])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

	
class DeliverableUpdate(FlaskForm):
	idDeliverable = IntegerField(label = "idDeliverable", validators = [Optional()])
	Deliverable_title = StringField(label = "Deliverable_title", validators = [Length(min=1, max=45), DataRequired(message="Title is a required field.")])
	Deliverable_summary = TextAreaField(label = "Deliverable_summary", validators = [Length(min=1), DataRequired(message="Summary is a required field.")])
	Deliverable_date = DateField(label = "Deliverable_date", validators = [Optional()])
	Project_idProject = IntegerField(label = "Project_idProject", validators = [Optional()])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

class PhoneUpdate(FlaskForm):
	Phone_number = IntegerField(label ="Phone_number", validators = [Optional()])
	org_idorg = IntegerField(label = "org_idorg", validators = [NumberRange(min=0)])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

	
class WorksUpdate(FlaskForm):
	Project_idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
	researcher_idresearcher = IntegerField(label = "idresearcher", validators = [NumberRange(min=1)])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])

class ProjectHasDomainUpdate(FlaskForm):
	Project_idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
	Scientific_domain_Scientific_domain_name = StringField(label = "Scientific_domain_Scientific_domain_name", validators = [Optional()])
	submit = SubmitField("Submit", validators = [DataRequired(message="Name is a required field.")])




#FilterClasses

class ProjectFilter(FlaskForm):
    idProject = IntegerField(label = "idProject", validators = [NumberRange(min=1)])
    Project_title = StringField(label = "Project_title", validators = [Length(min=1, max=45), DataRequired(message="Name is a required field.")])
    Project_summary = TextAreaField(label = "Project_summary", validators = [Length(min=1), DataRequired(message="Summary is a required field.")])
    Project_budget = FloatField(label = "Project_budget", validators =  [NumberRange(min=0), Optional()])
    Project_starting = DateField(label = "Project_starting", validators = [Optional()])
    Project_ending = DateField(label = "Project_ending", validators = [Optional()])
    org_idorg = IntegerField(label = "Organisation ID", validators = [NumberRange(min=1)])
    researcher_idresearcher = IntegerField(label = "Select Manager ID", validators = [NumberRange(min=1)])
    Executive_idExecutive = IntegerField(label = "Executive ID", validators = [NumberRange(min=1)])
    Program_idProgram = IntegerField(label = "Select Associated Program ID", validators = [NumberRange(min=1)])
    researcher_ideval = IntegerField(label = "Select Evaluator ID", validators = [NumberRange(min=1)])
    EvalGrade = IntegerField(label = "Grade of Evaluation", validators = [NumberRange(min=0, max=100), Optional()])
    EvalDate = DateField(label = "Date of Evaluation", validators = [Optional()])
    submit = SubmitField("Filter")

