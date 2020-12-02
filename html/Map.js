Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv', function(err, rows){
      function unpack(rows, key) {
          console.log(rows);
          console.log(key);
          return rows.map(function(row) { return row[key]; });
      }

      array = []

      myObj = {
          location: "Belarus",
          alcohol: "17.5"
      }
      array.push(myObj)
    country = [{location: "Australia", covid:"900"}
    ,{location: "Canada", covid:"90"}]
    var data = [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: unpack(country, 'location'),
        z: unpack(country, 'covid'),
        text: unpack(country, 'location'),
        autocolorscale: true
    }];

    var layout = {
      // title: 'Pure alcohol consumption<br>among adults (age 15+) in 2010',
      geo: {
          projection: {
              type: 'robinson'
          }
      }
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});

});