// 2
window.addEventListener("load", function () {
    const linksList = document.links;
    let contents = "<ul>";

    for (var i = 0; i < linksList.length; ++i) {
        var currentLink = linksList[i];
        contents += "<li><a href='" + currentLink.href + "'>" + currentLink.innerHTML + "</li>";
    }

    contents += "</ul>";
    document.getElementById("links2").innerHTML = contents;
});

function avail_anchors() {
    document.getElementById("anch").innerHTML = document.anchors.length;
}

function avail_forms() {
    document.getElementById("frms").innerHTML = document.forms.length;
}

function first_label_element() {
    const nodelist = document.getElementsByTagName("label").item(0).innerHTML;
    document.getElementById("first_p").innerHTML = nodelist;
}

function alertFirstP() {
    const x = document.getElementsByTagName("P").namedItem("thefirst_p");
    alert(x.innerHTML);
}

function avail_itms() {
    document.getElementById("its").innerHTML = document.images.length;
}
