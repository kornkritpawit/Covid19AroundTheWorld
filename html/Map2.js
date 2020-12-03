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
                    totalDeathCases
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
        z: unpack(country, 'totalDeathCases'),
        text: unpack(country, 'countryName'),
        colorscale: [
            [0,'rgb(145,3,3)'],[0.3,'rgb(190,40,40)'],
            [0.5,'rgb(245,70,70)'], [0.7,'rgb(231,117,117)'],
            [0.9,'rgb(231,130,130)'],[1,'rgb(219,193,193)']],
        autocolorscale: false,
        reversescale: true
    }];

    const layout = {
        title: 'Hover cursor over the map to see all-time death people by country.',
        geo: {
            projection: {
                type: 'robinson'
            }
        }
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});
}

getCovidCase();