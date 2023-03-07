# survey.csv 위에서 5개 출력
import usecsv
import csv
import re
import pandas as pd

df = pd.read_csv('survey.csv')
print(df.head())
print(df.mean())
print('수입합계 : ', df.income.sum())
# 수입 중앙값
print('수입 중앙값 : ', df.income.median())
print(df.describe())
print(df.income.describe())
print(df.sex.value_counts())