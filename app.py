#Creating a python file to create Flask apps that will showcase the analysis results

#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies to access SQLite
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import the flask dependencies 
from flask import Flask, jsonify

#set up our database
#create engine variable to access SQLite database (create an engine to access it)
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
#save the references to each table (class)
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create session link from python to the database
session = Session(engine)

#create a new flask application called app
app = Flask(__name__)

#define the welcome route using following code, all things must be defined underneath an @app.route statement
#create welcome function with return statement to return f strings with reference to other routes for analysis
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation 
    /api/v1.0/stations 
    /api/v1.0/tobs 
    /api/v1.0/temp/start/end
    ''')

#create precipitation route that gives precipitation info on each day in previous year
@app.route("/api/v1.0/precipitation")
#create precipitation fnction
def precipitation():
    #find date one year ago from most ercent date
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   #write query to get date an precipitation for most recent year
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    #create a dictionary and use jsonify() to return dict in a json format
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#create stations route that returns data on stations 
@app.route("/api/v1.0/stations")
#create stations function
def stations():
    #create query to get all stations in the database
    results = session.query(Station.station).all()
    #unravel all reults with np.ravel with results as paramenter to make  dimensional array, convert to a list using list()
    stations = list(np.ravel(results))
    #use jsonify() to return results in json format
    return jsonify(stations=stations)

#create a temperature route that returns temp oberservations from the previous year
@app.route("/api/v1.0/tobs")
#create temps function
def temp_monthly():
    #calculate the date one year from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query the primary station (most used station) for the previous year's temp info
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    #unravel results into a one-D array, convert the results into a list
    temps = list(np.ravel(results))
    #return the results of the temps list in a json format
    return jsonify(temps=temps)

#create route for min/max/avg temps. we need two routes for starting and ending dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#create stats funciton with start and end paramenters set to none
def stats(start=None, end=None):
    #Create list with info on the min/max/avg temps
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #add if-not statement to determine the start/end dates and what to do with them if within range
    #we use asterickt with sel (*sel) to show theres multile query results
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    #calculate the min/max/avg temps with the start/end dates
    #create temps list with resutl info then jsonify the list as a return
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)