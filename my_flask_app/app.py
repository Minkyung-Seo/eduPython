from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'title': 'Hello, Flask! 나의 동적페이지...',
        'description': 'This is a simple web application using Flask and Jinja2.',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
