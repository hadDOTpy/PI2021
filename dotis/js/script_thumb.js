// Script para "transformar" o file em um botão
const $ = document.querySelector.bind(document);
const previewImg = $('#preview-img');
const fileChooser = $('#arquivo');
const fileButton = $('#imagem');

fileButton.onclick = () => fileChooser.click();

fileChooser.onchange = e => {
    const fileToUpload = e.target.files.item(0);
    const reader = new FileReader();
    reader.onload = e => previewImg.src = e.target.result;
    reader.readAsDataURL(fileToUpload);
};