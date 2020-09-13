let editor = document.getElementById("editor");
let target = document.getElementById("target");
let startButton = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;
let typingTimer;
let typing = false;
let stylesheet = document.documentElement.appendChild(document.createElement("style")).sheet;
let textName = document.getElementById("textName");
let textNameText = textName.innerHTML;
let textNameWidth = textName.clientWidth;


function updateTextNameAnimation() {
    let textNameFieldWidth = document.getElementById("textNameField").width;
    if (textNameWidth <= textNameFieldWidth) {
        textName.style.animationName = "";
        textName.innerHTML = textNameText;
        return;
    }
    textName.innerHTML = (textNameText + "&nbsp;".repeat(8)).repeat(2);
    widthText = textName.clientWidth / 2;
    var rule = ` example {
        0% { left: 0px; }
        15% { left: 0px; }
        100% { left: ${-widthText}px; }
    }`;
    if (CSSRule.KEYFRAMES_RULE)
        rule = "@keyframes" + rule;
    else 
        rule = "@-webkit-keyframes" + rule;
    stylesheet.insertRule(rule, stylesheet.cssRules.length);
    textName.style.animationName = "example";
    textName.style.animationDuration = (widthText / 60) + 's';
}


function time2secs(tm) {
    return (tm / 1000).toFixed(1);
}


function showTypingTimer() {
    if (typeof startTime == "undefined")
        return;
    var tm = time2secs(new Date() - startTime);
    status.innerHTML = "You type: " + tm + "s";
} 


window.onload = function() {
    target.value = targetText;
    updateTextNameAnimation();
}


window.onresize = function() {
    updateTextNameAnimation();
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

function checkModKeys(e, ...keys) {
  if (keys.includes('ctrl') != e.ctrlKey)
    return false;
  if (keys.includes('shift') != e.shiftKey)
    return false;
  if (keys.includes('alt') != e.altKey)
    return false;
  if (keys.includes('meta') != e.metaKey)
    return false;
  return true;
}

window.onkeydown = function(e) {
  if (checkModKeys(e, 'ctrl') && e.keyCode == 13) { // Ctrl+Enter
    startButton.onclick();
  }
}


