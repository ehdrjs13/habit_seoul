from flask import Flask, request, send_from_directory
from core.upload import Uploader

app = Flask(__name__)
uploader = Uploader()

@app.route('/setup', methods=['GET']) 
def setup(): 
    file_path = uploader.setFilePath()

    return 

@app.route('/upload', methods=['POST'])
def upload():
    

@app.route('/testify', methods=['POST'])
def testify():

    return


@app.route('/sendrank')
def sendrank():

    return



