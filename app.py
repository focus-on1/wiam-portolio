from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/a-propos')
def about():
    return render_template('a-propos.html')

@app.route('/experience-formation')
def experience():
    return render_template('experience-formation.html')

@app.route('/competences')
def skills():
    return render_template('competences.html')

@app.route('/projets')
def projects():
    return render_template('projets.html')

@app.route('/projets/flowry')
def projects_flowry():
    return render_template('flowry.html')

@app.route('/projets/delices-du-liban')
def projects_delice_liban():
    return render_template('delice_liban.html')

@app.route('/projets/eco-beauty')
def projects_eco_beauty():
    return render_template('eco_beauty.html')

@app.route('/projets/table-anouk')
def projects_table_annouk():
    return render_template('table_annouk.html')

@app.route('/projets/tc-france')
def projects_TC_Francek():
    return render_template('TC-France.html')

@app.route('/projets/secret')
def projects_secret():
    return render_template('projectfutur.html')





@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)