# def get_fractional_part(number):
#     """
#     Returns the fractional part of a floating-point number.
# 
#     Args:
#         number (float): The floating-point number to extract the fractional part from.
# 
#     Returns:
#         float: The fractional part of the input number.
#     """
#     return number - int(number)
# 
# a = get_fractional_part(3.14)
# print(a)

def fractional_part(x):
    """
    Calculate the fractional part of a given number.

    Parameters:
    x (float or int): The number to calculate the fractional part from.

    Returns:
    float: The fractional part of the number
    """
    
    # Ensure the number is a float (in case it's an integer)
    if isinstance(x, int):
        x = float(x)
    
    # Calculate the fractional part using the modulus operator
    return x - int(x)


print(fractional_part(6.14))

