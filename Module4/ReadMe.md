This folder contains the visualizations related to secondary schools in India. Code to generate the plots is also uploaded.

Data source: https://data.gov.in/resources/number-secondary-and-senior-secondary-schools-all-india-level-year-2001-2010

> ds200_plots.py: Code to generate the visualizations

> Senior Secondary schools trend across years.png:  This plot shows the trend of number of senior secondary schools in India from 2001 to 2010. The rate of increase in the number of secondary schools has been nearly constant from 2001 to 2010. This plot shows a near linear trend.

> Lower Secondary schools trend across years.png: This plot shows the trend of number of lower secondary schools in India from 2001 to 2010. The rate of increase in the number of lower secondary schools has been nearly constant from 2001 to 2010. This plot shows a near linear trend.

> Scatter plot 2001.png: This is a scatter plot of number of lower secondary schools v/s number of secondary schools in the year, 2001. Each sample point represents one state. The range of both axes are matched so that the 45deg line represents x=y. In most of the states it is seen that the number of lower secondary schools is much higher than the number of senior secondary schools. 

> Scatter plot 2010.png: This is a scatter plot of number of lower secondary schools v/s number of secondary schools in the year, 2010. Each sample point represents one state. The range of both axes are matched so that the 45deg line represents x=y. In about 50% of the states, the number of lower secondary schools is much higher than the number of senior secondary schools. However, many of the states fall on the 45deg line indicating that the number of senior secondary schools matches with the number of lower secondary schools. This trend is as expected in developing states over time as the requirement of number of secondary schools increases. 

> Box plot Secondary schools.png: This is a box plot showing the trend of increase in number of Secondary schools from 2001 to 2010. Box plot of all states is included. The number of schools is normalized with respect to the number of schools in 2001, so that the plot represents the increase in number of schools w.r.t. 2001. The mean increases over years, indicating that the number of schools are increasing over time. The variance also increases over time as expected. Year 2009 shows an outlier which is far from the remaining points indicating that this might be an issue related to data collection. 

> Box plot Secondary schools no outliers.png: This is the same as plot 'Box plot Secondary schools.png' without outliers. Here the trend of linear increase can be observed more clearly. In some cases the ratio is below 1 indicating that some schools have been closed down
