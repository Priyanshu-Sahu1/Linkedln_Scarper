# Linkedln Scarper


Download pycharm and setup virtual enviroment in your pycharm inside the folder LinkedlnProfile_URLDataScraper using Command in terminal below. 

pip install virtualenv or can follow the below link to create virtual Environment

https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

After creating virtual environment in your project.
install scrapy package in pycharm ,
install instaloader package using pip install instaloader ,
install pandas into the terminal using pip install pandas command in the Terminal
To install all these packages use command pip install r- requirement.text 

Before Running the spider run this command to create python path for all python files in the directory
$env:PYTHONPATH = "Path of Directory;$env:PYTHONPATH"
Path of Directory:Main Project Directory which includes all files such as login,requirement and parameter


To scrape data from linkedln (Profile Urls) you need a Linkedln login.
Need to add your credentials in parameter.py file.
Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below
cd .\scraperSkeleton\


After reaching to the scraperSkeleton directory
Run following command in terminal.
scrapy crawl LinkedlnCrawler -o filename.csv --nolog in the terminal.
Notes:

1)


