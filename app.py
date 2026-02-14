from flask import Flask, render_template, request
from gemini_ai import generate_sql
from sql_executor import execute_query

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""
    sql = ""

    if request.method == "POST":

        user_input = request.form["query"]

        sql = generate_sql(user_input)

        result = execute_query(sql)

    return render_template("index.html",
                           result=result,
                           sql=sql)


if __name__ == "__main__":
    app.run(debug=True)