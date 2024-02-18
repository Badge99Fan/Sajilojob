from __init__ import *
import datetime as dt
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
#################   CREATING DATABASE ######################################
class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)

    email=db.Column(db.Text(),nullable=False)
    phone_number=db.Column(db.Integer(),nullable=False)
    password=db.Column(db.Text(),nullable=False)
    profile_img=db.Column(db.Text(),default='default.jpg')
    post=db.relationship('Posts',backref='user',lazy='dynamic')

    def __init__(self,username,email,phone_num,password) -> None:
        self.username=username
        self.email=email
        self.phone_number=phone_num
        self.password=generate_password_hash(password)

    def check_password(self,passwordfield):
        check=check_password_hash(self.password,passwordfield)
        if check:
            return True
        else:
            return flash('Invalid password')
        
##################################################################
        
############    Posts Database ###################
        
class Posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_title=db.Column(db.Text())
    post_salary=db.Column(db.Text())
    location=db.Column(db.Text())
    post_qualification=db.Column(db.Text())
    post_description=db.Column(db.Text())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    post_time=db.Column(db.Text())

    def __init__(self,post_title,post_salary,post_qualificaitoin,post_description,location,user_id,post_time) -> None:
        self.post_title=post_title
        self.post_salary=post_salary
        self.post_qualification=post_qualificaitoin
        self.post_description=post_description
        self.location=location
        self.post_time=post_time
        self.user_id=user_id


#####################################################################
        
