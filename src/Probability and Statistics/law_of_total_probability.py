

class Solution:
    """
        
        The law of total probability relates the probability of an event A to the
        probabilities of A given a partition of events {Bi}. It is used in scenarios with conditional
        dependencies.
    """
    def law_of_total_probabilty(self,pab1:float,pab2:float,pb1:float,pb2:float):
        total_probabilty = pab1*pb1+pab2*pb2
        return total_probabilty
    
    


if __name__=='__main__':
    sol = Solution()
    pab1,pab2,pb1,pb2 = 0.3,0.7,0.4,0.6
    ans = sol.law_of_total_probabilty(pab1,pab2,pb1,pb2)
    print(ans)