from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session handling

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ayyoubberoiguii@hotmail.com'  # Update this
app.config['MAIL_PASSWORD'] = 'ayyoubbeg123'    # Update this
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        service = request.form['service']
        period = request.form['period']
        email = request.form['email']
        description = request.form['description']
        
        # Save data in session for retrieval after payment
        session['order_data'] = {
            'service': service,
            'period': period,
            'email': email,
            'description': description
        }

        return redirect(url_for('payment'))

    return render_template('index.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/confirm_payment')
def confirm_payment():
    order_data = session.get('order_data')
    if order_data:
        msg = Message('New Order: Netflix/Spotify Account',
                      sender='ayyoubberoiguii@hotmail.com', recipients=['ayyoubberoiguii@hotmail.com'])
        msg.body = f"Service: {order_data['service']}\nPeriod: {order_data['period']}\nEmail: {order_data['email']}\nDescription: {order_data['description']}"
        mail.send(msg)
        
    return "Thank you! Your order has been processed."

if __name__ == '__main__':
     # Use the port from the PORT environment variable, or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
