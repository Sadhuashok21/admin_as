const strike = document.getElementById('strike');
const superScript = document.getElementById('superscript');

const bold = document.getElementById('bold');
const italic = document.getElementById('italic');
const underline = document.getElementById('underline');


const selection = window.getSelection();
function sel() {

    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const container = document.createElement('div');

        container.appendChild(range.cloneContents());

        console.log(container.innerHTML);
    }
}


function boldApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('bold')
    }
}

function italicApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('italic')
    }
}
function underLineApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('underline')
    }
}


function strikeApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('strikeThrough')
    }
}

function superScriptApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('superscript')
    }
}
function subScriptApply() {
    if (selection.rangeCount > 0) {
        document.execCommand('subscript')
    }
}

function redo() {
    document.execCommand('redo')

}

function undo() {
    document.execCommand('undo')
}

function justifyCenter() {
    if (selection.rangeCount > 0) {
        document.execCommand('justifyCenter')
    }
}


function justifyLeft() {
    if (selection.rangeCount > 0) {
        document.execCommand('justifyLeft')
    }
}

function justifyRight() {
    if (selection.rangeCount > 0) {
        document.execCommand('justifyRight')
    }
}


function justifyFull() {
    document.execCommand('justifyFull')
}


