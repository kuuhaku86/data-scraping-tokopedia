from scraper import Scraper
from csv_creator import CSVCreator
from flask import Flask, render_template

scraper = Scraper()
datas = scraper.get_data()

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
  return render_template('view.html', datas=datas)

if __name__ == "__main__":
  CSVCreator.create_csv(datas)

  app.run()