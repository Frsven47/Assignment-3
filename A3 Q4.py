class EuclideanAlgorithm:
    """
    A class to encapsulate the Euclidean Algorithm for finding
    the greatest common divisor (GCD) of two integers.
    """

    @staticmethod
    def gcd(num1, num2):
        """
        Calculate the greatest common divisor (GCD) of two integers
        using the Euclidean Algorithm.

        Args:
            num1 (int): The first integer.
            num2 (int): The second integer.

        Returns:
            int: The GCD of num1 and num2.
        """
        if num2 == 0:
            return num1
        else:
            return EuclideanAlgorithm.gcd(num2, num1 % num2)


def get_integer_input(prompt):
    """
    Get a valid integer input from the user.

    Args:
        prompt (str): The input prompt for the user.

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            value = int(prompt)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            prompt = input("Invalid input. Please enter a non-negative integer: ")


if __name__ == "__main__":
    print("Enter two non-negative integers to find their GCD using the Euclidean Algorithm.")
    num1 = get_integer_input(input("Enter the first number: "))
    num2 = get_integer_input(input("Enter the second number: "))
    result = EuclideanAlgorithm.gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")
