# Covid-19 Around Asia

![Asia](https://icon-library.com/images/asia-icon/asia-icon-4.jpg)

Our group will analyze the covid19 situation in the country around the world. 
- The first source will provide the covid-19 cases in each country around the world including the new covid-19 case, the new death case and the recovered cases. 
- The second source will provide the total population. 
- The third source will provide all the information of flights that take place in each country. 
- The last source will provide the currency rate in each country and compare covid-19 situation with the currency rate.

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

# How to Open API
1. เข้าไปที่ลิ้ง
   ```
      http://localhost:8080/covid-api/v1/ui/
   ```
2. สามารถดูข้อมูล covid ได้โดยใช้ medthod GRTเพิ่ม / ไปข้างหลัง ui/
   - 

## Team members

| Name | ID |
|-----|-------|
| Vichyawat Nakrugsa | 6110545635 |
| Tiranan Emson | 6110546003 |
| Sukrita Kittipitayakorn | 6110546062 |
| Kasidis Luangwutiwong | 6110546364 |

## Project Documents

* [Project Proposal](https://docs.google.com/document/d/18GtP0rLPiUKCUFxaS5H0ibUgyyp8HK8oZGXdNV5zEKM/edit)