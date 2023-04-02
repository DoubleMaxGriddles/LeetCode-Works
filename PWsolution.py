class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        pSet, n = set(password), len(password)

        catCt = 3- (bool(pSet & set(ascii_lowercase))+ 
                    bool(pSet & set(ascii_uppercase))+
                    bool(pSet & set('0123456789'   )))

        if n <  6:  return max(6 - n, catCt)        # Case 1

        repCt = [len(list(g)) for _, g in groupby(password)]
        repCt = [r for r in repCt if r > 2]

        if n > 20:                                  # Case 2: reduce to 6<= n <= 20
                                                    #         by eliminating triples
            repCt = [(r%3, r) for r in repCt]
            heapify(repCt)

            for i in range(n-20): 

                if not repCt: break

                _, r = heappop(repCt)
                if r > 3: heappush(repCt, ((r-1)%3, r-1))

            repCt = [r for _,r in repCt]
 
        return max(catCt, sum(r//3 for r in repCt))+max(0,n-20)   # Case3