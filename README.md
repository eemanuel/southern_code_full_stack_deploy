# Southern Code Full Stack Test

## Problem

### Description of the task

The candidate is required to design and implement a web application using Django for both the frontend and backend, HTMX, and Tailwind CSS. The application will interact with a public weather API to retrieve and display weather data.

1. Backend Development:
   The developer is tasked with setting up a Django backend that interacts with a public weather API like OpenWeatherMap or Weatherstack. The developer should demonstrate the ability to handle GET and POST requests, error handling, and data extraction from the API's JSON responses.
2. Frontend Development:
   The frontend should be developed using Django templates, HTMX, and Tailwind CSS. The developer needs to create a responsive user interface with a form for users to enter their location (city name, country) and a button to fetch the weather forecast.
3. Interactivity:
   When the user enters a location and clicks the fetch button, a request should be sent to the backend. Using HTMX, update the page with the retrieved weather information without requiring a full page refresh. The displayed data should include weather conditions, temperature, humidity, and wind speed.
4. Error Handling:
   Implement error handling for situations like incorrect city names, API unavailability, or API limit exceeded.
5. Styling:
   Style the interface using Tailwind CSS to make it visually appealing and user-friendly.

## Requirements

### Clone repository

```sh
$ git clone https://github.com/eemanuel/southern_code_full_stack_test
```

### Create virtualenv

Above the cloned directory level

```sh
$ virtualenv venv
$ source venv/bin/activate
```

### Install requirements

At the same level than manage.py

```sh
$ pip install -r requirements/local.txt
```

### Install frontened dependences

If you haven't installed Node:

```sh
sudo snap install node --classic
```

At the same level than manage.py

```sh
$ npm install htmx.org@1.9.2
```

This project was developed using tailwind 3.3.2
but is not necesary to install it to run the project.

### To run development server inside virtualenv

Make migrations and migrate:

```sh
$ python manage.py migrate
```

Then run the local server:

```sh
$ python manage.py runserver
```

### If you want to run the tests

Here you can run all the tests:

```sh
$ pytest -q --disable-warnings
```

## Install pre-commit locally

If you are develoeper you should install in you system:

```sh
pip install pre-commit
```

And at .git folder level execute:

```sh
pre-commit install
```

## Local Endpoint

### URL to check the weather

[GET] http://localhost:8000/
