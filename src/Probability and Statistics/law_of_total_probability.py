class Solution:
    """
    The law of total probability relates the probability of an event A to the
    probabilities of A given a partition of events {Bi}. It is used in scenarios with conditional
    dependencies.
    
    The formula for the law of total probability is:
    P(A) = P(A | B1) * P(B1) + P(A | B2) * P(B2)
    where {B1, B2} is a partition of the sample space.
    """

    def law_of_total_probabilty(self, pab1: float, pab2: float, pb1: float, pb2: float) -> float:
        """
        Calculate the total probability of event A using the law of total probability.

        Formula: P(A) = P(A | B1) * P(B1) + P(A | B2) * P(B2)

        Parameters:
        pab1 (float): Conditional probability P(A | B1)
        pab2 (float): Conditional probability P(A | B2)
        pb1 (float): Probability of event B1 (P(B1))
        pb2 (float): Probability of event B2 (P(B2))

        Returns:
        float: The total probability P(A) using the law of total probability
        """
        # Apply the law of total probability formula
        total_probability = pab1 * pb1 + pab2 * pb2
        return total_probability


if __name__ == '__main__':
    # Create an instance of the Solution class
    sol = Solution()

    # Define the probabilities
    pab1, pab2, pb1, pb2 = 0.3, 0.7, 0.4, 0.6  # Example values for P(A | B1), P(A | B2), P(B1), and P(B2)

    # Calculate the total probability using the law of total probability
    ans = sol.law_of_total_probabilty(pab1, pab2, pb1, pb2)

    # Output the result
    print("Total Probability P(A):", ans)
