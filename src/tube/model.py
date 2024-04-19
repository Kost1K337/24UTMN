from tensorflow.keras.models import load_model
import joblib

modelsPath = 'tube/assets/models'
scalersPath = 'tube/assets/scalers'


class SSiTModel:
    def __init__(self, pipeChars):
        self.model = self.load_model(pipe=pipeChars)
        self.scaler = self.load_scaler(pipe=pipeChars)

    def load_model(self, pipe):
        return load_model('/'.join([modelsPath, f'Pipe_with_params_{pipe}_model.h5']))

    def load_scaler(self, pipe):
        return joblib.load('/'.join([scalersPath,f'std_scaler_{pipe}.bin']))

    def changePipe(self, pipeChars):
        self.model = self.load_model(pipe=pipeChars)
        self.scaler = self.load_scaler(pipe=pipeChars)

    def predict(self, data):
        scaled_data = self.scaler.transform(data)
        preds = self.model.predict(scaled_data).astype(float)
        return preds