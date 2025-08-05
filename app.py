from flask import Flask, request, render_template
import tempfile
import shutil
import os

app = Flask(__name__)

UPLOAD_DIR = 'pictures'

@app.route('/upload', methods=['POST','GET'])
def upload_files():
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    if request.method == 'POST':
        if 'files' not in request.files:
            return 'No files part'
        files = request.files.getlist('files')
        if not files:
            return 'No files selected'
        if files:
            temp_dir = tempfile.mkdtemp()
            for file in files:
                file.save(os.path.join(temp_dir, file.filename))
            # Process the files here
            # You can now save the files or send them back to the client
            for file in files:
                shutil.copy(os.path.join(temp_dir, file.filename), UPLOAD_DIR)
            shutil.rmtree(temp_dir)
            return 'Files uploaded successfully'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()