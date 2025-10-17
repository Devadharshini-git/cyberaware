from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/tips')
def tips():
    return render_template('tips.html', title="Safety Tips")

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title="Cyber Quiz")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['message']
        message = f"Thank you {name}, your feedback has been received!"
    return render_template('contact.html', title="Contact Us", message=message)

if __name__ == '__main__':
    app.run(debug=True)
