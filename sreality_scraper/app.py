from flask import Flask, render_template
from sreality_scraper.database import database
import subprocess
from settings import SCRAPE_ON_EACH_REQUEST

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():

    if SCRAPE_ON_EACH_REQUEST:
        database.delete_all_items()
        subprocess.check_output(['python3', 'sreality_scraper/spiders/sreality_spider.py'])

    #get the data from db
    items = database.load_all_items()

    #render html template with data
    return render_template('./index.html', items=items)

if __name__ == '__main__':
    database.create_table_if_doesnt_exist()

    if not SCRAPE_ON_EACH_REQUEST:
        database.delete_all_items()
        subprocess.check_output(['python3', 'sreality_scraper/spiders/sreality_spider.py'])
        
    app.run(host='0.0.0.0', port=8080, debug=True)