class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five = 0   # count of $5 bills
        ten = 0    # count of $10 bills
        
        for i in range(0, n):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:  # customer pays with 20
                if ten >= 1 and five >= 1:
                    # best case: give one $10 and one $5
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    # otherwise: give three $5 bills
                    five -= 3
                else:
                    return False
                    
        return True