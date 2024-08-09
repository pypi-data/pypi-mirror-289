# Import the main functions and classes from pytuft.py
from .pytuft import compile_contract, deploy_contract, execute_contract, calculate_fee, get_account_balance

import logging

logging.basicConfig(level=logging.INFO)

# Optional: define the __all__ variable to specify what gets imported with 'from pytuft import *'
__all__ = ['compile_contract', 'deploy_contract', 'execute_contract', 'calculate_fee', 'get_account_balance']
