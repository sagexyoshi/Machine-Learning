#create your individual project here!
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('train.csv')
data.info()
#data['age'] = 2024 - pd.to_datetime(data['bdate']).dt.year

x = data[['bdate', 'sex', 'education_status']]
y = data['result']

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size = 0.2, random_state = 42)
print(x_train)
print(x_test)