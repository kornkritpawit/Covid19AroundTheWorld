// set endpoint and your access key
endpoint = 'latest'
access_key = '35c77d0f34c27b8a918447ade3037e6d';
var dateArr =[]

// get the most recent exchange rates via the "latest" endpoint:
$.ajax({
    url: 'http://data.fixer.io/api/' + endpoint + '?access_key=' + access_key,   
    dataType: 'jsonp',
    success: function(json) {

        // exchange rata data is stored in json.rates
        // alert(json.rates.GBP);
        // base currency is stored in json.base
        // alert(json.base);
        // timestamp can be accessed in json.timestamp
        // alert(json.timestamp);
        var dateArr = json.date.split("-");
        year = dateArr[0];
        month = dateArr[1];
        day = dateArr[2];
        $("#1").html("<h1>"+ json.rates.THB +" "+ json.base + " "+ json.date + "</h1>")
    }
})

;