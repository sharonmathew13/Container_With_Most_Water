class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ti=0
        for i in range(len(height)-1):
            j=i+1
            while j< len(height):
                if height[i] >= height[j]:
                    if ti < height[j]*(j-i):
                        ti=height[j]*((j-i))
                else:
                    if ti < height[i]*(j-i):
                        ti=height[i]*((j-i))

                j=j+1
                    
                
                
                    
                
        return ti
