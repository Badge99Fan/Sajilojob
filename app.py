from Modals import *
from Forms import *
import time
from flask import request

@app.route('/')
def index():
   posts=Posts.query.all()
   
   return render_template('all_posts.html',posts=posts)

@app.route('/signup',methods=['GET','POST'])
def signup():
    s_form=Signup()
    if s_form.validate_on_submit():
        user_name=s_form.username.data
        user_email=s_form.user_email.data
        user_phone_num=s_form.user_phone_num.data
        user_password=s_form.user_password.data
        user=User.query.filter_by(email=user_email).first()
        if user:
            flash('This email is already taken')
            return redirect(url_for('signup'))
        else:
            new_user=User(username=user_name,email=user_email,phone_num=user_phone_num,password=user_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('profile'))
    return render_template('signup.html',form=s_form)

@app.route('/login',methods=['GET','POST'])
def login():
    l_form=Login()
    if l_form.validate_on_submit():
        user_email=l_form.user_email.data
        user_password=l_form.user_password.data
        user=User.query.filter_by(email=user_email).first()

        if user and user.check_password(passwordfield=user_password):
            flash('Login Successfully!')
            login_user(user)
            next=request.args.get('next')
            if next==None:
                next=url_for('profile')
            return redirect(next)
       
    return render_template('login.html',form=l_form)


@app.route('/post',methods=['GET','POST'])
@login_required
def post():
    p_form=PostForm()
    if p_form.validate_on_submit():
        current_time=dt.datetime.now()
        post_time=current_time.strftime("%d %B,%Y")
        title=p_form.post_title.data.title()
        salary=p_form.post_salary.data
        qualification=p_form.post_qualification.data
        description=p_form.post_description.data
        location=p_form.location.data
        user=current_user.id
        post=Posts(post_title=title,post_salary=salary,post_qualificaitoin=qualification,post_description=description,location=location,user_id=user,post_time=post_time)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html',form=p_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',user=current_user)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
       
        f=request.files['file']
        if f:
            f.save("static/img/"+f.filename)
            current_user.profile_img=f.filename
       
        username=request.form['username']
        phone_num=request.form['phone_num']
 
        
        current_user.username=username
        current_user.phone_number=phone_num
        db.session.commit()

        

        return redirect(url_for('profile'))
    return render_template('upload.html')
 
@app.route('/delete/<int:id>')
def delete(id):
    post=Posts.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    post=Posts.query.filter_by(id=id).first()
    if request.method == 'POST':
        post.post_title = request.form['title'].title()
        post.post_salary = request.form['salary']
        post.location = request.form['location']
        post.post_qualification = request.form['qualification']
        post.post_description = request.form['description']
        db.session.commit()
        return redirect(url_for('profile'))

     
        
    return render_template('update.html',data=post)

@app.route('/blog/<int:id>')
def blog(id):
    post=Posts.query.filter_by(id=id).first()
    return render_template('blog.html',blog=post)
@app.route('/gmail')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search'].title()
        posts = Posts.query.filter_by(post_title=search_term).all()  # Use .all() to get all results

        if not posts:  # Check if no posts were found
            flash('Nothing found')
            return render_template('results.html', searches=[])
        else:
            return render_template('results.html', searches=posts)

    return redirect(url_for('index'))
 
@app.route('/admin')
@login_required
def admin():
    all_posts=Posts.query.all()
    return render_template('admin.html',posts=all_posts)


@app.route('/mail')
def mail():
    return redirect("https://mail.google.com/mail/u/0/#inbox?compose=new", code=302)
if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)