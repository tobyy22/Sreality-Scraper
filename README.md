# Sreality-Scraper

## Assignment
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Usage
- Clone the repository
- Run 'docker-compose up --build' in the root folder of the project
- There will be a http server running on 127.0.0.1:8080 (implemented with Flask framework)
- It will return HTTP page showing scraped flats from Sreality
- Set variable SCRAPE_ON_EACH_REQUEST in settings.py to T/F if you want to scrape on each request


## Database
- Assuming the PostgreSQL database is running locally
- In file settings.py set DB_NAME, USER, PASSWORD
- Database will create its dable if it does not exist yet (does not control if table exists but has wrong structure, will probably be error)
- Before the scrape process runs, it makes sure that the database table is empty
- Name of the table can be specified in database.py
