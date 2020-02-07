import pickle
import pandas as pd
import numpy as np
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
ynew = mlp.predict(Xnew.reshape(1, -1))
# show the inputs and predicted outputs
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
