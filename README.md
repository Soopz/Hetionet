# Hetionet
Author: Nelson Lim, Jeffrey Chen
CSCI 493.71

Hetionet is an integrative network of biomedical knowledge assembled from 29 different databases of genes, compounds, diseases, and more. This implementation focuses on the gene, disease,anatomy, and compound relationships. From a disease id, this implementation is able to return the specific genes the disease targets and the specific anatomy the disease affects. Also, from the disease id it can return a specific compound that can treat that disease. 

PROBLEM 1:

To run the first query first the data to be loaded must be in the same directory as the python programs. Createkeyspace.py should be run first to then createtables.py, then the loaddata.cql script through the cqlsh shell. From there the diseasequery.py can be run to query the Cassandra Database.

PROBLEM 2:

TO ACCESS FILES:
unzip the attached files and there should be 2 files(.tsv)
In this project I converted the Files into a .csv so that I was able to enter it into mongodb easily

TO RUN:
I am using Anaconda 3 to run my python code and MongoAtlas' server to store my data
To be able to access MongoAtlas, you must whitelist current IP and and add yourself as a user to be able to access the documents
To import code to Mongo Atlas, I use the following commands on Windows powershell where the command mongoimport is installed
To Run code use command : python project_mongodb.py
