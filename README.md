# Surfs Up Analysis

[Link to Challenge Code](https://github.com/c-geisel/Surfs_Up/blob/main/SurfsUp_Challenge.ipynb)

## Overview of the analysis 
Explain the purpose of this analysis.

## Results 
Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.

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

![december_temp_stats.png](Images/december_temp_stats.png)
## Summary 
Provide a high-level summary of the results- write a report that describes the key differences in weather between June and December and two recommendations for further analysis.


