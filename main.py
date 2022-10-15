from dataclasses import fields
from flask import Flask, request
from g_drive_service import GoogleDriveService

app=Flask(__name__)


service=GoogleDriveService().build()

@app.get('/all-files')
def get_all_files():
    pass



@app.get('/files-with-id/<file_id>/')
def get_files_with_id(file_id):
    pass

@app.get('/files-in-folder/<folder_id>/')
def get_files_in_folder(folder_id):
    pass

@app.get('/files-with-type')
def get_files_with_type():
    pass


@app.get('/files-with-limit-offset')
def get_files_with_limit_offset():
    pass


@app.get('/files-with-limit-offset-order')
def get_files_with_limit_offset_order():
    pass


if __name__=='__main__':
    app.run(debug=True, port=8000)