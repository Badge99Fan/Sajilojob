from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed

#################### LOGIN FORM #######################################


class Login(FlaskForm):

    user_email = EmailField('Enter your email', validators=[DataRequired()])
    user_password = PasswordField(
        'Enter your password', validators=[DataRequired()])
    submit = SubmitField('Login')


#######################################################

####################################    SIGNUP FORM #####################################
class Signup(FlaskForm):
    username = StringField('Enter your Username',validators=[DataRequired()])
    user_email=EmailField('Enter your email',validators=[DataRequired()])
    user_phone_num=StringField('Enter your Phone number',validators=[DataRequired()])
    user_password=PasswordField('Enter your password',validators=[DataRequired()])
    submit=SubmitField('Signup')
#################################################################################
    
################ POST FORM #############################
class PostForm(FlaskForm):
    post_title=StringField('Enter the post name')
    post_salary=StringField('Enter the Salary')
    location=StringField('Enter the post location')
    post_qualification=TextAreaField('Enter the qualifications for the job', render_kw={'rows': 5, 'cols': 40})
    post_description=TextAreaField('Enter the post_description', render_kw={'rows': 2, 'cols': 40})
    submit=SubmitField('Post')

###################################################################
###################### UPLOAD FILES ##########################
class UploadForm(FlaskForm):
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit=SubmitField('Submit')

