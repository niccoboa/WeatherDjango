
# Weather Forecast API using DRS
## Summary and description:
>_RESTful API that provides weather forecasts based on user queries, including location, date, and time. Utilize HTTP methods like GET to retrieve forecasts and POST to submit queries. Developed using Django Rest Framework._

My Weather Forecast API is a Django Rest Framework (DRF) based application that provides weather forecast information. It allows users to access weather forecasts based on location, date, and time. The API is built using Django and DRF and is deployed using Railway. You can test it [[here](https://web-production-5ae0.up.railway.app/)].


## Installation prerequisites
To set up the Weather Forecast API on your PC, please follow these steps:
1. Make sure you have Python and pip installed. You can check the Python version by running `py --version`.
3. Install Django by running: `pip install django`

4. Install Django Rest Framework (DRF): `pip install djangorestframework`


## Usage (test)
To use the Weather Forecast API, follow these instructions:

0. Visit https://web-production-5ae0.up.railway.app/ or go to the development server address if you got it locally.
1. **APP**: Access the API endpoint to view all available weather information by visiting `/forecasts`. This will display all the weather information, ordered by id: https://web-production-5ae0.up.railway.app/forecasts/
> **Note**. The composite primary key is: _location, date, time_. You won't be able to POST a new record if a record with these parameters already exists.
The remaining fields are: _temperature_ and _description_.

2. **GET**: Filter the weather information by location by adding `?field=string` to the API endpoint URL. For example, `/forecasts/?location=Florence` will [display weather forecasts for Florence](https://web-production-5ae0.up.railway.app/forecasts?location=Florence).
The complete list of possible requests (includes 'multi field' stuff) is as follows:
	- [`/forecasts/?id=1`](https://web-production-5ae0.up.railway.app/forecasts/?id=1) 
	- [`/forecasts/?location=Florence`](https://web-production-5ae0.up.railway.app/forecasts/?location=Florence)
	-  [`/forecasts/?location=Florence&date=2023-06-11`](https://web-production-5ae0.up.railway.app/forecasts/?location=Florence&date=2023-06-11)
	- [`/forecasts/?location=Florence&date=2023-06-11&time=10:30:00`](https://web-production-5ae0.up.railway.app/forecasts/?location=Florence&date=2023-06-11&time=10:30:00)
3. **LOGIN** To be able to perform administrative actions like creating or deleting forecasts, you can log as superuser in to the [`/admin` route](https://web-production-5ae0.up.railway.app/admin/).
> I already created one superuser with these credentials: *username*: `niccoboa` and _password_: `niccoboa`. You can use it to test the app of course.

> To logout, just go again to [/admin](https://web-production-5ae0.up.railway.app/admin/) and click on logout on top or directly type: [`/admin/logout`](https://web-production-5ae0.up.railway.app/admin/logout/)

4. **POST**:Once logged in you ar able to POST. Go back to [`/forecasts/`](https://web-production-5ae0.up.railway.app/forecasts/). At the bottom of the page you will find the HTML form provided by DRS. You can add a record by writing, in the content area, something like this:
 ``` js
 {
        "location":    "Dublin",
        "date":        "2023-06-18",
        "time":        "23:30:00",
        "temperature": "12.30",
        "description": "Cloudy"
}
 ```

> **Bonus tip.** You can as well post *multiple* forecasts at the same time, by providing an array of records: ` [{"location":    "Dublin", "date":        "2023-06-18", "time":        "23:30:00", "temperature": "12.30", "description": "Cloudy"
}, {"location":    "New York", "date":        "2023-06-19", "time":        "12:30:00", "temperature": "15.40", "description": "Sunny"}]`

5. **DELETE**: you can delete a single record by **id** by going to the specified forecast (for example: [/forecasts/?id=10](https://web-production-5ae0.up.railway.app/forecasts/?id=10) and then clicking on DELETE red button on top of the page.

## Credits
The Weather Forecast API utilizes the following technologies and frameworks:
- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Django Rest Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- Railway: [https://railway.app/](https://railway.app/)

## Contact
For any questions, feedback, or issues regarding the Weather Forecast API, please feel free to contact me at [niccolo.boanini@stud.unifi.it](mailto:niccolo.boanini@stud.unifi.it).
