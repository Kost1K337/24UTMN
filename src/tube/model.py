import joblib
import zipfile

class DTreeForIMA:
    def __init__(self, filename):
        self.filename = filename
        with zipfile.ZipFile(f'{self.filename}.zip', 'r') as zip_ref:
            zip_ref.extractall()
        self.model = joblib.load(f'tube/{self.filename}.pkl')

    def predict(self, X_test):
        pred_dtr = self.model.predict(X_test)
        return pred_dtr