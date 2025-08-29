from flask import Flask, request, Response
from collections import OrderedDict
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

def ProcessNumbers(arr):
    even = []
    odd = []
    sum = 0

    for num in arr:
        if num.isdigit():
            if int(num) % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
            sum += int(num)
    
    return even, odd, sum

def processAlphabhet(arr):
    alp = []
    special = []
    concat, i = "", 0

    for char in arr:
        if char.isalpha():
            alp.append(char.upper())
        elif not char.isalnum():
            special.append(char)
    
    for char in alp[::-1]:
        if i % 2 == 0:
            concat += char.upper()
        else:
            concat += char.lower()
        i += 1
    
    return alp, special, concat

@app.route("/bfhl", methods=['POST'])
def home():
    req = request.get_json()
    data = req.get("data", [])

    evenArr , oddArr, sumNum = ProcessNumbers(data)
    alpArr, specialArr, concat = processAlphabhet(data)
    user_id = "navinkumar_23082004"
    roll_no = "22BCE1020"
    email = "omnavinyogesh.icc@gmail.com"

    response = OrderedDict()
    response["is_success"] = True
    response["user_id"] = user_id
    response["email"] = email
    response["roll_number"] = roll_no
    response["odd_numbers"] = oddArr
    response["even_numbers"] = evenArr
    response["alphabets"] = alpArr
    response["special_characters"] = specialArr
    response["sum"] = str(sumNum)
    response["concat_string"] = concat

    return Response(
        json.dumps(response),
        status=200,
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run()

