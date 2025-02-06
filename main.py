"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

year = int(input("Enter an integer between 1,000 and 10,000: "))

def is_leap(value):
    """
    This function determines whether an integer between 1000 and 10,000 is a leap year
    """
    return (value % 4 == 0 and value % 100 != 0) or value % 400 == 0

print(is_leap(year))
