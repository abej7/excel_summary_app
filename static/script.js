const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file');
const form = document.getElementById('upload-form');
const loading = document.getElementById('loading');
const fileName = document.getElementById('file-name');

// ドラッグ＆ドロップ処理
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length) {
        fileInput.files = files;
        fileName.textContent = files[0].name;
    }
});

// ファイル選択時のファイル名表示
fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
    } else {
        fileName.textContent = '選択されていません';
    }
});

// フォーム送信時にローディング表示
form.addEventListener('submit', () => {
    loading.style.display = 'block';
});
