let editor = document.getElementById("editor");
let need = document.getElementById("need");
let button = document.getElementById("startButton");
let needText = "Hello, world!";
let status = document.getElementById("status");

window.onload = function() {
    need.value = needText;
};

let startTime = undefined;

button.onclick = function() {
    startTime = new Date();
    editor.value = "";
    status.innerHTML = "Now type";
    editor.focus();
    editor.readOnly = false;
}

editor.oninput = function() {
    if (editor.value == needText) {
        status.innerHTML = "Done, your time: " + Math.abs(new Date() - startTime) / 1000.0;
        startTime = undefined;
        editor.readOnly = true;
    }
};
