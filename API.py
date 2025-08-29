from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

    response = {
        "is_success": True,
        "user_id": user_id,
        "email" : email,
        "roll_number": roll_no,
        "odd_numbers": oddArr,
        "even_numbers": evenArr,
        "alphabets": alpArr,
        "special_characters": specialArr,
        "sum": str(sumNum),
        "concat_string": concat
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
