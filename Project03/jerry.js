var serverCall = function(path, method, requestData, callback) {
    var xmlhttp = new XMLHttpRequest();
    var url = "https://mac1xa3.ca/e/sunwooj/accounts/" + path + "/";

    xmlhttp.onreadystatechange = function() {
        //if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
        if (this.readyState == 4) {
            var myArr = JSON.parse(this.responseText);
            callback(this.status, myArr);
        }
    };

    xmlhttp.open(method, url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json")
    xmlhttp.send(JSON.stringify(requestData));
}
