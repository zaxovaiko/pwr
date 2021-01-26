const tip = document.getElementById("tip");
const inputs = Array.from(document.querySelectorAll("input"));
inputs.forEach((e) => {
    e.onfocus = function (e) {
        tip.style.display = "block";
        tip.innerHTML = `Focus on input with name "${e.target.name}"`;
    };

    e.onblur = function () {
        tip.style.display = "none";
    };
});

// Form
// const form = document.getElementById("order-form");
// form.addEventListener("submit", function (e) {
//     e.preventDefault();

//     if (confirm("Do you want to submit?")) {
//         alert("Form was Submitted.");
//         document.writeln(
//             `<p>Form was submitted today at</p><h1>${new Date()}</h1><a href="javascript:history.back();">Go back</a>`
//         );
//     }
// });

// form.addEventListener("reset", function () {
//     tip.innerHTML = "Form was reset";
//     tip.style.display = "block";
//     setTimeout(() => {
//         tip.style.display = "none";
//     }, 1000);
// });
