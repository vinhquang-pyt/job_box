from flask import Flask, render_template, request
from forms import ApplicationForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'our_secret_key'
    app.config['CSRF_SESSION_KEY'] = 'THIS IS THE OTHER KEY'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/apply', methods=['GET', 'POST'])
    def apply():
        form = ApplicationForm(request.form)
        if form.validate_on_submit():
            return 'Thanks for applying'
        return render_template('application.html', form = form)


    return app
