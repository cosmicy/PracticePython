'''fwefwe'''
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    '''fewf'''
    return "Hell66o, World!"


@app.route('/indexa')
def indexa():
    '''fsdfsf'''
    user = {'nickname': 'Miguel'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''


@app.route('/indext')
def indext():
    '''fewf'''
    user = {'nickname': 'Miguffel'}  # fake user
    return render_template("index.html", title='Home', user=user)


@app.route('/indexf')
def indexf():
    '''fewf'''
    user = {'nickname': 'Miguffel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Johnefef'},
            'body': 'Beautiful day in Pofefeefrtland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index2.html", title='Home', user=user, posts=posts)
