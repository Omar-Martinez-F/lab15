from flask import Flask , render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def task2():
    p1 = "<p>Erin: lol</p>"
    p2 = "<p>Teddy: lmao</p>"
    p3 = "<p>Ariel: bo2 </p>"
    return p1+p2 + p3



@app.route("/omar")
def task3():
    return render_template("template.html")

# link to repo: https://github.com/Omar-Martinez-F/lab15