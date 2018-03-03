from flask import Flask, render_template, flash, request, session, url_for, redirect

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main():
	#return render_template('Home.html')
	return render_template('index.html')

@app.route("/register.html", methods=["GET", "POST"])
def register():
	#Register user - puts data in users.csv
	if request.method == "POST     ":
		main()
		users = open("users.csv", a)
		users.write(session["email"], session["password"])
		Home()
	else:
		return render_template('register.html')



@app.route("/login.html", methods =["GET", "POST"])
def login():
		#Log user in with valid login credentials
	return None

@app.route("/Home.html", methods = ["GET"])
def Home():
	return render_template('Home.html')


if __name__ == "__main__":
     app.run()

