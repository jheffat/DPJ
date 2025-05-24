"""
DPJ - A CLI Encryption Application
Author: Jheff MAT
License: MIT
Version: 3.5.3
"""

__version__ = "3.5.3"
__author__ = "Jheff MAT"

# Expose core functions for easy import
from .utils import *

 

# Optionally, include logging or configuration setup
import logging

# Set up logging (optional, if you want detailed logging in your app)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example usage of logging
logger.info("DPJ app initialized")