from flask import Flask, flash, redirect, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '87370273d704e35e24f622c1bfa1490c'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date_posted': 'May 22, 2022'
    },
    {
        'author': 'Jone Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 22, 2022'
    }
]


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == "admin@blog.com" and form.password.data == "abc"):
            flash("You have been logged in Successfully!!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check Username or Password", "danger")
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
