from flask import Flask, render_template, url_for
from employees import employees_data

# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="Home")


# about page
@app.route("/about")
def about():
	return render_template("about.html", title="About")


# employees page
@app.route("/employees")
def employees():
	return render_template(
		"employees.html",
		title="Employees",
		emps=employees_data
    )


# managers page
@app.route("/employees/managers")
def managers():
	return render_template(
		"managers.html",
		title="Managers",
		emps=employees_data
    )


# demonstrating if-else with jinja
@app.route("/evaluate/<int:num>")
def evaluate(num):
	return render_template(
		"evaluate.html",
		title="Evaluate",
		number=num
    )


# start the app
if __name__ == "__main__":
	app.run(debug=True)




# The jinja filters:

| Filter  | Description                                                  | Example       |                           |
| ------- | ------------------------------------------------------------ | ------------- | ------------------------- |
| upper   | Converts text to uppercase                                   | "alice"       | upper → "ALICE"           |
| lower   | Converts text to lowercase                                   | "Alice"       | lower → "alice"           |
| title   | Capitalizes the first letter of each word                    | "hello world" | title → "Hello World"     |
| length  | Gets the number of items in a list or characters in a string | "apple"       | length → 5                |
| default | Sets a fallback value if the variable is None/empty          | none          | default("N/A") → "N/A"    |
| join    | Joins items in a list with a separator                       | ["a", "b"]    | join(", ") → "a, b"       |
| replace | Replaces part of a string                                    | "hello"       | replace("h", "y") → "yello" |
| date    | Formats a datetime object                                    | now           | date("Y-m-d")             |
| safe    | Prevents Jinja from escaping HTML                            | <b>Hello</b>  | safe → <b>Hello</b>       |


<p>Username: {{ username|upper }}</p>

<p>Username: ALICE</p>
