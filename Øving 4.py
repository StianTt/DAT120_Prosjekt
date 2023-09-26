#oppgave d

def antal_elem_storre_eller_lik(x,y):
    for i in x:
        if i >= y:
            print (i)
#oppgave e
def differansen_mellom_neste_og_siste(x):
    v=[]
    for i in range (len(x)-1):
        v.append(x[i]-x[len(x)-1])
    return v

#oppgave e.a frivillig 1

#def numeriske_deriverte(x,y,h):
   # l=[]
   # for i in range (len (x)):
       # der=()/h


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

#a,b= liner_reg(x,y,n)
#funksjon som regner ut verdi

def trend(x,a,b): 
    verdi=[]
    for i  in range (len(x)):
        a.append(a*x[i]+b)
    return verdi
    

