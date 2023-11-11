from flask import Flask, render_template
from cloudwatch.router.srv import srv_page
from cloudwatch import config
from cloudwatch.utils import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def dashboard():
    # This is where you'll fetch your data and pass it to your template
    return render_template('dashboard.html')

app.register_blueprint(srv_page)


if __name__ == '__main__':
    app.run(debug=True)