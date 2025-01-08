import math
import numpy as np

class Neuron:
    def __init__(self, examples):
        np.random.seed(42)
        self.weights = np.random.normal(0, 1, 3 + 1)
        self.examples = examples
        self.train()
        
    def train(self, learning_rate=0.01, batch_size=10, epochs=200):
        n_batches = len(self.examples) // batch_size
        
        for _ in range(epochs):
            for batch_idx in range(n_batches):
                start_idx = batch_idx * batch_size
                end_idx = start_idx + batch_size
                batch = self.examples[start_idx:end_idx]
                
                batch_outputs = [
                    {
                        "prediction": self.predict(example["features"]),
                        "label": example["label"]
                    }
                    for example in batch
                ]
                
                gradients = self.__get_gradients(batch, batch_outputs)
                self.weights = self.weights - learning_rate * np.array(gradients)
    
    def predict(self, features):
        inputs = np.append(features, 1)
        z = np.dot(self.weights, inputs)
        return 1 / (1 + math.exp(-z))
        
    def __get_gradients(self, batch, predictions_labels):
        errors = [pred["prediction"] - pred["label"] 
                 for pred in predictions_labels]
        gradients = np.zeros_like(self.weights)
        
        for example, error in zip(batch, errors):
            inputs = np.append(example["features"], 1)
            gradients += error * inputs
            
        return gradients / len(batch)
