class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        check = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for l in s:
            # print(1)
            if l in ["(", "[", "{"]:
                st.append(l)
            else:
                if len(st) >=1:
                    p = st.pop()
                    # print(check[p])
                    if check[p] == l:
                        
                        continue
                    else:
                        return False
                        
                else:
                    return False

        return len(st) == 0


        # s1 = []
        # s2 = []
        # s3 = []

        # for l in s:
        #     if l == "(":
        #         s1.append("(")
        #     elif l == "{":
        #         s2.append("{")
        #     elif l == "[":
        #         s3.append("[")
        #     elif l == ")":
        #         if len(s1) >=1:
        #             s1.pop()
        #         else:
        #             return False
        #     elif l == "}":
        #         if len(s2) >= 1:
        #             s2.pop()
        #         else:
        #             return False
        #     else:
        #         if len(s3) >=1:
        #             s3.pop()
        #         else:
        #             return False
        # return len(s1) == 0 and len(s2) == 0 and len(s3) == 0

        
        