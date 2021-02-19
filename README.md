# data-wrangling-result
Script to scrap a website to get daily energy price

## Libraries
Libraries used: the following libraries were installed/used to achieve the goal of the challenge
* Beautiful Soup - for webscraping
* pandas - for data manipulation
* re - for regex
* datetime - for date
* requests - to access the html page


## Scraping Process
* Download and parse the html file
* Download the HTML file
* parse the HTML with BeautifulSoup and create a soup object
* select the table tag and specifice the exact one using css classes, attribute or index
* select the th and tr tags
* convert element to text
* use for loop to iterate over the values and append to an empty list
* select the tr tags
* use for loop to iterate to the values in each row and append to a list
* convert to a dataframe
* write a function to create date time object for weekdays from start date to end date
* convert list to series, merge with the dataframe and drop columns not needed
* save as csv file




## Challenges
Here are some of the challenges experienced
* Firstly, the data was partition monthly using an empty tr tag. when the data was scrapped this created an empty row without values.
* I decided not to use drop.na() as some empty cells wheren't just partitioned rows but actual missing values, removing missing values will affect the dataset.
*when I tried it, I noticed the dated that was created on the rows were also deleted.
