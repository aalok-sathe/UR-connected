from flask import Flask, render_template, flash, request, session, url_for, redirect

from forum import FacilitiesForum

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
	#return render_template('Home.html')
	return render_template('index.html')

@app.route("/register.html", methods=["GET", "POST"])
def register():
	#Register user - puts data in users.csv
	if request.method == "POST":
		users = open("users.csv", "a")
		passwords = open("passwords.csv", "a")
		users.write(request.form.get("email") + "\n")
		passwords.write(request.form.get("password") + "\n")
		users.close()
		passwords.close()
		return Home()
	else:
		return render_template('register.html')



@app.route("/login.html", methods =["GET", "POST"])
def login():
		#Log user in with valid login credentials
	return ("You're logged in")

@app.route("/Home.html", methods = ["GET"])
def Home():
	info = open("d.csv","r")
	txt = info.readlines()[0:5]
	info.close()
	top5 = []

	for line in txt:
		l = line.split(',')
		top5.append(l)

	return render_template('Home.html', top5 = top5)


if __name__ == "__main__":
     app.run()

