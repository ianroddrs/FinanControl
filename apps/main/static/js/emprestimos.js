new ClipboardJS('#copy-code');
var copyCodeElement = document.getElementById('copy-code');
copyCodeElement.addEventListener('click', function () {
    copyCodeElement.innerHTML = 'Copiado';
    setTimeout(function () {
        copyCodeElement.innerHTML = 'Copiar código do QR Code';
    }, 1000);
});