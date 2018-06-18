import os

from flask import Flask, g, session
from core import api, models, user, site, acquisition

app = Flask(__name__)
app.config.from_object("core.config")

app.register_blueprint(api.app, url_prefix="/api")
app.register_blueprint(acquisition.app, url_prefix="/acquisition")
app.register_blueprint(user.app, url_prefix="/user")
app.register_blueprint(site.app, url_prefix="/")

@app.before_request
def before_request():
	environment = os.getenv('ENVIRONMENT', 'development')
	if environment == 'production':
		g._environment = 'production'
	elif environment == 'stage':
		g._environment = 'stage'
		app.config['TESTING'] = True
	else:
		g._environment = 'development'
		app.config['DEBUG'] = True
	models.initialize_db()
	try:
		if 'user' in session:
			g.user = models.User.get(models.User.id == session['user'])
		else:
			g.user = None
	except models.DoesNotExist:
		g.user = None

@app.teardown_request
def teardown_request(exception):
	models.close_db()

	''' Register modules '''

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)