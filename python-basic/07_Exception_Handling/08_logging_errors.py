"""
Logging Errors
"""

import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    result = 10 / 0

except Exception as error:
    logging.error(error)
    print("Error logged successfully.")