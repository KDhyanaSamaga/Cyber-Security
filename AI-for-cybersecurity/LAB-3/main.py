import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

path = r'D:\Cyber-Security\AI-for-cybersecurity\LAB-3\payment_fraud.csv'

try:
    print("Processing.....\n")
    df = pd.read_csv(path)
    print("Dataset Loaded successfully......\n")
except FileExistsError:
    print("Please fix the path or Dataset does not exist")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


df = pd.get_dummies(df, columns=['paymentMethod'])

print(f"The size of the dataset :{df.shape}\n")
print(f"The features column:{df.columns.tolist()}\n")
print(f"Dataset Information :{df.info()}\n")
print(f"Sample Data :{df.sample(5)}\n")
print(f"Summary of the Dataset :{df.describe}\n")

X = df.drop('label', axis=1)
Y = df['label']
print(f"Input shape of X:{X.shape}\n")
print(f"Output shape of Y: {Y.shape}\n")

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.33, random_state=17)


model = LogisticRegression()
result = model.fit(X_train, Y_train)

Y_pred = result.predict(X_test)
print(accuracy_score(Y_pred, Y_test))
print(confusion_matrix(Y_test, Y_pred))




