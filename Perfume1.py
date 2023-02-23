# Solución utilizando librería sklearn y modelo de clasificación de vecinos cercanos
# Carga preestablecida de la base de datos
from sklearn.datasets import load_odor
odor = load_odor()

# Atributos de entrada y salida
x = odor.data
y = odor.target

# Dividir los vectores para facilitar el entrenamiento-validación
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.4, random_state = 1)

# Entrenar el modelo segun cantidad de perfumes (vecinos)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 19)
knn.fit(x_train, y_train)

# Predecir la salida
y_pred = knn.predict(x_test)
#print("Predicción: ",str(y_pred))
print("Predicción: ",y_pred)

# Comparar la predicción con la salida
from sklearn import metrics
print("Precisión del modelo KNeighborsClassifier: ",metr.accuracy_score(y_test,y_pred))

# Crear predicción para las salidas de ejemplo
#eje = [[],[]]
#preds = kn.predict(eje)
#pred_perf = [odor.target_names[p] for p in preds]
#print("La Predicción es: ",pred_perf)

# Salvar modelo
from sklearn.externals import joblib
joblib.dump(knn, 'data_knn.pkl')