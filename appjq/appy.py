from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    
    html_raw ="""<html>
    <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    </head>
    <body>
    <div id="res"></div>
    </body>
    </html>
    """
    
    return html_raw
    
if __name__ == "__main__":
    app.run()