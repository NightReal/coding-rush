let editor = document.getElementById("editor");
let target = document.getElementById("target");
let startButton = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;
let typingTimer;
let typing = false;


window.onload = function() {
    target.value = targetText;
};


function time2secs(tm) {
    return (tm / 1000).toFixed(1);
}


function showTypingTimer() {
    if (typeof startTime == "undefined")
        return;
    var tm = time2secs(new Date() - startTime);
    status.innerHTML = "You type: " + tm + "s";
} 

startButton.onclick = function(e, rightText=false) {
    startButton.classList.toggle('darkred-btn');
    startButton.classList.toggle('green-btn');
    editor.readOnly ^= true;
    if (typing) {
        startButton.innerHTML = "Start";
        clearInterval(typingTimer);
        if (!rightText)
            status.innerHTML = "You stopped typing.";
        else {
            var tm = time2secs(new Date() - startTime);
            status.innerHTML = "Done! Your time: " + tm + "s";
        }
        startTime = undefined;
    } else {
        startButton.innerHTML = "Stop";
        editor.value = "";
        startTime = new Date();
        showTypingTimer();
        typingTimer = setInterval(showTypingTimer, 100);
        editor.focus();
    }
    typing ^= true;
}



editor.oninput = function(e) {
    if (editor.value == targetText) {
        startButton.onclick(e, rightText=true);
    }
};


target.oncopy = function(event) {
    event.preventDefault();
};


target.onselect = function() { // deselect
  target.selectionStart = target.selectionEnd;
};

