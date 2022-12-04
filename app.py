from flask import Flask, render_template, request, jsonify
from catenary import catenary_plot
app = Flask(__name__)

@app.route("/")
def home_page(name=None):
    return render_template('index.html',name=name)
    #return "<p>Bhadva</p>"

@app.route("/projects")
def projects(name=None):
    return render_template('index1.html',name=name)

@app.route("/tools")
def tools(name=None):
    return render_template('index2.html',name=name)

@app.route('/catenary')
def catenary(name=None):
    return render_template('index3.html',name=name)

@app.route('/catenary_solved',methods=['POST'])
def catenary_solved(name=None):
    h = request.form['h']
    s = request.form['s']
    # operation = str(request.form['operation'])

    result = catenary_plot(h,s)

    return render_template('index3.html', prediction_text=str(result),name=name)

if __name__== "__main__":
    app.run(debug=True, port=5000)