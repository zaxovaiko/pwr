//1
let idcount = 0;
let currentNode = document.getElementById("bigheading");

window.addEventListener("load", function () {
    document.getElementById("byIdButton").addEventListener("click", byId, false);
    document.getElementById("insertButton").addEventListener("click", insert, false);
    document.getElementById("appendButton").addEventListener("click", appendNode, false);
    document.getElementById("replaceButton").addEventListener("click", replaceCurrent, false);
    document.getElementById("removeButton").addEventListener("click", remove, false);
    document.getElementById("parentButton").addEventListener("click", parentt, false);
});

function byId() {
    const id = document.getElementById("gbi").value;
    const target = document.getElementById(id);

    if (target) {
        switchTo(target);
    }
}

function insert() {
    const newNode = createNewNode(document.getElementById("ins").value);
    currentNode.insertBefore(newNode, currentNode.childNodes[0]);
    switchTo(newNode);
}

function appendNode() {
    const newNode = createNewNode(document.getElementById("append").value);
    currentNode.appendChild(newNode);
    switchTo(newNode);
}

function replaceCurrent() {
    var newNode = createNewNode(document.getElementById("replace").value );
    currentNode.parentNode.replaceChild(newNode, currentNode);
    switchTo(newNode);
}

function remove() {
    if (currentNode.parentNode == document.body){
        alert( "Can't remove a top-level element." );
    }
    else {
        var oldNode = currentNode;
        switchTo(oldNode.parentNode);
        currentNode.removeChild(oldNode);
    }
}

function parentt() {
    var target = currentNode.parentNode;
    if (target != document.body)
        switchTo(target);
    else
        alert("No parent.");
}

function createNewNode(text) {
    let newNode = document.createElement("p");
    let nodeId = "new" + idcount++;
    newNode.setAttribute("id", nodeId);
    text = "[" + nodeId + "] " + text;
    newNode.appendChild(document.createTextNode(text));
    return newNode;
}

function switchTo(newNode) {
    currentNode.className = "";
    currentNode = newNode;
    currentNode.classList.add("highlighted");
    document.getElementById("gbi").value = currentNode.getAttribute("id");
}