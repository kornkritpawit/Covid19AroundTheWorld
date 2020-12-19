function intoArray(data) {
    const populationArray = [];
    const totalCasesArray = [];
    const textArray = [];
    const colorArray = [];

    for (let i = 0; i < data.length; i++) {
        populationArray.push(data[i].population);
        totalCasesArray.push(data[i].totalCases);
        textArray.push(data[i].countryName + "<br>"
            + "Total Cases: " +  data[i].totalCases + "<br>"
            + "Population: " + data[i].population + "<br>"
            + "Cases per 1 million: " + Math.round(data[i].totalCases / data[i].population * 1000000)
        );
        if ((data[i].totalCases / data[i].population) < 0.001) {
            colorArray.push('rgb(44, 160, 101)');
        } else if ((data[i].totalCases / data[i].population) < 0.01) {
            colorArray.push('rgb(255, 144, 14)');
        } else {
            colorArray.push('rgb(255, 65, 54)');
        }
    }

    return [populationArray, totalCasesArray, textArray, colorArray]
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
        totalCasesArray = array[1],
        countryNameArray = array[2],
        colorArray = array[3];

    const trace1 = {
        x: populationArray,
        y: totalCasesArray,
        text: countryNameArray,
        mode: 'markers',
        marker: {
            size: Array(populationArray.length).fill(20),
            color: colorArray
        }
    };

    const plotData = [trace1];

    const layout = {
        title: 'Infected and Population in each country',
        showlegend: false,
        height: 600,
        width: 900,
        xaxis: {
            title: 'Population'
        },
        yaxis: {
            title: 'Total Cases'
        }
    };

    Plotly.newPlot('myDiv', plotData, layout);
}

getCovidCase();