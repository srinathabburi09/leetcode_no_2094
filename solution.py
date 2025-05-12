from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_perms = set()  # we use hashset because to store only unique permutations 
        for p in permutations(digits, 3):  #here p is a tuple which forms permutations over the digits array of length of 3 and 3 will be execulsive in the for loop
            if p[0] == 0:  #if p is a permutation of digits to 3, right so permutation of p at index 0 is zero we simply continue because we dont need that permutaion it will be of len 2
                continue
            num = p[0] * 100 + p[1] * 10 + p[2] # this creates a number which consists of 3-digit
            if num % 2 == 0: # if num is even 
                even_perms.add(num) # then we add it to set to remove duplicates so set contains only unique elements
        return sorted(list(even_perms))     # then we convert set into a list or array and sort it.
 
