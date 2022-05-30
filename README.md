Follow the instructions [here to set up flask](https://flask.palletsprojects.com/en/2.1.x/installation/).

Then run the following bash commands to run the flask server

```bash
. venv/bin/activate
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

or for powershell users...

```powershell
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

flask run
```
