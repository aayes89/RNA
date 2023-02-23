# importar las clases para trabajar con los datos
import numpy as np
import pandas as pd

# Cargar los datos de olor de los perfumes
df_olor = pd.read_csv('perfume_data.csv', index_col=0)
df_olor = pd.read_excel('perfume_data.xlsx', index_col=0)

# Atributos de entrada y salida
df_olor.head()
#df_olor.describe()

# Separo los datos de prueba de la salida.
# Se tienen 28 olores como datos de entrada 
# El atributo de salida es perfume, de tipo nominal, por lo que se trata de un problema de clasificación por cluster

# elementos de las columnas B hasta la AC, en este caso nombradas como i1-i28
X = df_olor[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10','i11','i12','i13','i14','i15','i16','i17','i18','i19','i20','i21','i22','i23','i24','i25','i26','i27','i28']].values
# Los perfumes son:
mapping = {"'ajayeb'":0, "'ajmal'":1, "'amreaj'":2, "'aood'": 3,"'asgar_ali'": 4, "'bukhoor'": 5, "'burberrry'": 6,"'dehenalaod'": 7, "'junaid'": 8, "'kausar'": 9, "'rose'": 10,"'solidmusk'": 11, "'TeaTreeOil'":12 , "'raspberry'": 13,"'RoseMusk'": 14, "'strawberry'": 15, "'constrected2'": 16,"'carolina_herrera'": 17, "'oudh_ma'alattar'": 18,"'constrected'":19}

y = df_olor.replace({'class': mapping})
#y = df_olor.replace({'class': mapping})['perfume'].values

# Defino la RNA
from sklearn.neural_network import MLPClassifier
mlpc = MLPClassifier(hidden_layer_sizes=(10, 5), solver='sgd', max_iter=1000, early_stopping=True, activation='logistic')

# Entreno la RNA
with ignore_warnings(category=ConvergenceWarning):
mlpc = mlpc.fit(X,y)

# Calculo el error del entrenamiento

from sklearn.metrics import mean_squared_error

y_pred = mlpc.predict(X)
error  = 0

for truth, pred in zip(y, y_pred):
	if truth != pred:
		error +=1
error /= len(y_pred)		

print("El error de entrenamiento es: "+ str(error))

# Devuelvo la predicción
print("Predicción: "+str(y_pred))
# Si y_pred es arreglo, entonces
for yy in y_pred:
   print(yy)
