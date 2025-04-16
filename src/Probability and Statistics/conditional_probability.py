


class Solution:
    """
        pb : probability of event b
        P(A ∩ B) : likelihood of two events occuring simultaneously . Here pab is same as P(A ∩ B)
        P(A | B) : likelihood of event  A occuring given that b has already occured .
        It is useful for Bayesian inference .
    """
    def conditional_probability(self,pb:float,pab:float)->float :
        result = pab/pb
        return result
    
    """ scratch implementation using set"""
    def conditional_probabilty_scratch(self,A:set,B:set)->float:
        # A = {1,2,3,4}
        # B = {2,4}

        A_B  = A&B  # A intersection B
        result = len(A_B)/len(B)
        return result

    


if __name__=="__main__":
    sol=Solution()
    pb,pab =0.5,0.2 
    A={1,2,3,4}
    B={2,4}
    ans=sol.conditional_probability(pb,pab)
    ans1=sol.conditional_probabilty_scratch(A,B)
    print(ans1)