class Solution:

    def restoreIpAddresses(self,s: str) -> List[str]:
        
        ans=[]
        def is_valid(s):
            temp=s.split(".")

            #checking if the length of the last value is more than 3 or not, if more than 3 then definitely note possible
            if(len(temp[-1])>3):
                return
            
            for val in temp:

                #for strings less than size 10 this case might arise                
                if val=="": return

                #checking the 0 logic
                if(len(val)>1 and val[0]=='0'): return
                
                #checking the value cant exceed 255 logic
                if(int(val)>255): return

            ans.append(s)
                        

        def backtrack(prev_part,count,s):
            if(count==3):
                is_valid(prev_part+s)
                #print(prev_part+s)
                return
            for i in range(1,4):
                backtrack(prev_part+s[:i]+".",count+1,s[i:])
                


        
        backtrack("",0,s)
        return ans