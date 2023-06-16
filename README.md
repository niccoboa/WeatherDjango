# Weather Forecast API
## REST Django Framework

_RESTful API that provides weather forecasts based on user queries, including location,
date, and time. Utilize HTTP methods like GET to retrieve forecasts and POST to submit queries._


## Description
The Weather Forecast API is a Django Rest Framework (DRF) based application that provides weather forecast information. It allows users to access weather forecasts based on location, date, and time. The API is built using Django and DRF and is deployed using Railway. You can test it here: [here](https://link-url-here.org](https://web-production-5ae0.up.railway.app/)

## Installation
To set up the Weather Forecast API, please follow these steps:

1. Make sure you have Python installed. You can check the Python version by running `py --version`.

2. Install Django by running the following command: `pip install django`

3. Install Django Rest Framework (DRF) by running the following command: `pip install djangorestframework`


## Usage
To use the Weather Forecast API, follow these instructions:

1. Access the API endpoint to view all available weather information by visiting `/forecasts`. This will display all the weather information.

2. Filter the weather information by location by adding `?location=YourCity` to the API endpoint URL. For example, `/forecasts?location=NewYork` will display weather forecasts for New York.

3. Additionally, you can filter the weather information by location, date, and time. For example, `/forecasts?location=NewYork&date=2023-06-15&time=12:00` will display the weather forecast for New York on June 15, 2023, at 12:00 PM.

4. To perform administrative actions like creating or deleting forecasts, you can log in to the `/admin` route.


## Credits
The Weather Forecast API utilizes the following technologies and frameworks:
- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Django Rest Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- Railway: [https://railway.app/](https://railway.app/)

## Contact
For any questions, feedback, or issues regarding the Weather Forecast API, please feel free to contact me at [niccolo.boanini@stud.unifi.it](mailto:niccolo.boanini@stud.unifi.it).
