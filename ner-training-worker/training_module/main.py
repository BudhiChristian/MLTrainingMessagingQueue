from .preparation import prepare_training_data
from .training import train

def train_data(data):
    training_data = prepare_training_data(data)
    train(train_data)