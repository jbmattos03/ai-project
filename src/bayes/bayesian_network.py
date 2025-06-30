from pomegranate import *

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import logger_config

logger = logger_config(process_name="BayesianNetwork")

class BayesianNetwork:
    def __init__(self):
        logger.info("Initializing Bayesian Network model")
        pass

if __name__ == "__main__":
    logger.info("Running Bayesian Network as main script")
    model = BayesianNetwork()
    logger.info("Bayesian Network initialized successfully")