from flask import Flask, render_template, url_for

app = Flask(__name__)

"""Route to Landing PAGE"""
@app.route('/')
def hello_world():
    background_image_urls = [
        url_for('static', filename='images/home1.jpg'),
        url_for('static', filename='images/home2.jpg'),
        url_for('static', filename='images/home3.jpg')
    ]
    return render_template('landing_page.html', images = background_image_urls)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)