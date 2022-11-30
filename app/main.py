import utils 
import leer as leer
import charts as charts


def run():
  
  data = leer.readcsv("./data.csv")
  country = input('Type Country => ')
  
  
  result = utils.population_by_country(data,country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.gen_population(country);
    charts.generate_chart(country['Country/Territory'],labels, values)
     
if __name__ == '__main__':
  run()