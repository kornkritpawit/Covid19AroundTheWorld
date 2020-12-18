function unpack(rows, key) {
    return rows.map(function (row) {
        return row[key];
    });
}

function unpackTotalCases(rows, key1, key2, key3) {
    return rows.map(function (row) {
        return "Total Cases: " + row[key1] + "<br>" + "Total Death: " + row[key2] + "<br>" + "Total Recovered: " + row[key3];
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
                    totalDeathCases
                    totalRecoveredCases
                }
            }
            `
        })
    });
    // console.log(resp)
    const json = await resp.json();
    // console.log(json)
    let country = json.data.covid19SituationSummaryAllCountry;
    const data = [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: unpack(country, 'countryName'),
        z: unpack(country, 'totalCases'),
        text: unpackTotalCases(country, 'totalCases', 'totalDeathCases', 'totalRecoveredCases'),

        colorscale: [
            [0,'rgb(5, 10, 172)'],[0.3,'rgb(40, 60, 190)'],
            [0.5,'rgb(70, 100, 245)'], [0.7,'rgb(90, 120, 245)'],
            [0.9,'rgb(106, 137, 247)'],[1,'rgb(155,165,202)']],
        autocolorscale: false,
        reversescale: true
    }];

    const layout = {
        title: 'Hover cursor over the country to see the information.',
        geo: {
            projection: {
                type: 'robinson'
            }
        }
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});
}

getCovidCase();