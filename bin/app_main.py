from flask import Flask, request, redirect, render_template, flash
from flask_login import LoginManager, UserMixin, login_user, UserMixin, login_required, logout_user
import dpcenter
from subprocess import check_output, CalledProcessError
import json
import config

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to access to main page'
login_manager.login_message_category = ['danger', 'Error_Access:']
app.secret_key = config.SECRET_KEY

class User(UserMixin):
	def __init__(self, id):
		self.id = id
	def __repr__(self):
		return "%d"% (self.id)

user = User(0)

def check_login():
	username = request.form['username']
	password = request.form['password']
	if username == config.USERNAME and password == config.PASSWORD:
		return True
	return False

@app.route('/', methods=['GET', 'POST'])
@login_required
def main():
	dpcenter.start()
	if request.method == "POST":
		command = request.form['command'] 
		try:
			exit_command = check_output(command, shell=True)
		except CalledProcessError:
			exit_command = command+" Not Found"
		flash(exit_command)
		return render_template('index.html')

	return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		if check_login():
			login_user(user)
			return redirect('/')
		else:
			flash('You username or password is not invalid', ['danger', 'Error_input:'])
			return render_template("login.html")
	else:
		return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('logout successfuly', ['info', 'Success:'])
	return redirect('/login')


if __name__ == '__main__':
	app.run('0.0.0.0', 5000, debug=True)