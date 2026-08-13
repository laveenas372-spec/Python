class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        pre, suf, maxLen = [0] * (4 * n), [0] * (4 * n), [0] * (4 * n)
        leftChar, rightChar = [""] * (4 * n), [""] * (4 * n)

        def pushUp(u, l, r):
            mid = (l + r) >> 1
            left_u, right_u = u << 1, u << 1 | 1
            leftChar[u] = leftChar[left_u]
            rightChar[u] = rightChar[right_u]
            
            pre[u] = pre[left_u]
            if pre[left_u] == mid - l + 1 and rightChar[left_u] == leftChar[right_u]:
                pre[u] += pre[right_u]
                
            suf[u] = suf[right_u]
            if suf[right_u] == r - mid and rightChar[left_u] == leftChar[right_u]:
                suf[u] += suf[left_u]
                
            maxLen[u] = max(maxLen[left_u], maxLen[right_u])
            if rightChar[left_u] == leftChar[right_u]:
                maxLen[u] = max(maxLen[u], suf[left_u] + pre[right_u])
        
        # ... continued next slide ...
        def build(u,l,r):
            if l ==  r:
                pre[u] = suf[u] = maxLen[u] = 1
                leftChar[u] = rightChar[u] = s[l]
                return
            mid = (l + r) >> 1
            build(u << 1,l,mid)
            build(u << 1| 1,mid + 1 ,r)
            pushUp(u,l,r)

        def update(u,l,r,pos,ch):
            if l == r:
                leftChar[u] = rightChar[u] = ch
                return
            mid = (l + r) >> 1
            if pos <= mid:
                update(u << 1,l,mid,pos,ch)
            else:
                update(u << 1 | 1,mid + 1,r,pos,ch)
            pushUp(u,l,r)
        
        build(1,0,n-1)
        ans = []
        for i in range(len(queryIndices)):
            update(1,0,n-1,queryIndices[i],queryCharacters[i])
            ans.append(maxLen[1])
        return ans