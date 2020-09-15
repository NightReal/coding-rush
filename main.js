let editor = document.getElementById("editor");
let target = document.getElementById("target");
let startButton = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let startTime = undefined;
let typingTimer;
let stylesheet = document.getElementById("dynamic-style").sheet;
let textName = document.getElementById("textName");
let textNameText = textName.innerHTML;
let textNameWidth = textName.clientWidth;
let tooltipsl = document.querySelectorAll('.tooltip .tooltiptext-l');
let tooltipsr = document.querySelectorAll('.tooltip .tooltiptext-r');
let lastTextValue = "";


function updateTextNameAnimation() {
    var textNameFieldWidth = document.getElementById("textNameField").offsetWidth;
    if (textNameWidth <= textNameFieldWidth) {
        textName.style.animationName = "";
        textName.innerHTML = textNameText;
        return;
    }
    textName.innerHTML = (textNameText + "&nbsp;".repeat(8)).repeat(2);
    widthText = textName.clientWidth / 2;
    var t1 = 2, t2 = widthText / 60;
    var rule = ` example {
        0% { left: 0px; }
        ${t1 / (t1 + t2) * 100}% { left: 0px; }
        100% { left: ${-widthText}px; }
    }`;
    if (CSSRule.KEYFRAMES_RULE)
        rule = "@keyframes" + rule;
    else 
        rule = "@-webkit-keyframes" + rule;
    stylesheet.insertRule(rule, stylesheet.cssRules.length);
    textName.style.animationName = "example";
    textName.style.animationDuration = (t1 + t2) + 's';
}


function time2secs(tm) {
    return (tm / 1000).toFixed(1);
}


function showTypingTimer() {
    if (!typing())
        return;
    var tm = time2secs(new Date() - startTime);
    status.innerHTML = "You type: " + tm + "s";
} 


window.onload = function() {
    target.value = targetText;
    editor.focus();
    updateTextNameAnimation();
}


window.onresize = function() {
    updateTextNameAnimation();
}

function getRevVisibility(vis) {
  if (vis == "hidden")
    return "visible";
  return "hidden";
}

function switchVisibility(element) {
    element.style.visibility = getRevVisibility(element.style.visibility);
}

function typing() {
    return startTime !== undefined;
}

function startStopTyping(opts={'rightText' : false, 'defText' : ''}) {
    startButton.classList.toggle('darkred-btn');
    startButton.classList.toggle('green-btn');
    switchVisibility(document.getElementById("startButtonTooltip"));
    switchVisibility(document.getElementById("stopButtonTooltip"));
    //editor.readOnly ^= true;
    if (typing()) {
        startButton.innerHTML = "Start";
        clearInterval(typingTimer);
        if (!opts.rightText)
            status.innerHTML = "You stopped typing.";
        else {
            var tm = time2secs(new Date() - startTime);
            status.innerHTML = "Done! Your time: " + tm + "s";
        }
        startTime = undefined;
    } else {
        startButton.innerHTML = "Stop";
        editor.value = opts.defText;
        startTime = new Date();
        showTypingTimer();
        typingTimer = setInterval(showTypingTimer, 100);
        editor.focus();
    }
    lastTextValue = editor.value;
}

startButton.onclick = function(e) {
    startStopTyping();
}


editor.oninput = function(e) {
    if (e.inputType == "insertFromPaste") {
        editor.value = lastTextValue;
        return;
    }
    if (!typing()) {
        if (e.data == null) {
            editor.value = "";
        } else {
            startStopTyping({defText: e.data});
        }
    }
    if (editor.value == targetText) {
        startStopTyping({rightText: true});
    }
    lastTextValue = editor.value;
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
    startStopTyping();
  }
}

window.onmousemove = function(e, kek=false) {
    var x = e.clientX;
    var y = e.clientY;
    for (var i = 0; i < tooltipsl.length; i++) {
        var tt = tooltipsl[i];
        if (getComputedStyle(tt).display != "none") {
            tt.style.left = x - tt.offsetWidth + 'px';
            tt.style.top = y + 'px';
        }
    }
    for (var i = 0; i < tooltipsr.length; i++) {
        var tt = tooltipsr[i];
        if (getComputedStyle(tt).display != "none") {
            tt.style.left = x + 'px';
            tt.style.top = y + 'px';
        }
    }
};


