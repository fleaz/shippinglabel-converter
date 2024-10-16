import os
from bottle import route, request, static_file, run, redirect, HTTPResponse, hook
from random import randint
from os import remove

from convert import convert_dhl

@route('/')
def root():
    return static_file('index.html', root='templates')

@route('/dhl', method='POST')
def do_upload():
    upload = request.files.get('upload')
    if upload.content_type != "application/pdf":
        return HTTPResponse(status=400, body="Bad file")

    id = randint(100000,999999)
    upload.save(f"./uploads/{id}.pdf")
    convert_dhl(id)
    print(f"converted {upload.filename} as {id}.pdf")
    # delete upload file
    remove(f"./uploads/{id}.pdf")

    return redirect(f"/download/{id}")

@route('/download/<id>')
def download(id):
    filename = f"{id}.pdf"
    return static_file(filename, root='downloads', download=filename)

@hook('after_request')
def delFiles():
    if request.path.startswith("/download/"):
        id = request.path.split("/")[2]
        try:
             remove(f"./downloads/{id}.pdf")
        except FileNotFoundError:
            return

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

if __name__ == '__main__':
    for p in ['./uploads', './downloads']:
        if not os.path.exists(p):
            os.makedirs(p)
    run(host='0.0.0.0', port=8080)
