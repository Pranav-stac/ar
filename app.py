from flask import Flask, render_template, request, url_for, redirect, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['QR_FOLDER'] = 'static/qrcodes'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm'}

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QR_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        try:
            # Clear previous uploads
            for filename in os.listdir(app.config['UPLOAD_FOLDER']):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Use fixed QR code
            return render_template('qr_display.html', qr_code='final.png')
        except Exception as e:
            print(f"Error in upload: {str(e)}")
            return redirect(request.url)

@app.route('/ar')
def ar_view():
    try:
        # Get the uploaded file (if any)
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        uploaded_file = files[0] if files else None
        return render_template('ar.html', media_file=uploaded_file)
    except Exception as e:
        print(f"Error in AR view: {str(e)}")
        return "Error loading AR view", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')