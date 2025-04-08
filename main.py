from flask import Flask, render_template_string

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template_string("""
        <html>
            <head>
                <title>Welcome to DevOps World 🌍</title>
                <style>
                    body { 
                        background-color: #f0f8ff; 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        padding-top: 50px;
                    }
                    h1 {
                        color: #007BFF;
                    }
                    p {
                        color: #333;
                        font-size: 20px;
                    }
                </style>
            </head>
            <body>
                <h1>Hello, DevOps World! 🚀</h1>
                <p>Welcome to Flask app.</p>
                <p>Click <a href="/about">here</a> to learn more!</p>
            </body>
        </html>
    """)

# About Route
@app.route('/about')
def about():
    return render_template_string("""
        <html>
            <head>
                <title>About Us - DevOps World 🌍</title>
                <style>
                    body { 
                        background-color: #fff0f5; 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        padding-top: 50px;
                    }
                    h1 {
                        color: #e83e8c;
                    }
                    p {
                        color: #555;
                        font-size: 18px;
                    }
                </style>
            </head>
            <body>
                <h1>About This App 📜</h1>
                <p>This is a simple Python Flask app built for DevOps practice!</p>
                <p><a href="/">Back to Home</a></p>
            </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
