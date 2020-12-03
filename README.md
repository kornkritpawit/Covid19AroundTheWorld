# Covid-19 Around The World

![Asia](https://icon-library.com/images/asia-icon/asia-icon-4.jpg)

Our group will analyze the covid-19 situation around  the world. 
- The first source will provide the covid-19 cases in each around  the world including the total covid-19 case, the total death case ,new case ,new death
- The second source will provide the recovered cases. 
- The third source will provide the country  around  the world. 
- The last source will provide the currency rate in each country.

## Requirement
Python version 3.6 or greater is required.

## Installation
1. Clone or download the project to your machine.
2. Install Flask framework. Use command line tools.

    For Unix:
    ```
    pip3 install Flask
   ```
   
    For Windows:
    ```
    pip install Flask
   ```
3. Access to project directory. For example,
    ```
    YOUR_DIRECTORY/Covid19AroundAsia/ $
   ```
4. Generate models by this command.
    ```
    java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/covid-api.yaml -o autogen -g python-flask
   ```
5. Run local server on your machine by this command.
   
   For Unix:
    ```
   python3 app.py
   ```
   
   For Windows:
   ```
   python app.py
   ```
   The server will running on default configuration on http://localhost:8080/.
6. Open second window command line. Open GraphQL accessible by this command.
    ```
   openapi-to-graphql --cors -u http://localhost:8080/covid-api/v1/ openapi/covid-api.yaml
   ```
   Default port is 8080. You can change to your port that you open python local server.

# How to Open API
1. Start the REST API server and Optionally test the API at
   ```
      http://localhost:8080/covid-api/v1/ui/
   ```
2. We can see information about covid-19 API by seeing the documentation. All method provide by GET request.
   - /countries
   - /countries/{countryName}
   - /covid19Situation/newCases/allCountry
   - /covid19Situation/newCases/world
   - /covid19Situation/newCases/{countryName}
   - /covid19Situation/summary/allCountry
   - /covid19Situation/summary/world
   - /currencyRates/unit/{countryName}
   - /currencyRates/{countryName}

## Team members

| Name | ID |
|-----|-------|
| Vichyawat Nakrugsa | 6110545635 |
| Tiranan Emson | 6110546003 |
| Sukrita Kittipitayakorn | 6110546062 |
| Kasidis Luangwutiwong | 6110546364 |

## Project Documents

* [Project Proposal](https://docs.google.com/document/d/18GtP0rLPiUKCUFxaS5H0ibUgyyp8HK8oZGXdNV5zEKM/edit)