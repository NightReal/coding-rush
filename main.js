let editor = document.getElementById("editor");
let target = document.getElementById("target");
let button = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;
let typingTimer;


function time2secs(tm) {
  return (tm / 1000).toFixed(1);
}


function showTypingTimer() {
  if (typeof startTime == "undefined") {
      return;
  }
  var tm = time2secs(new Date() - startTime);
  status.innerHTML = "You type: " + tm + "s";
} 


window.onload = function() {
    target.value = targetText;
};


button.onclick = function() {
    editor.value = "";
    startTime = new Date();
    showTypingTimer();
    typingTimer = setInterval(showTypingTimer, 100);
    editor.readOnly = false;
    editor.focus();
}


editor.oninput = function() {
    if (editor.value == targetText) {
        clearInterval(typingTimer);
        status.innerHTML = "Done! Your time: " + time2secs(new Date() - startTime) + "s";
        startTime = undefined;
        editor.readOnly = true;
    }
};


target.oncopy = function(event) {
    event.preventDefault();
};


target.onselect = function() { // deselect
  if (window.getSelection) {
      if (window.getSelection().empty) {  // Chrome
        window.getSelection().empty();
      } else if (window.getSelection().removeAllRanges) {  // Firefox
        window.getSelection().removeAllRanges();
      }
    } else if (document.selection) {  // IE?
      document.selection.empty();
    }
};

