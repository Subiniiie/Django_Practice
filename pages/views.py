from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
import numpy as np
import csv

# Create your views here.
def index(request):
    csv_path = 'cyber_crimes.csv'
    df = pd.read_csv(csv_path, encoding = 'euc-kr')
    context = {
        'df': df,
    }
    return render(request, 'pages/index.html', context)


def occur(request):
    font_path = 'C:\Windows\Fonts\malgun.ttf'
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'
    csv_path = 'cyber_crimes.csv'
    df = pd.read_csv(csv_path, encoding = 'euc-kr')
    occur_df = df.iloc[2::2]
    occur_df = occur_df.drop(columns = ['구분'])
    
    x = occur_df['연도']
    y = occur_df.columns[1:]
    
    fig, ax = plt.subplots(figsize=(20, 16))
    for column in y:
        ax.plot(x, occur_df[column], label=column)
    ax.legend(loc='upper left')
    
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'occur_df': occur_df,
    }
    plt.close(fig)
    return render(request, 'pages/occur.html', context)


def arrest(request):
    font_path = 'C:\Windows\Fonts\malgun.ttf'
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'
    csv_path = 'cyber_crimes.csv'
    df = pd.read_csv(csv_path, encoding = 'euc-kr')
    arrest_df = df.iloc[1::2]
    arrest_df = arrest_df.drop(columns= ['구분'])
    
    x = arrest_df['연도']
    y = arrest_df.columns[1:]
    
    fig, ax = plt.subplots(figsize=(20, 16))
    for column in y :
        ax.plot(x, arrest_df[column], label=column)
    ax.legend()
    
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'arrest_df': arrest_df,
    }
    plt.close(fig)
    return render(request, 'pages/arrest.html', context)
    
