# django-restapi-project
An Application api written in Django for the project for rest api project source code.

## Technologies used 
*[Django](https://www.djangoproject.com/): The python web framework that encourages development for clean and pragmatic design with less code.

## Installation 
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org/downloads/).
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash 
        $ git clone https://github.com/amly-yaml/django-restapi-project.git
    ```
* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd django-restapi
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv env -p python3
        ```
    3. Cd into virtual environment env:
        ```bash
            $ cd env 
        ```
    4. Activate the virtaul environment:
        ```bash
            $ source bin/activate
        ``` 
    5. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    6. Make those migrations work:
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```
* #### Run the application 
    Run up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/
    ```

