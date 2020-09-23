let editor = document.getElementById("editor");
let target = document.getElementById("target");
let startButton = document.getElementById("startButton");
let targetText = "Hello, world!";
let status = document.getElementById("status");
let speed = document.getElementById("speed");
let timepass = document.getElementById("timepass");
let startTime = undefined;
let header = document.getElementsByTagName("header")[0];
let footer = document.getElementsByTagName("footer")[0];
let body = document.getElementsByTagName("body")[0];
let typingTimer = undefined;
let stylesheet = document.getElementById("dynamic-style").sheet;
let textName = document.getElementById("textName");
let textNameText = textName.innerHTML;
let textNameWidth = textName.clientWidth;
let tooltipsl = document.querySelectorAll('.tooltip .tooltiptext-l');
let tooltipsr = document.querySelectorAll('.tooltip .tooltiptext-r');
let tooltips = document.querySelectorAll('.tooltip .tooltiptext-l, .tooltip .tooltiptext-r');
let lastTextValue = "";
let resizeTimer = undefined;
let tooltipButton = document.getElementById("tooltipButton");
let tooltipsEnabled = true;
let typeInfo = document.getElementById("typeInfo");


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
    var t = new Date() - startTime;
    var tm = time2secs(t);
    timepass.innerHTML = tm;
    if (Math.round(t / 100) % 4 != 0)
        return;
    var v = 0;
    if (tm > 0)
      v = Math.round(editor.value.length * 1000 * 60 / t);
    speed.innerHTML = v;
} 


window.onload = function() {
    target.value = targetText;
    editor.focus();
    updateTextNameAnimation();
    window.onresize();
    editor.style.height = getComputedStyle(editor).height;
    target.style.height = getComputedStyle(target).height;
    footer.style.display = "block";
}


window.onresize = function() {
    updateTextNameAnimation();
    updateFooterPosition(true);
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
        typingTimer = undefined;
        if (!opts.rightText)
            status.innerHTML = "You stopped typing.";
        else {
            var t = new Date() - startTime;
            timepass.innerHTML = time2secs(t);
            speed.innerHTML = Math.round(editor.value.length * 1000 * 60 / t);
            status.innerHTML = "You finished typing.";
        }
        startTime = undefined;
    } else {
        startButton.innerHTML = "Stop";
        editor.value = opts.defText;
        startTime = new Date();
        showTypingTimer();
        typingTimer = setInterval(showTypingTimer, 100);
        editor.focus();
        status.innerHTML = "You typing now.";
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
    var char = e.data;
    if (e.inputType == "insertLineBreak") {
        char = '\n';
    }
    if (!typing()) {
        if (char === null) {
            editor.value = "";
        } else {
            startStopTyping({defText: char});
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

let mouseX, mouseY;

window.onmousemove = function(e) {
    if (!tooltipsEnabled)
        return;
    var x = e.pageX;
    var y = e.pageY;
    mouseX = x;
    mouseY = y;
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

function smartScroll(x, y) {
  var w = window.innerWidth, h = window.innerHeight;
  var x0 = window.scrollX, y0 = window.scrollY;
  var x1 = w + x0, y1 = h + y0;
  var a = x0, b = y0;
  if (x < x0)
      a = x;
  if (x > x1)
      a = x - w;
  if (y < y0)
      b = y;
  if (y > y1)
      b = y - h;
  window.scrollTo(a, b);
}

function updateFooterPosition(windowResize) {
  var he = typeInfo.offsetTop + typeInfo.offsetHeight + 30;
  var hf = parseInt(getComputedStyle(footer).height);
  var H = window.innerHeight;
  var l;
  if (he + hf <= H) {
      l = H - hf;
  } else {
      l = he;
  }
  l = l + 'px';
  if (footer.style.top != l) {
      footer.style.top = l;
  }
  if (!windowResize)
      smartScroll(0, he + hf);
}

function updateTextareaHeight() {
    target.style.height = getComputedStyle(editor).height;
    updateFooterPosition(false);
}
function updateTextareaHeightRev() {
    editor.style.height = getComputedStyle(target).height;
    updateFooterPosition(false);
}

function checkNearRightDown(el, kwargs={'eps': 10}) {
    var eps = kwargs['eps']
    var x = el.offsetLeft + el.offsetWidth - eps;
    var y = el.offsetTop + el.offsetHeight - eps;
    if (x - eps > mouseX || mouseX > x + eps)
        return false;
    if (y - eps > mouseY || mouseY > y + eps)
        return false;
    return true;
}

editor.onmousedown = function() {
    if (!checkNearRightDown(editor))
        return;
    resizeTimer = setInterval(updateTextareaHeight, 15);
}
target.onmousedown = function() {
    if (!checkNearRightDown(target))
        return;
    resizeTimer = setInterval(updateTextareaHeightRev, 15);
}

window.onmouseup = function() {
    if (resizeTimer !== undefined) {
        clearInterval(resizeTimer);
        resizeTimer = undefined;
        updateTextareaHeight();
    }
}


tooltipButton.onclick = function() {
    var w = getComputedStyle(tooltipButton).width;
    if (tooltipsEnabled) {
        tooltipButton.innerHTML = "Enable tooltips";
        for (var i = 0; i < tooltips.length; ++i)
            tooltips[i].classList.remove("enabled-tooltip");
            
    } else {
        tooltipButton.innerHTML = "Disable tooltips";
        for (var i = 0; i < tooltips.length; ++i)
            tooltips[i].classList.add("enabled-tooltip");
    }
    tooltipButton.style.width = w;
    tooltipsEnabled ^= true;
}
