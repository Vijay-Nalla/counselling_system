from flask import Flask, request, jsonify
from risk_predictor import predict_risk

app = Flask(__name__)

@app.route('/api/risk', methods=['POST'])
def risk():
    student_data = request.json
    result = predict_risk(student_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
