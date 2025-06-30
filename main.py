from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    op = data.get('operation')
    a = data.get('a')
    b = data.get('b')

    try:
        if op == 'add':
            result = calc.add(a, b)
        elif op == 'subtract':
            result = calc.subtract(a, b)
        elif op == 'multiply':
            result = calc.multiply(a, b)
        elif op == 'divide':
            result = calc.divide(a, b)
        elif op == 'power':
            result = calc.power(a, b)
        elif op == 'sqrt':
            result = calc.sqrt(a)
        else:
            return jsonify({"error": "Nieznana operacja"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
