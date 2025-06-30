from torch import *

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import logger_config

logger = logger_config(process_name="CNN")

class CNN(torch.nn.Module):
    def __init__(self):
        logger.info("Initializing CNN model")
        pass

    def forward(self, x):
        pass

if __name__ == "__main__":
    logger.info("Running CNN model as main script")
    model = CNN()
    logger.info("CNN model initialized successfully")