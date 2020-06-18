import os
import csv

cereal_csv = os.path.join("Resources", "budget_data.csv")





with open(cereal_csv, "r") as input_csv_file:
  csvreader = csv.reader(input_csv_file, delimiter = ",")
  header = next(csvreader)
  profloss= []
  test= []
  
   



  for row in csvreader:
     profloss.append(int(row[1])) 
     

  
    
  totalmonths= len(profloss)
  Min= min(profloss)
  Max= max(profloss)  
  thesum= sum(profloss) 

  print(f'the number of months is: {totalmonths}')
  print(f'the total is: {thesum}')
  print(f'the Max is: {Max}')
  print(f'the Min is: {Min}')