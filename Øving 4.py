import matplotlib.pyplot as plt

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

#oppgave d,i
def antal_elem_storre_eller_lik(x,y):
    sum=0
    for i in x:
        if i >= y:
            sum+=1
    return sum
print(antal_elem_storre_eller_lik(temperaturer,20),"dager over 20")
print(antal_elem_storre_eller_lik(temperaturer,25),"dager over 25")
print(antal_elem_storre_eller_lik(temperaturer,30),"dager over 30")

#oppgave e,j
def differansen_mellom_neste_og_siste(x,a):
    v=[]
    index_liste=[]
    for i in range (len(x)-1):
        v.append(x[i+1]-x[i])
    
    for i in range (len(v)):
        index_liste.append(i)        
        if v[i] <a:
            print(i," Synkende")
        elif v[i] ==a:
            print(i," Uforandret")
        else:
            print(i, " Stigende")
    return  index_liste

differansen_mellom_neste_og_siste(temperaturer,0)

#oppgave f
def sammenhengende_sekvensen(x):
    y=0
    for i in range (len(x)-1):
        if x[i]==0:
            if x[i+1]==0:
                y+=1
            elif x[i+1]!=0:
                if x[i-1]==0:
                    y+=1    
    return y

#oppgave g
def liner_reg(x,y,n): 
    from statistics import mean 
    
    average_x=mean(x)
    average_y=mean(y)
    
    sum_above=0
    sum_under=0

    
    for i in range (n):
       sum_above +=((x[i]-average_x)*(y[i]-average_y))
       
       sum_under +=((x[i]-average_x)**2)
    
    a= sum_above/sum_under
    b=average_y - (a*average_x)
    return a,b
 
def trend(x,a,b): 
    verdi=[]
    for i  in range (len(x)):
        a.append(a*x[i]+b)
    return verdi

#oppgave h
def sorted_storre_enn_5(z):
    # Sort the list 'z' in ascending order
    z.sort()  # Remove the assignment to 'z' here
    
    storage = []
    
    # Iterate through the sorted list
    for i in z:  # No runtime error on this line after fixing the sorting
        if i > 5:
            # Check if the number 'i' is already in storage
            found = False
            for item in storage:
                if item[0] == i:
                    # If it's in storage, increment the count (item[1])
                    item[1] += 1
                    found = True
                    break
            
            # If not in storage, add it as [i, 1]
            if not found:
                storage.append([i, 1])
    
    return storage
