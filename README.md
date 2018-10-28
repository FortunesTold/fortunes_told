Fortunes Told
--------



### Running Fortunes Told locally

Clone this repo:
```
> git clone https://github.com/FortunesTold/fortunes_told.git
```

Create a virtual environment:
```
> virtualenv env
> source env/bin/activate
```

Install the dependencies:
```
> pip install -r requirements.txt
```

Ensure your keys are set in your virtual env:
```
> source secrets.sh
```

Start the app:
```
> python server.py
```

Go to http://localhost:5000 in your browser to have your fortunes told! 