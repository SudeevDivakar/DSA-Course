def minWindow(s, t):
    #write code here
    if t == '':
        return ''
        
    t_freq, s_freq = {}, {}
    for i in t:
        if i not in t_freq:
            t_freq[i] = 1
        else:
            t_freq[i] += 1
            
    need = len(t_freq)
    have = 0
    
    res = [-1, - 1]
    res_length = float('inf')
    
    l = 0
    for r in range(len(s)):
        if s[r] not in s_freq:
            s_freq[s[r]] = 1
        else:
            s_freq[s[r]] += 1
            
        if s[r] in t_freq and s_freq[s[r]] == t_freq[s[r]]:
            have += 1
        
        while have == need:
            if r - l + 1 < res_length:
                res_length = r - l + 1
                res = [l, r]
            
            s_freq[s[l]] -= 1
            if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                have -= 1
                
            l += 1
        
    if res_length == float('inf'):
        return ''
    
    else:
        return s[res[0]: res[1] + 1]
        
        
# Time Complexity = O(n + m)  where n -> length of string t, m -> length of string s
# Space Complexity = O(us + ut)  where us -> unique characters in string s, ut -> unique characters in string t