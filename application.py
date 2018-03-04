from flask import Flask, render_template, flash, request, session, url_for, redirect

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
		users.write(request.form.get("email"))
		passwords.write(request.form.get("password"))
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
	txt = info.readlines()
	info.close()
	top5 = []

	i = 0
	while i < 5:
		l = txt[i].split(',')
		top5.append(l)
		i+=1

	return render_template('Home.html', top5 = top5)


if __name__ == "__main__":
     app.run()

