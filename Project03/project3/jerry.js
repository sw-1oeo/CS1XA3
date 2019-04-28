/* Make API call to the Django server */
var serverCall = function(path, method, requestData, callback) {
    var xmlhttp = new XMLHttpRequest();
    // Set url from base url plus specific path
    var url = "https://mac1xa3.ca/e/sunwooj/accounts/" + path + "/";

    xmlhttp.onreadystatechange = function() {
        // check if response is ready
        if (this.readyState == 4) {
            // Parse JSON data from response
            var myArr = JSON.parse(this.responseText);
            // Call the callback function, pass the status code and data
            callback(this.status, myArr);
        }
    };

    // Make a JSON request to the server
    xmlhttp.open(method, url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json")
    xmlhttp.send(JSON.stringify(requestData));
}