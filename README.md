## **V**UIIS **X**NAT **H**istory **R**eporter

This tiny [Flask](http://flask.pocoo.org) web app hits a REDCap server using
[PyCap](http://sburns.org/PyCap), downloads the project data as a
[pandas](http://pandas.pydata.org) DataFrame, does some simple groupby'ing
& aggregation and displays the resulting tables. Simple & sweet.

### Getting up and running


    $ pip install -r requirements
    $ export VXHR_RCURL=https://redcap.your=institute.org/api/
    $ export VXHR_RCTOKEN=SUPERSECRETTOKEN
    $ python vxhr.py
     * Running on http://127.0.0.1:8000/


### Settings

Required & helpful environment variables vxhr will honor:

* `VXHR_RCURL`: API URL to your REDCap instance
* `VXHR_RCTOKEN`: API Token to your project
* `VXHR_PORT`: port to launch web app, optional, defaults to 9000
* `VXHR_HOST`: host to launch web app, optional, defaults to 127.0.0.1
* `VXHR_INDEX`: url to put index on, defaults to '/'

### Running

Install dependencies:

    $ pip install -r requirements.txt

Development:

    $ python vxhr.py

(Note, the flask app is in `debug` mode)

Production:

    $ gunicorn vxhr:app -c gunicorn.py.ini
