import os
import csv

Pypoll_csv = os.path.join("Resources", "PyPoll.csv")




with open(Pypoll_csv, "r") as input_csv_file:
  csvreader = csv.reader(input_csv_file, delimiter = ",")
  header = next(csvreader)
  totalvoteslist=[]
  khanlist=[] 
  Correylist=[]
  lilist=[]
  otlist=[]


  for row in csvreader:
    if row[2] == "Khan":
          khanlist.append(row[2])
    elif row[2] == "Correy":
        Correylist.append(row[2])
    elif row[2] == "Li":
        lilist.append(row[2])
    elif row[2] == "O'Tooley":
        otlist.append(row[2])


    
        



  khanvotes = len(khanlist)
  correyvotes = len(Correylist)
  livotes= len(lilist)
  otvotes = len(otlist)
  
  Countofvotes = len(totalvoteslist)

  total = khanvotes + correyvotes + livotes + otvotes
  
  
  khanpercent= round(100/total * khanvotes)
  Correypercent = round(100/total * correyvotes)
  lipercent = round(100/total * livotes)
  otpercent= round(100/total* otvotes)
  
  
  
  print(f'ELECTION RESULTS')  
  print("-------------------------")
  print(f'Total of the Votes: {total}')
  print("-------------------------")
  print (f'Khan got {khanvotes} votes {khanpercent}%')  
  print(f'Correy got {correyvotes} votes {Correypercent}%')  
  print(f'Li got {livotes} votes {lipercent}%')  
  print(f'OTooley got {otvotes} votes {otpercent}%')  
  print("-------------------------")
  print(f'The Winner is Khan') 


    
     
     