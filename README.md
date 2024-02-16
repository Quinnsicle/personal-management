Follow the instructions [here to set up flask](https://flask.palletsprojects.com/en/2.1.x/installation/).



## About
---
This project was developed for a friend as a way to help him manage all the data he collects from tracking his time. He is currently using a large excel spreadsheet to log his time. This site will allow him to enter time in a more user friendly interface, while still allowing the flexibility of exporting the data elsewhere. This was also a good excuse to improve my skills with python, learn new frameworks like Flask and React, and experiment with different patterns such as REST API, ORM, and unit tests. 

&nbsp;

## Structure
---
***templates***

***blueprints***

***Models***
  - Uses SQLALCHEMY
  - features a json validator and json to dictionary convertor

***app factory***
  - Easily change configurations or create a new instance

***unit tests***

***api***
 - Easily create a generic api for any model with one line of code 'Generic.register_api(app, model, 'name')'


&nbsp;


## Try it out

First time setup of virtual environment
```bash
. .venv/bin/activate

pip install Flask
pip install jsonschema
pip install flask_sqlalchemy
```

Run the following bash commands to run the flask server
```bash
flask --app=rest run
```

or for powershell users...

```powershell
$env:FLASK_APP = "rest"
$env:FLASK_ENV = "development"

flask run
```
