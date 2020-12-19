function intoArray(data) {
    const populationArray = [];
    const totalCasesArray = [];

    for (let i = 0; i < data.length; i++) {
        populationArray.push(data[i].population);
        totalCasesArray.push(data[i].totalCases);
    }

    return [populationArray, totalCasesArray]
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
                        population
                        totalCases
                    }
                }
            `
        })
    });
    const json = await resp.json();
    const data = json.data.covid19SituationSummaryAllCountry;

    const array = intoArray(data);
    const populationArray = array[0],
        totalCasesArray = array[1];

    const trace1 = {
        x: populationArray,
        y: totalCasesArray,
        mode: 'markers',
        marker: {
            size: Array(populationArray.length).fill(20)
        }
    };

    const plotData = [trace1];

    const layout = {
        title: 'Marker Size',
        showlegend: false,
        height: 600,
        width: 900
    };

    Plotly.newPlot('myDiv', plotData, layout);
}

getCovidCase();