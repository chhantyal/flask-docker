from flask import Flask, render_template
from whitenoise import WhiteNoise


app = Flask(__name__)
app.secret_key = '[keep it secret]'
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
