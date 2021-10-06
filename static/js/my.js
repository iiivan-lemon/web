var clicks = 0;
var clicks1 = 0;
var clicks2 = 0;

    function clickplus() {
        clicks += 1;
        document.getElementById("clicks").innerHTML = clicks;
    };
    function clickminus() {
        clicks -= 1;
        document.getElementById("clicks").innerHTML = clicks;
    };
    function clickplus1() {
        clicks1 += 1;
        document.getElementById("clicks1").innerHTML = clicks1;
    };
    function clickminus1() {
        clicks1 -= 1;
        document.getElementById("clicks1").innerHTML = clicks1;
    };
    function clickplus2() {
        clicks2 += 1;
        document.getElementById("clicks2").innerHTML = clicks2;
    };
    function clickminus2() {
        clicks2 -= 1;
        document.getElementById("clicks2").innerHTML = clicks2;
    };