from flask import *
from forms import ApplicationForm
from functools import wraps

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'our_secret_key'
    app.config['CSRF_SESSION_KEY'] = 'THIS IS THE OTHER KEY'
    @app.route('/')
    def index():
        return render_template('index.html')

    def login_required(test):
        @wraps(test)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return test(*args, **kwargs)
            else:
                flash('You need to login first')
                return redirect(url_for('login'))
        return wrap

    @app.route('/hello')
    @login_required
    def hello():
        return render_template('hello.html')

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged_out')
        return redirect (url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                return redirect(url_for('hello'))
        return render_template('login.html', error=error)

    @app.route('/apply', methods=['GET', 'POST'])
    def apply():
        form = ApplicationForm(request.form)
        if form.validate_on_submit():
            return 'Thanks for applying'
        return render_template('application.html', form = form)

    return app
