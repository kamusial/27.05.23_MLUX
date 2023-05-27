import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins')

# print(penguins.to_string())
# sns.pairplot(penguins, hue='species')
# plt.show()

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
penguins_features = penguins_filtered.drop(columns=['species'])
target = pd.get_dummies(penguins_filtered['species'])
print(target)

from sklearn.model_selection import train_test_split
from tensorflow import keras
from numpy.random import seed
seed(1)
from tensorflow.random import set_seed
set_seed(2)
penguins_features
X_train, X_test, y_train, y_test = train_test_split(penguins_features, target, test_size=0.2, random_state=0)

print(X_train.shape)
inputs = keras.Input(shape=X_train.shape[1])
hidden_layer = keras.layers.Dense(4, activation="relu")(inputs)
output_layer = keras.layers.Dense(3, activation="relu")(hidden_layer)

model = keras.Model(inputs=inputs, outputs=output_layer)

