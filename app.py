from flask import Flask, render_template, request
from scanner.network_scanner import NetworkScanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        network_range = request.form.get('network_range')
        scanner = NetworkScanner(network_range)
        scanner.scan()
        results = scanner.process_results()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
