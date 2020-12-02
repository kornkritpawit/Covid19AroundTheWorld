function unpack(rows, key) {
    return rows.map(function (row) {
        return row[key];
    });
}


async function getCovidCase() {
    const resp = await fetch('http://localhost:3000/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({
            query: `
            {
                covid19SituationSummaryAllCountry {
                    countryName
                    totalCases
                }
            }`
        })
    });
    console.log(resp)
    const json = await resp.json();
    console.log(json)
    let country = json.data.covid19SituationSummaryAllCountry;
    console.log(country)
    const data = [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: unpack(country, 'countryName'),
        z: unpack(country, 'totalCases'),
        text: unpack(country, 'countryName'),
        autocolorscale: true
    }];

    const layout = {
        title: 'Hover cursor over the map to see all-time infected people by country.',
        geo: {
            projection: {
                type: 'robinson'
            }
        }
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});
}

getCovidCase();