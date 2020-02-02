if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=list(arr)
    arr2=set(arr1)
    arr2.remove(max(arr2))
    print(max(arr2))
    
