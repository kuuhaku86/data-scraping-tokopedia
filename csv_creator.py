import csv

class CSVCreator:

  @staticmethod
  def create_csv(datas):
    fields = ["name", "price", "city", "img"]

    with open('shoes.csv', 'w') as f:
      writer = csv.DictWriter(f, fieldnames=fields)

      writer.writeheader()
      writer.writerows(datas)