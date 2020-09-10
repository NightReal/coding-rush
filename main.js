let editor = document.getElementById("editor");
let target = document.getElementById("target");
let startButton = document.getElementById("startButton");
let stopButton = document.getElementById("stopButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;
let typingTimer;


window.onload = function() {
    target.value = targetText;
};


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


startButton.onclick = function() {
    editor.value = "";
    startTime = new Date();
    showTypingTimer();
    typingTimer = setInterval(showTypingTimer, 100);
    editor.readOnly = false;
    editor.focus();
    stopButton.disabled = false;
}


function endTyping() {
    clearInterval(typingTimer);
    startTime = undefined;
    editor.readOnly = true;
    stopButton.disabled = true;
}


stopButton.onclick = function() {
    status.innerHTML = "You stopped typing.";
    endTyping();
}


editor.oninput = function() {
    if (editor.value == targetText) {
        var tm = time2secs(new Date() - startTime);
        endTyping();
        status.innerHTML = "Done! Your time: " + tm + "s";
    }
};


target.oncopy = function(event) {
    event.preventDefault();
};


target.onselect = function() { // deselect
  target.selectionStart = target.selectionEnd;
};

