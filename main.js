let editor = document.getElementById("editor");
let target = document.getElementById("target");
let button = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;

window.onload = function() {
    target.value = targetText;
};


button.onclick = function() {
    startTime = new Date();
    editor.value = "";
    status.innerHTML = "Now type";
    editor.focus();
    editor.readOnly = false;
}


editor.oninput = function() {
    if (editor.value == targetText) {
        status.innerHTML = "Done, your time: " + Math.abs(new Date() - startTime) / 1000.0 + "s";
        startTime = undefined;
        editor.readOnly = true;
    }
};


target.oncopy = function(event) {
    event.preventDefault();
};


deselect = function() {
  if (window.getSelection) {
      if (window.getSelection().empty) {  // Chrome
        window.getSelection().empty();
      } else if (window.getSelection().removeAllRanges) {  // Firefox
        window.getSelection().removeAllRanges();
      }
    } else if (document.selection) {  // IE?
      document.selection.empty();
    }
}

target.onselect = deselct;
