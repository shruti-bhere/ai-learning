"""
Datetime Module
"""

from datetime import datetime

today = datetime.now()

print(today)

print(today.date())

print(today.time())

print(today.strftime("%d-%m-%Y"))