from flask import Flask, render_template, url_for

app = Flask(__name__)

"""Route to Landing PAGE"""
@app.route('/')
def hello_world():
    background_image_urls = [
        url_for('static', filename='images/home1.jpg'),
        url_for('static', filename='images/home2.jpg'),
        url_for('static', filename='images/home3.jpg'),
        url_for('static', filename='images/hma_banner.jpg'),
        url_for('static', filename='images/hma3.jpg'),
        url_for('static', filename='images/hma1.jpg'),
        url_for('static', filename='images/about.jpg')
    ]
    return render_template('landing_page.html', images = background_image_urls)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/users')
def users():
    return render_template('users.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)