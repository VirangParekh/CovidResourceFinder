# CovidResourceFinder

# To Set Up this project locally:

- In the desired folder, git bash the following:
  > > `git clone https://github.com/VirangParekh/CovidResourceFinder.git`
- Set up a python virtual environment using the following commands:

```
$ pip install virtualenv
$ python -m venv env
```

- Activate and deactivate using:

```
$ .\env\Scripts\activate
$ deactivate
```

- In the env, install all the requirements using:
  > > `$ pip install -r requirements.txt`

# To run the project

> - Run the migrations if you haven't already using:

> > `$ python manage.py makemigations`
> > OR
> > `$ python manage.py makemigrations AppName`
> > and
> > `$ python manage.py migrate`

> - Run the server using:
>   > `$ python manage.py runserver`

# Code styles and other things:
- Use the `black` formatter to style the text, run black using
> `$ black .`
> OR
> ~~~
> $ pip install black
> $ black .
> ~~~
- For the frontend development use the `Prettier` code formatter;
  - If using VS Code, there is an extension availble
  - Otherwise, find help at: https://prettier.io/
- Update the requirements file in the roots directory using;
> `pip freeze > requirements.txt`
