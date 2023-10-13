Select * from swiggy

---Count of restaurant per city
Select City, COUNT(City) as Resta_number 
from swiggy
Group by City
Order by Resta_number Desc

---Highest restaurant city
Select Top 1
City, COUNT(City) as Resta_number
from swiggy
Group by City
Order by Resta_number Desc

-- Restaurants as per their Avg_ratings from highest to lowest
 Select Restaurant,max(Avg_ratings) as ratings
 from swiggy
 Group By Restaurant
 Order By ratings desc
 
 -- Highest  Ave rating restaurant as per Avg_ratings
 Select Restaurant, Avg_ratings
 from swiggy
 where Avg_ratings = (Select max(Avg_ratings) from swiggy)

 --Count of restaurants having highest Avg_ratings as per City
 Select City, COUNT(City) as High_Avg_rating_rest_count
 from swiggy
 where Avg_ratings = (Select max(Avg_ratings) from swiggy)
 Group by City
 Order by High_Avg_rating_rest_count desc

 -- Highest rating restaurant as per Total Ratings
 Select Restaurant, Total_ratings
 from swiggy
 where Total_ratings = (Select max(Total_ratings) from swiggy)

 --Average Delivery time as per Cities
 Select City, avg(Delivery_time) as Avg_Del_Time
 from swiggy
 Group By City
 Order By Avg_Del_Time

 -- City with maximum average delivery time
SELECT Top 1 City, avg(Delivery_time) as Avg_Del_Time
FROM swiggy
Group By City
ORDER BY Avg_Del_Time DESC 

-- City with minimum average delivery time
SELECT Top 1 City, avg(Delivery_time) as Avg_Del_Time
FROM swiggy
Group By City
ORDER BY Avg_Del_Time

---Average price as per city
Select City, round(AVG(Price), 2) as Avg_Price
from swiggy
Group by City
Order by Avg_Price Desc

---Top 10 Restaurant whose price is more than average price of other restaurants
Select Top 10 Restaurant,Food_type, Price
from swiggy
where Price > (Select AVG(Price) from swiggy)
order by Price desc


