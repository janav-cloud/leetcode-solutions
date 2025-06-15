class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_str = str_num
        min_str = str_num
        
        for ch in str_num:
            if ch != '9':
                max_str = str_num.replace(ch, '9')
                break

        if str_num[0] != '1':
            min_str = str_num.replace(str_num[0], '1')
        else:
            for ch in str_num:
                if ch != '0' and ch != '1':
                    min_str = str_num.replace(ch, '0')
                    break
    
        return int(max_str) - int(min_str)