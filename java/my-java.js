// Create a degital Clock 




    function time2time() {
        let myTime = new Date();
        let h = myTime.getHours();
        let m = myTime.getMinutes();
        let s = myTime.getSeconds();
        let indicator = "AM";
        if (h >= 12) {
            h = h -12;
            indicator = "PM";
        }
    document.getElementById("idName").innerHTML = h + ":" + m + ":" + s + " "+ indicator;
    }
    setInterval(time2time, 1000);


// Degital clock code ended 



