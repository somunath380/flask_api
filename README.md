## The data is stored in the testdb.db file which contains all the data of the bank_branches.csv 

## the dbconfig.py file is for setting up the database and checking connection

## the main backend code is in the app.py file

# Working of app.py

## To run it first you have to run testdb.db 

## To view the details of a bank given its IFSC code 
## type localhost/ifsc/<ifsc number> and this will get the bank corresponding to that given ifsc

## To view the details of all the bank branches of a given bank in a given city 
## type localhost/details/<bank_name>/<city>
  
## all the used frameworks are given in the requirements.txt 
  
#NOTE
  ### i haven't uploaded my created virtual env because it contains more than 100 files
