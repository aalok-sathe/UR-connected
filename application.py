from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	#return render_template('Home.html')
	return render_template('index.html')
@app.route("/register", methods=["GET", "POST"])
def register():
	#Register user - puts data in users.csv
		if request.method == "POST":
			users = open("users.csv", a)
			users.write(session["email"], session["password"])
		else:
			return render_template("register.html")



@app.route("/login", methods =["GET", "POST"])
def login():
		#Log user in with valid login credentials
	return None

if __name__ == "__main__":
     app.run()