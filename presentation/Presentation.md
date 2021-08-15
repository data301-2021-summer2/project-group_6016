# Presentation
(I cannot record with my computer so I will written out my presentation, I have explained my situation to professor)
## Overview
The data I chose is about bike rentals. The data is collected in 2 year span. It includes: The amount of instants, date, season, year, month, holiday, weekday, workingday, weather, temperature, feeling temperature, humidity, windspeed, amount of casual users, amount of registered users and the total count of users that rented on that day. For my research I will be using holiday, temperature, humidity and windspeed. I would like to find out the relationship of people's willingness to rent bike on different kind of day. Such as, holiday/working day, and the effect of temperature, humidity and windspeed on people's desire to rent bike.
## How many instances are in the data?
As mentioned, the data is collected in 2 years span and has 731 instances. I used df.shape to find out the amount of columns and rows in the dataset.
## First research: Holiday and non Holiday
I want to know the willingness of people renting bike during holidays and non holidays (0 is non holiday and 1 is holiday). I will find out by comparing the count (cnt) of people renting bike during holidays and non holidays. Also, I will calculate the max, min and average value for both holidays and non holidays.
After looking at the graphs, we can see that surprisingly people rented more bike on non holidays compare to holidays (4527 to 3735). On the other hand, holidays have a more steady rent rate compare to non holidays, ranging from 1000-7403 counts, compare to 22-8714 counts.
## Second research: Temperature and Count
I want to see how the temperature affect people's willingness to rent a bike. Temperature value is derived by (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale). This is the default value for temperature, but we can still see whether people are more willing to rent a bike during hot days or cooler days.
Based on the result, we can clearly see that people prefer biking on a hotter day compare to cooler day, which is another surprice. My initial hypothesis is the people will prefer cooler day than hotter day to enjoy the breeze. We can assume that data is collected in a colder area.
## Third research: Humidity and Count
After temperature, I also would like to see how the humidity can affect people's decision renting a bike.
We can see that the average humidity falls around 0.6. Based on comparing humidity and count, wew can assume people enjoy biking on all kind of humidity. Generally people still prefer humidity that are just all right, maybe sometimes a little bit more humid weather too.
## Fourth research: Windspeed and Count
From the graphs we can see that people prefer less windy days compare to more windy days. Especially when it is extremely windy (0.5), although it only occurs once, we can see that the count dropped.
## Conclusion
In conclusion, weather does not play a huge factor on people's desire to rent bikes. Based on comparing between the number of bike rented between holiday and non holidays, we can assume that a lot of people rent bike on a regular basis during workdays, so weather plays a lesser factor on people's willingness to rent bikes. 