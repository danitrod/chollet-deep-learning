import matplotlib.pyplot as plt
import numpy as np


def plot_history(hist):
    epochs = np.array(hist.epoch) + 1

    plt.plot(epochs, hist.history['loss'], 'yo', label='Training loss')
    plt.plot(epochs, hist.history['val_loss'], 'r--', label='Validatoin loss')
    plt.xticks(epochs)
    plt.xlabel = 'Epoch'
    plt.title('Loss')
    plt.legend()
    plt.show()
    plt.plot(epochs, hist.history['acc'], 'yo', label='Training accuracy')
    plt.plot(epochs, hist.history['val_acc'],
             'r--', label='Validation accuracy')
    plt.xticks(epochs)
    plt.xlabel = 'Epoch'
    plt.title('Accuracy')
    plt.legend()
    plt.show()
