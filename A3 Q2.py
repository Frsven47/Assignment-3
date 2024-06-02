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
        # Ensure num1 is the larger number and num2 is the smaller one
        if num2 == 0:
            return num1
        else:
            return EuclideanAlgorithm.gcd(num2, num1 % num2)

# Example usage
if __name__ == "__main__":
    num1 = 64
    num2 = 88
    result = EuclideanAlgorithm.gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")
