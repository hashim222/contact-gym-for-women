from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about-us.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form['fname'])
        print(request.form['email'])
    return render_template('contact-us.html')


if __name__ == '__main__':
    app.run(debug=True)
