from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables to store the counter and the reset prime
counter = 0
reset_prime = 2

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    """Find the next prime number after n."""
    next_n = n + 1
    while not is_prime(next_n):
        next_n += 1
    return next_n

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/counter', methods=['GET', 'POST'])
def counter_page():
    """Render the counter page and handle counter logic."""
    global counter, reset_prime
    if request.method == 'POST':
        counter += 1
        if counter >= reset_prime:
            counter = 0
            reset_prime = next_prime(reset_prime)
        return redirect(url_for('counter_page'))
    return render_template('counter.html', counter=counter, reset_prime=reset_prime)

if __name__ == '__main__':
    app.run(debug=True)
