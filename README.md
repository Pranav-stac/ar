# Dynamic AR Content Viewer

This is a Flask-based web application that allows users to upload images or videos and view them in AR using pattern markers.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have your pattern marker file (`ok.patt`) in the `static` directory.

3. Run the application:
```bash
python app.py
```

The application will run on HTTPS (required for AR.js) at https://localhost:5000

## Usage

1. Open the application in your browser
2. Upload an image or video file using the upload form
3. Click "View AR Experience" to open the AR viewer
4. Point your camera at the pattern marker to see the uploaded content in AR

## Supported File Types

- Images: PNG, JPG, JPEG, GIF
- Videos: MP4, WEBM

## Notes

- The application requires HTTPS to access the camera
- Only one file can be active at a time - uploading a new file will replace the previous one
- Maximum file size is 16MB 