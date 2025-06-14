from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Excel 処理
            df = pd.read_excel(filepath)
            output_path = os.path.join(OUTPUT_FOLDER, 'summary.xlsx')

            print("読み込み成功？", df.head())
            print("出力先:", output_path)

            df.to_excel(output_path, index=False)
            print("Excel保存完了")

            # 完了メッセージ
            flash("処理完了…下のボタンからダウンロードしてください！")
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/download')
def download():
    output_path = os.path.join(OUTPUT_FOLDER, 'summary.xlsx')
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)