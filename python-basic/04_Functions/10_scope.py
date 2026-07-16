"""
Variable Scope
"""

global_var = "Python"

def display():
    local_var = "AI"

    print(global_var)
    print(local_var)

display()