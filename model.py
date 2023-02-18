import joblib
from sklearn.svm import SVC

class Model:
    def __init__(self, model_file):
        self.clf = joblib.load(model_file)
    
    def get_predict(self, samples):
        return self.clf.predict(samples)
        
    def get_predict_prob(self, samples):
        return self.clf.predict_proba(samples)


