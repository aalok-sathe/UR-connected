from flask import *

app = Flask(__name__)

@app.route("/")

@app.route("/register", methods=["GET", "POST"])
def register():
	#Register user - puts data in users.csv
		if request.method == "POST":
			users = open("users.csv", a)
			users.write(session["email"], session["password"])
		else:
			render_template("homepage.html")



@app.route("/login", methods =["GET", "POST"])
def login():
		#Log user in with valid login credentials
	return Null

if __name__ == "__main__":
    app.run()