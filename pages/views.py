from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Create your views here.
def index(request):
    csv_path = 'cyber_crimes.csv'
    df = pd.read_csv(csv_path, encoding = 'euc-kr')
    context = {
        'df': df,
    }
    return render(request, 'pages/index.html', context)
