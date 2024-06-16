from django.shortcuts import render
from django.http import HttpResponse
from CSV.models import *
import csv
# Create your views here.
# inserting data from bank.csv file to database
def insert_bank(request):
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\Django\\madhu\\Scripts\\bankCSV\\CSV\\bank.csv','r') as FO:
        IDO=csv.reader(FO)
        for DO in IDO:
            BN=DO[0].strip()
            BO=Bank(bank_name=BN)
            BO.save()
        return HttpResponse('data is inserted')

# inserting data from branch1.csv file to database
def insert_branch(request):
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\Django\\madhu\\Scripts\\bankCSV\\CSV\\branch1.csv','r')as FO:
        IDO=csv.reader(FO)
        next(IDO)
        for DO in IDO:
            BN=DO[0]
            BO=Bank.objects.filter(bank_name=BN)
            if BO:
                ifsc=DO[1]
                branch=DO[2]
                address=DO[3]
                contact=DO[4]
                city=DO[5]
                district=DO[6]
                state=DO[7]
                BBO=Branch(bank_name=BO[0],isfc=ifsc,branch=branch,address=address,contact=contact,city=city,district=district,state=state)
                BBO.save()
        return HttpResponse('done')