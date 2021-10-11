# Surfs Up Analysis

[Link to Challenge Code](https://github.com/c-geisel/Surfs_Up/blob/main/SurfsUp_Challenge.ipynb)

## Overview of the analysis 
The initial purpose of this analysis is to investigate weather patterns on the island of Oahu to decide if it would be profitable to set up a Surf and Shake Shop year round. In the following analysis summary statistics are found on the months of June and December to determine if this business is sustainable year round. The analysis is completed using Python and Pandas, with SQLite/SQLAlchemy.

## Results 
- The first task in completing this analysis is to determine the summary statistics for June.
    1. The first step in finding June statistics is to write a query that filters all temperatures out of the month of June from the Measurements table. this is      done by starting a query on the date and temperature observations columns in the Measurement column. A filter is then applied that goes through each year           included in the table and selects all dates that greater or equal than the first of June and less than the first of July from the same year. The code for this looks as the following:

    '''

        temps_june = session.query(Measurement.date, Measurement.tobs).\
        filter((Measurement.date >= dt.date(2010, 6, 1)) & (Measurement.date < dt.date(2010, 7, 1))|
           (Measurement.date >= dt.date(2011, 6, 1)) & (Measurement.date < dt.date(2011, 7, 1))|
           (Measurement.date >= dt.date(2012, 6, 1)) & (Measurement.date < dt.date(2012, 7, 1))|
           (Measurement.date >= dt.date(2013, 6, 1)) & (Measurement.date < dt.date(2013, 7, 1))|
           (Measurement.date >= dt.date(2014, 6, 1)) & (Measurement.date < dt.date(2014, 7, 1))|
           (Measurement.date >= dt.date(2015, 6, 1)) & (Measurement.date < dt.date(2015, 7, 1))|
           (Measurement.date >= dt.date(2016, 6, 1)) & (Measurement.date < dt.date(2016, 7, 1))|
           (Measurement.date >= dt.date(2017, 6, 1)) & (Measurement.date < dt.date(2017, 7, 1))).all()

    '''
    
    2. Following this the June temperatures are converted into a list. They are converted to a list so that a data frame may be created. A dataframe is then created with the column names "Date" and "June Temps". The Date is set as the index but we set the index to false so that there are not two Date columns in the data frame. 


    3. With the data frame created, summary statistivcs can be performed on the temperature column by using "df.describe()". The following summary statistics for the temperatures in the month of June are shown:
![june_temp_stats.png](Images/june_temp_stats.png)

'''

    temps_december = session.query(Measurement.date, Measurement.tobs).\
    filter((Measurement.date >= dt.date(2010, 12, 1)) & (Measurement.date < dt.date(2011, 1, 1))|
       (Measurement.date >= dt.date(2011, 12, 1)) & (Measurement.date < dt.date(2012, 1, 1))|
       (Measurement.date >= dt.date(2012, 12, 1)) & (Measurement.date < dt.date(2013, 1, 1))|
       (Measurement.date >= dt.date(2013, 12, 1)) & (Measurement.date < dt.date(2014, 1, 1))|
       (Measurement.date >= dt.date(2014, 12, 1)) & (Measurement.date < dt.date(2015, 1, 1))|
       (Measurement.date >= dt.date(2015, 12, 1)) & (Measurement.date < dt.date(2016, 1, 1))|
       (Measurement.date >= dt.date(2016, 12, 1)) & (Measurement.date < dt.date(2017, 1, 1))).all()
'''

![december_temp_stats.png](Images /december_temp_stats.png)
## Summary 
Provide a high-level summary of the results- write a report that describes the key differences in weather between June and December and two recommendations for further analysis.


