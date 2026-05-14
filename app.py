from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Days to hours converter is running! Use POST /convert to make a request"

calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json.get("days", [])
    results = []
    for item in data:
        try:
            num = int(item)
            if num > 0:
                results.append(days_to_units(num))
            elif num == 0:
                results.append("Zero is invalid")
            else:
                results.append(f"{num} is negative — no conversion")
        except ValueError:
            results.append(f"{item} is not a valid number")
    return jsonify(results=results)

if __name__ == "__main__":
    app.run()
