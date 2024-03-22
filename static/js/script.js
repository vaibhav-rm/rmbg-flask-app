const dropArea = document.getElementById('dropArea');
const fileInput = document.getElementById('fileInput');
const uploadForm = document.getElementById('uploadForm');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    document.addEventListener(eventName, preventDefaults, false)
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    document.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    document.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
    dropArea.classList.add('highlight');
}

function unhighlight(e) {
    dropArea.classList.remove('highlight');
}

document.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    fileInput.files = files;
    uploadForm.submit(); // Submit the form after files are dropped
}