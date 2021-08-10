import pandas as pd

import numpy as np

import os

from datetime import timedelta


print(os.getcwd())
print('./파일이름.txt 입력하면 됨')
f=input("파일경로와 이름입력:")
#주소를 텍스트로 복사해서 입력

df = pd.read_csv(f, delimiter = '\t',encoding='cp949')

#df = pd.read_csv(csv, encoding='cp949')
df.columns = ['time', '공조온도', '공조급기', 'x', '상부온도', '품온', '품온1', '품온2', '하부온도']
df = df.drop('x', axis=1)
#print(df.head())
print(df)
print('\n')
new_data={}

idx = 0 ## 원하는 인덱스
 
temp1 = df[df.index < idx]
temp2 = df[df.index >= idx]
df = temp1.append(new_data, ignore_index=True).append(temp2, ignore_index=True)

print(df)

df['time'] = df['time'].fillna(method='bfill')


print(df)


#df['new_time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S', errors='raise')

df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S', errors='raise')+ timedelta(minutes=15)


print(df)

#print(df.iloc[0][0])
df.iloc[0,0] = df.iloc[1,0] - timedelta(minutes=15)

#range={1,2,3,4,5,6,7}
#for i in range:
#  df.iloc[0][i] = pd.to_numeric(df.iloc[0][i])

print(df)

#df = df.drop('time', axis=1)

#dfa = df['a'].dropna(axis=0)

df.index = pd.DatetimeIndex(df['time']) 

print(df)

#dfa_summary = dfa.resample('H').first()
df_summary = df.resample('30T').mean()
print(df_summary)
df_summary = df_summary.resample('H').first()

print(df_summary)

df_summary.to_excel(excel_writer='./평균.xlsx')
