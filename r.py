from f import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory list to store submissions
submissions = []

@app.route('/')
def index():
    return render_template('index.html', submissions=submissions)

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form.get('name')
    email = request.form.get('email')

    # Store in submissions list
    submissions.append({'name': name, 'email': email})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
