from flask import *

from pickle import *

app = Flask(__name__)
app.secret_key = "created_by_vedant"
@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		f = open("model.pkl", "rb")
		model = load(f)
		f.close()   
		f = open("mms.pkl", "rb")
		mms = load(f)
		f.close()
		try:
			if request.method == "POST":
				# gender = float(request.form["gender"])
				age = float(request.form["age"])
				annual_income = float(request.form["annual_income"])
				spending_score = float(request.form["spending_score"])
				d = [[age, annual_income, spending_score]]
				mmsd = mms.transform(d)
				ans = model.predict(mmsd)
				if ans == 0:
					msg = "Older, High Income, Moderate Spending"
				elif ans == 1:
					msg = "Middle-Aged, High Income, Moderate Spending"
				elif ans== 2:
					msg = "Young, High Income, Moderate Spending"
				elif ans == 3:
					msg = "Middle-Aged, High Income, Low Spending"
				elif ans==4:
					msg = "Young, Moderate Income, High Spending"
				elif ans == 5:
					msg = "Young, Low Income, High Spending"
				elif ans == 6:
					msg = "Middle-Aged, Low Income, Low Spending"
				elif ans == 7:
					msg = "Middle-Aged, Low Income, High Spending"
				elif ans == 8:
					msg = "Middle-Aged, High Income, Low Spending"
				elif ans == 9:
					msg = "Middle-Aged, Moderate Income, Moderate Spending"
				elif ans == 10:
					msg = "Older, Moderate Income, Low Spending"
				elif ans == 11:
					msg = "Young, High Income, Low Spending"
				elif ans == 12:
					msg = "Middle-Aged, High Income, Moderate Spending"
				elif ans == 13:
					msg = "Middle-Aged, Moderate Income, Low Spending"
				else:
					msg = "Older, High Income, Low Spending"
				msg = "Belongs to : " + str(msg)

			return render_template("home.html", msg=msg)
		except Exception as e:
			msg = "Issue " + str(e)
			return render_template("home.html", msg = msg)
	return render_template("home.html")



if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
