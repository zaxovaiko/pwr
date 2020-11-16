document.getElementById("setTextWeight").onclick = function (e) {
    const arr = Array.from(document.querySelectorAll("*"));
    arr.forEach((e) => (e.style.fontWeight = document.getElementById("textWeight").value));
};

document.getElementById("chooseTextColor").onclick = function (e) {
    const arr = Array.from(document.querySelectorAll("*"));
    arr.forEach((e) => (e.style.color = document.getElementById("textColor").value));
};

document.getElementById("chooseColor").onclick = function (e) {
    document.body.style.background = document.getElementById("bgColor").value;
};
