from sklearn.neural_network import MLPClassifier
import joblib

def train_model(X, y):
    model = MLPClassifier(hidden_layer_sizes=(100, 100), activation='relu', max_iter=500)
    model.fit(X, y)
    return model

def save_model(model, filename):
    joblib.dump(model, filename)
