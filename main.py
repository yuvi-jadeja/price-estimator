from flask import Flask, request, render_template
from validator import is_number
import utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    data = {
        "locations": utils.getLocationNames(),
        "price": ""
    }

    if request.method == "POST":
        try:
            sqft = request.form.get('Squareft')
            uiBHK = request.form.get('uiBHK')
            uiBathrooms = request.form.get('uiBathrooms')
            location = request.form.get('location')

            if is_number(sqft) or is_number(uiBHK) or is_number(uiBathrooms) or location == None:
                data = {
                    "locations": utils.getLocationNames(),
                    "price": "Invalid input!"
                }
            else:
                data = {
                    "locations": utils.getLocationNames(),
                    "price": utils.getEstimatedPrice(location, sqft, uiBathrooms, uiBHK)
                }
        except ValueError as e:
            data = {
                "locations": utils.getLocationNames(),
                "price": "Invalid input!"
            }
        except Exception as e:
            data = {
                "locations": utils.getLocationNames(),
                "price": "Something went wrong!"
            }

    return render_template('index.html', data=data)


if __name__ == "__main__":
    utils.loadSavedData()
    print("Starting Server for Realt Estate Price Estimate...")
    app.run(host="0.0.0.0", port=5000)
