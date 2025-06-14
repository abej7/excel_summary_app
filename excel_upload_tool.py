from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

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

            # Excelファイル読み込み
            df = pd.read_excel(filepath)

            # 実用的な加工（ここでは "合計" 列を追加する例）
            if '数量' in df.columns and '単価' in df.columns:
                df['合計'] = df['数量'] * df['単価']

            output_path = os.path.join(OUTPUT_FOLDER, f"processed_{filename}")
            df.to_excel(output_path, index=False)

            return send_file(output_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
