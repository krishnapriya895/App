from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
entries = []
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
         name = request.form['name']
         email = request.form['email']
         entries.append({'name': name, 'email': email})
         return redirect(url_for('index'))
    return render_template('index.html', entries=entries)
 
if __name__ == '__main__':
     app.run(debug=True)

