class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalalice= sum(aliceSizes)
        totalbob= sum(bobSizes)
        targettotal =(totalalice +totalbob)//2
        for alicecandy in aliceSizes:
            bobcandy=alicecandy+(targettotal-totalalice)
            if bobcandy in bobSizes:
                return[alicecandy,bobcandy]
