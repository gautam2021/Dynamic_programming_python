def rec_EqualSumPartition(wt,Sum,n):
    if Sum==0 :          # base condition
        return True
    if n==0:
        return False
    elif wt[n-1]>Sum:
        return rec_EqualSumPartition(wt,Sum,n-1)
    
    else:
        return rec_EqualSumPartition(wt,Sum-wt[n-1],n-1) or EqualSumPartition(wt,Sum,n-1)
    
        

def recursive_EqualSumPartition():
    print('give me values of weighted array   ')
    wt=list(map(int,input().split()))
    n=len(wt)
    
    
   
    
    
    if sum(wt)%2!=0:
        print("No , Equal Subset is not found with given sum")
    else:
        if rec_EqualSumPartition(wt,sum(wt)//2,n)==True:
            print('Yes , Found a subset with given sum')
        else:
            print("No , Equal Subset is not found with given sum")




def memo_EqualSumPartition(wt,Sum,n):
    t=[[-1 for i in range(Sum+1)] for j in range(n+1)]
    if Sum==0:
        return True
    if n==0:
        return False
    if t[n][Sum]!=-1:
        return t[n][Sum]
    elif wt[n-1]<=Sum:
        t[n][Sum]=memo_EqualSumPartition(wt,Sum-wt[n-1],n-1) or memo_EqualSumPartition(wt,Sum,n-1)
    else:
        t[n][Sum]=memo_EqualSumPartition(wt,Sum,n-1)
    return t[n][Sum]
    
   

def memoized_EqualSumPartition():
    print('give me values of weighted array   ')
    wt=list(map(int,input().split()))
    n=len(wt)
    
    
    if sum(wt)%2!=0:
        print("No , Equal Subset is not found with given sum")
    else:
        if memo_EqualSumPartition(wt,sum(wt)//2,n)==True:
            print('Yes , Found a subset with given sum')
        else:
            print("No , Equal Subset is not found with given sum")
        
    
def DP_EqualSumPartition(wt,Sum,n):
    t=[[0 for i in range(Sum+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(Sum+1):
            if i==0 or j==0 :
                t[i][j]=True
            elif wt[i-1]<=j:
                t[i][j]=t[i-1][Sum-wt[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][Sum]
                

def dp_EqualSumPartition():
    print('give me values of weighted array   ')
    wt=list(map(int,input().split()))
    
   
    
    n=len(wt)
    if sum(wt)%2!=0:
        print("No , Equal Subset is not found with given sum")
    else:
        if DP_EqualSumPartition(wt,sum(wt)//2,n)==True:
            print('Yes , Found a subset with given sum')
        else:
            print("No , Equal Subset is not found with given sum")

    
if __name__=='__main__':
    while True:
        print('\nPress 1 for Subset Sum using RECURSION: \n ')
        print('\nPress 2 for Subset Sum using MEMOIZATION_DP: \n ')
        print('\nPress 3 for Subset Sum using TOP-DOWN_DP: \n ')
        print('\nPress anything else for Quit:\n  ')
        x=int(input('Enter your choice.\n\n'))

        if x==1:
            recursive_EqualSumPartition()
        elif x==2:
            memoized_EqualSumPartition()
        elif x==3:
            dp_EqualSumPartition()
        else:
            print('Thanks !')
            break
            
