# find the middle of the list

def mid_list(my_list:list):
    n=len(my_list)
    mid_list_index=n//2
    mid_list_value=my_list[mid_list_index]
    return mid_list_value

if __name__=="__main__":
    ll = [12, 45, 67, 87, 49, 98, 56]
    val=mid_list(ll)
    print(f"Value of the middle in list: {val}")
