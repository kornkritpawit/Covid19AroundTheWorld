function unpack(rows, key) {
    return rows.map(function (row) {
        return row[key];
    });
}

function unpackTotalCases(rows, rows2) {
    const array = [];
    for (let i = 0; i < rows.length; i++) {
        array.push("Total Cases: " + rows[i].totalCases + "<br>"
            + "Total Death: " + rows[i].totalDeathCases + "<br>"
            + "Total Recovered: " + rows[i].totalRecoveredCases + "<br>"
            + "Today New Cases: " + rows2[i].newCases + "<br>"
            + "Today Death: " + rows2[i].newDeath
        );
    }
    return array;
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

    const resp2 = await fetch('http://localhost:3000/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify({
            query: `
                {
                  covid19SituationNewCasesAllCountry {
                    countryName
                    newCases
                    newDeath
                  }
                }
            `
        })
    });
    const json = await resp.json();
    const json2 = await resp2.json();
    let country = json.data.covid19SituationSummaryAllCountry;
    let country2 = json2.data.covid19SituationNewCasesAllCountry;

    const data = [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: unpack(country, 'countryName'),
        z: unpack(country, 'totalCases'),
        text: unpackTotalCases(country, country2),

        colorscale: [
            [0,'rgb(145,3,3)'],[0.3,'rgb(190,40,40)'],
            [0.5,'rgb(245,70,70)'], [0.7,'rgb(231,117,117)'],
            [0.9,'rgb(231,130,130)'],[1,'rgb(219,193,193)']],
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