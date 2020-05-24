# recursive function
def possible_alignments(m, n):
    # f(0,n) = f(m,0) = f(0,0) = 1
    if (m == 0) or (n == 0) or (m==0 and n==0):  #  stopping condition
        return 1 # as per formula

      # f(i,j) = f(i-1,0) + f(0,j-1) + f(i-1,j-1)
    return possible_alignments(m-1, n) + possible_alignments(m, n-1) + possible_alignments(m-1, n-1)
    

l1_str = input("enter first sequence len ")
l2_str = input("enter second sequence len ")
l1 = int(l1_str) #converting strings we got for lengths to int to use
l2 = int(l2_str)

if (l1 == 0 and l2 == 0):  # empty string, only 1 alignment
    print("Only 1 possible alignment")
else:
    print("Number of possible alignments: ", possible_alignments(l1,l2)) # call recursive function
