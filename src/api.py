from flask import Flask, Response, request, send_file
from flask_restful import Resource
import json
from src.utils.transactions import Charts
import pandas as pd

class Net_Worth_Chart(Resource):
    def post(self):
        filename = request.get_json()
        filename.to_csv
        Net_Worth = Net_Worth(filename)
        L1 = Net_Worth.values().tolist()

        dict1  = {}
        for elem in L1:
            dict1[elem[1]] =[]

        for elem in L1:
            dict1[elem[1]].append(elem[0])

        return Response(json.dumps(dict1), mimetype='application/json' )

class Monthly_Expense_Chart(Resource):
    def post(self):
        filename = request.get_json()
        filename.to_csv

        Total_Monthly_Expense = Monthly_Expense(filename)
        L2 = Total_Monthly_Expense.values.tolist()

        dict2 = {}
        for elem in L1:
            dict2[elem[1]] =[]

        for elem in L1:
            dict2[elem[1]].append(elem[0])

        return Response(json.dumps(dict2), mimetype='application/json' )

class Expense_Breakdown_Chart(Resource):
    def post(self):
        filename = request.get_json()
        filename.to_csv

        Expense_Breakdown = Expense_Breakdown(filename)
        L3 = Expense_Breakdown.values.tolist()

        dict3 = {}
        for elem in L1:
            dict3[elem[1]] =[]

        for elem in L1:
            dict3[elem[1]].append(elem[0])
 
        return Response(json.dumps(dict3), mimetype='application/json' )

