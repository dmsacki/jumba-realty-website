from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically save the data to a database or send it via email
    print(f"Received message from {name} ({email}): {message}")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
