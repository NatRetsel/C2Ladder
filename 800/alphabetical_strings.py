"""
    Given a string, determine if it can be formed through the following operation:
        - Begin with empty string, call S
        - At ith step, we can choose to append or prepend ith character to S

        Simulation with two pointers
        - locate position of 'a'
        - mark positions infront and back of 'a', make sure either one is 'a'+1 (like current string front and back)
        - locate position 'b' now, repeat
        - once both pointers occupy index 0 and len(s)-1, string is valid
        - otherwise we would've checked that at some point the digits are not sequential and terminated

"""



from typing import Dict

def solve()->None:
    s:str = input()
    ch_count:Dict[str,int] = {}
    a_idx:int = -1
    for i in range(len(s)):
        if s[i] == "a" and a_idx == -1:
            a_idx = i
        if s[i] not in ch_count.keys():
            ch_count[s[i]] = 1
        else:
            print("NO")
            return
    if a_idx == -1:
        print("NO")
        return
    if len(s) == 1:
        print("YES")
        return
    # str_front:int = a_idx if a_idx-1 < 0 else a_idx-1
    # str_back:int = a_idx if a_idx+1 == len(s) else a_idx+1
    str_front:int = a_idx-1
    str_back:int = a_idx+1

    curr_char:str = "a"
    while (str_front >= 0 and str_back <= len(s)-1):
        # print("str_front: {}, str_front char: {}, str_back: {}, str_back char: {}".format(str_front, s[str_front],str_back,s[str_back]))
        if (ord(s[str_front])-ord(curr_char) == 1):
            curr_char = s[str_front]
            str_front -= 1
        elif (ord(s[str_back])-ord(curr_char) == 1):
            curr_char = s[str_back]
            str_back += 1
        else:
            print("NO")
            return
    while (str_front >= 0):
        if (ord(s[str_front])-ord(curr_char) == 1):
            curr_char = s[str_front]
            str_front -= 1
        else:
            print("NO")
            return
    while (str_back <=len(s)-1):
        if (ord(s[str_back])-ord(curr_char) == 1):
            curr_char = s[str_back]
            str_back += 1
        else:
            print("NO")
            return


    print("YES")
    return


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
