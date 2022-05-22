from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title' : 'Blog Post',
        'content' : 'First Post Content',
        'date_posted': 'May 22, 2022'
    },
    {
        'author': 'Jone Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted': 'May 22, 2022'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)