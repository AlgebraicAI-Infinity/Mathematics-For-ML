class Solution:
    """
    A class to perform probability calculations related to conditional probability.

    Conditional Probability:
    - P(A | B) : Likelihood of event A occurring given that event B has already occurred.
    - P(A ∩ B) : Likelihood of two events occurring simultaneously (also known as the intersection of A and B).
    - The formula for conditional probability is:
        P(A | B) = P(A ∩ B) / P(B)
    """

    def conditional_probability(self, pb: float, pab: float) -> float:
        """
        Calculate the conditional probability P(A | B), given P(B) and P(A ∩ B).

        Formula: P(A | B) = P(A ∩ B) / P(B)

        Parameters:
        pb (float): Probability of event B (P(B))
        pab (float): Probability of both events A and B occurring simultaneously (P(A ∩ B))

        Returns:
        float: The conditional probability P(A | B)
        """
        # Calculate conditional probability using the formula
        result = pab / pb
        return result
    
    """ Scratch implementation using set intersection """
    def conditional_probabilty_scratch(self, A: set, B: set) -> float:
        """
        Calculate the conditional probability P(A | B) using set operations.

        Formula: P(A | B) = |A ∩ B| / |B|

        Parameters:
        A (set): A set representing event A
        B (set): A set representing event B

        Returns:
        float: The conditional probability P(A | B)
        """
        # A ∩ B represents the intersection of sets A and B
        A_B = A & B  # A intersection B
        # Conditional probability is the size of the intersection divided by the size of B
        result = len(A_B) / len(B)
        return result


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Define the probabilities and sets
    pb, pab = 0.5, 0.2  # Example values for P(B) and P(A ∩ B)
    A = {1, 2, 3, 4}  # Set A
    B = {2, 4}        # Set B

    # Calculate the conditional probability using the formula
    ans = sol.conditional_probability(pb, pab)
    
    # Calculate the conditional probability using set intersection
    ans1 = sol.conditional_probabilty_scratch(A, B)
    
    # Output the results
    print("Conditional Probability using formula:", ans)
    print("Conditional Probability using set operations:", ans1)
