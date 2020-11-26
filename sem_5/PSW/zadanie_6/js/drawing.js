window.addEventListener("load", function () {
    resetField();

    //
    document.getElementById("canvas").addEventListener(
        "mousemove",
        function (e) {
            document.getElementById("coordsS").innerHTML = `ScreenCoords: (${e.screenX}, ${e.screenY})`;
            document.getElementById("coordsC").innerHTML = `ClientCoords: (${e.clientX}, ${e.clientY})`;

            if (e.target.tagName.toLowerCase() == "td") {
                if (e.ctrlKey) {
                    e.target.setAttribute("class", "blue");
                }
                if (e.shiftKey) {
                    e.target.setAttribute("class", "red");
                }
                if (e.altKey) {
                    e.target.setAttribute("class", "");
                }
            }
        },
        false
    );

    document.addEventListener("keyup", function (e) {
        if (e.keyCode == 65) {
            resetField();
        }
    });
});

function resetField() {
    const side = window.innerWidth / 12;
    const tbody = document.getElementById("tablebody");
    tbody.innerHTML = "";

    for (let i = 0; i < side; ++i) {
        const row = document.createElement("tr");
        for (let j = 0; j < side; ++j) {
            const cell = document.createElement("td");
            row.appendChild(cell);
        }
        tbody.appendChild(row);
    }
}
