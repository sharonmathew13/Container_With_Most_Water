class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ti=0
        for i in range(len(height)-1):
            
            for j in range(i,len(height)):
                if height[i] >= height[j]:
                    if ti < height[j]*(j-i):
                        ti=height[j]*((j-i))
                    
                
                else:
                    if ti < height[i]*(j-i):
                        ti=height[i]*((j-i))
                    
                
        return ti
