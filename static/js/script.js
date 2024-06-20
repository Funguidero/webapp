document.addEventListener('DOMContentLoaded', function() {
    var input = document.getElementById('imageInput');
    if (input) {
        input.addEventListener('change', handleFileUpload);
    }
});

function handleFileUpload() {
    var input = document.getElementById('imageInput');
    var fileLoadedContainer = document.querySelector('.file-loaded');
    var fileUnloadedContainer = document.querySelector('.file-unloaded');
    var fileNameSpan = document.getElementById('fileName');
    if (input.files && input.files[0]) {
        var file = input.files[0];
        fileNameSpan.textContent = file.name;
        fileLoadedContainer.classList.remove('hidden');
        fileUnloadedContainer.classList.add('hidden');
    }
}

function removeFile() {
    var input = document.getElementById('imageInput');
    var fileLoadedContainer = document.querySelector('.file-loaded');
    var fileUnloadedContainer = document.querySelector('.file-unloaded');
    var fileNameSpan = document.getElementById('fileName');
    input.value = '';
    fileNameSpan.textContent = '';
    fileLoadedContainer.classList.add('hidden');
    fileUnloadedContainer.classList.remove('hidden');
}
