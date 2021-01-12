from flask import Flask, render_template
import os

#The Flask object constructor takes arguments
app = Flask(__name__)

#Removes caching, hard reset every refresh.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Landing page
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

'''
If we are running from this file
If this is a windows OS
    Run default localhost on port 5000
If this is Mac or Linux/other
    Run open to the internet on port 80
    
Both of these will have multiple threads
'''
if __name__ == '__main__':
    if "win" in os.sys.platform:
        app.run(threaded=True, port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', threaded=True, port=80, debug=False)