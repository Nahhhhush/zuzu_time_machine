from flask import Flask, render_template, url_for
import os
import datetime

app = Flask(__name__)

# List of Zuzu's photos and their captions
def get_zuzu_photos():
    photos = []
    for filename in os.listdir('static'):
        if filename.startswith('zuzu') and filename.endswith('.jpg'):
            caption = filename.replace('zuzu-', '').replace('.jpg', '').replace('-', ' ').title()
            photos.append({'filename': filename, 'caption': f'Zuzu, {caption}'})
    return photos

@app.route('/')
def index():
    current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    photos = get_zuzu_photos()
    return render_template('index.html', photos=photos, current_date_time=current_date_time)

@app.route('/travel_to_past/<int:index>')
def travel_to_past(index):
    current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    photos = get_zuzu_photos()
    if index < 0 or index >= len(photos):
        index = 0
    return render_template('index.html', photos=photos, current_date_time=current_date_time, index=index)

if __name__ == '__main__':
    app.run(debug=True)