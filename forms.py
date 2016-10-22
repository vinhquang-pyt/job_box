from flask.ext.wtf import Form
from wtforms import TextField, FileField, SubmitField

class ApplicationForm(Form):
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    email = TextField("Email")
    resume = FileField("Resume")

    submit = SubmitField('Apply')
