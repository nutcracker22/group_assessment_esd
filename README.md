# group_assessment_esd

- checked for open data, found a dataset on air pollution in Scotland on https://www.scottishairquality.scot/
- Chose the data for Aberdeen from 1st Jan. 2022 until 25th March to match the requirement of 2000 - 7000 rows
- Designed a database using draw.io
- identified the need to add staion details data, which was not available in the dataset, but on the website
- coded a webscraper using selenium and BeautifulSoup to retrieve the data for station details from the website.
- setup models.py to structure the database in our code, according to the abovementioned database design
- coded the parser, which handled both the csv file downloaded, as well as the webscraper
- implemented extensive errorhandling in the parser, since the dataset contains many missing datapoints.
- in this way no manual manipulation of the csv file was required
- problems were the limitations of DecimalField and IntegerField, since they did not allow to have empty cells, when data was missing
- had a group discussion, on how to progress and how to split up the tasks.
- Considering GitHub issues and Kanban board, we decided to use GitHub issues, since they can be created, assigned and closed with terminal commands from our IDEs
- 