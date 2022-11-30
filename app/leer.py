import csv

def readcsv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file,delimiter=',')
    header = next(reader)
    print(header)

    data =[]
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)

    return data
    
      



if __name__ == '__main__':
  data = readcsv('./data.csv')
  print(data)
  
