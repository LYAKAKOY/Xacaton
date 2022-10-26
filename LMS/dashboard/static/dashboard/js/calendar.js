let arrowLeft = document.getElementById("arrow-left");
let arrowRight = document.getElementById("arrow-right");
let cur_month = 0;

for (let i = 1; i < 6; i++) {
    let table0 = document.getElementById(`table${i}`);
    let table2 = document.getElementById(`table${-i}`);
    table0.style.display = "none";
    table2.style.display = "none";
}

arrowLeft.addEventListener('click', prevPage);
arrowRight.addEventListener('click', nextPage);



function prevPage(e) {
    let table1 = document.getElementById(`table${cur_month}`);
    table1.style.display = "none";
    cur_month -= 1;
    let table = document.getElementById(`table${cur_month}`);
    table.style.display = "table";

    if (cur_month == 5) {
        arrowRight.style.display = "none";
    }

    else if (cur_month == -5) {
        arrowLeft.style.display = "none";
    }

    else {
        arrowRight.style.display = "inline";
        arrowLeft.style.display = "inline";
    }
}

function nextPage(e) {
    let table1 = document.getElementById(`table${cur_month}`);
    table1.style.display = "none";
    cur_month += 1;
    let table = document.getElementById(`table${cur_month}`);
    table.style.display = "table";

    if (cur_month == 5) {
        arrowRight.style.display = "none";
    }

    else if (cur_month == -5) {
        arrowLeft.style.display = "none";
    }

    else {
        arrowRight.style.display = "inline";
        arrowLeft.style.display = "inline";
    }
}