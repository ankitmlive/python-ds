# Python programme to get number of difference in two same type of strings

str1="anit"
str2="amiT"

def str_diff(str1, str2):
    n1=len(str1)
    n2=len(str2)
    counter=0
    position=[]
    if n1==n2:
        for i in range(n1):
            if str1[i] != str2[i]:
                position.append(i)
                counter += 1
        return counter, position
    else:
        print("Strings are different")
        return

if __name__=="__main__":
    counter, position=str_diff(str1, str2)
    print(f"Number of word difference is {counter} and position of difference is: {position}", )

        