from flask import *
from forms import ApplicationForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'our_secret_key'
    app.config['CSRF_SESSION_KEY'] = 'THIS IS THE OTHER KEY'
    @app.route('/')
    def index():
        return render_template('index.html')

    # @app.route('/login')
    # def login():
    #     return render_template('login.html')

    @app.route('/hello')
    def hello():
        return render_template('hello.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('hello'))
        return render_template('login.html', error=error)

    @app.route('/apply', methods=['GET', 'POST'])
    def apply():
        form = ApplicationForm(request.form)
        if form.validate_on_submit():
            return 'Thanks for applying'
        return render_template('application.html', form = form)



    return app
