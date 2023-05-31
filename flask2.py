from flask import Flask, render_template
app = Flask(__name__)
@app.route("/read")

def studnet_page():
    name = "soham"
    return render_template("read.html",student_name = name)
app.run()