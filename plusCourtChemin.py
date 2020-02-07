import random

tgeninchange=50 ###a choisir en fonction de la taillepop###
tElet=50
tReprod=20
taillePop=100
tMutation=3 ###a choisir en fonction de la longeur des genes###
listeV=[1,2,3,4,5,6]
liste=[[0,25,48,16,32,6],[25,0,81,76,25,52],[48,81,0,1,48,37],[16,76,1,0,20,59],[32,25,48,20,0,98],[6,52,37,59,98,0]]

pop=[ [3, 2, 5, 4, 6, 1],  [2, 1, 6, 3, 5, 4], [5, 3, 4, 6, 2, 1], [3, 5, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1]]
newPop=[]
 
def test(listeV):###genere des parcours au hasard###
    for k in range(len(listeV)-1):
            hub=listeV[k]
            n=random.randint(0,5)
            listeV[k]=listeV[n]
            listeV[n]=hub
    return listeV
          
def initialisation(taillePop):###entrer un entier positif###
    pop=[]
    for h in range(1,taillePop+1,1):
        pop.append(test([1,2,3,4,5,6]))
    return pop

def fitness(chrom):###entrer un chromosome correcte comprenant 1,2,3,4,5,6###
    S=0
    for k in range(0,len(chrom)-1,1):
        liste2=liste[chrom[k]-1]
        S=S+liste2[chrom[k+1]-1]
    return S
        
def trieFit(pop):###Trie une liste de fitness inutile seul###
    fit=[]
    for k in range (0,len(pop)):
        fit.append(fitness(pop[k]))
    fit.sort()
    return fit

def triepop(pop):
    triePop=[]
    fit=trieFit(pop)
    for k in range (0,len(fit)):
        fitneS=fit[k]
        for i in range(0,len(pop)):
            if fitness(pop[i])==fitneS:
                triePop.append(pop[i])
                break
    print (len(triePop))
    return triePop
            
def generationSuivante(pop,tMutation,tgeninchange):###pop deja triee svp###
    pop2=[]
    for k in range (0,tgeninchange):
        pop2.append(pop[k])
    while len(pop2)<len(pop):
        gf=geneF2(pop,tMutation)
        pop2.append(gf)
    return pop2
        
                

def geneF2(pop,tMutation):###cree un gf###
    gp=pop[random.randint(0,len(pop)-1)]
    gm=pop[random.randint(0,len(pop)-1)]
    gf=[]
    while gp==gm:
        gm=pop[random.randint(0,len(pop)-1)]
    for i in range(0,tMutation):
        gf.append(gp[i])
    c=tMutation
    ens1=set(gm)
    ens2=set(gf)
    g1=list(ens1-ens2)
    gfp2=ordreApp(gm,g1,c)
    gf.extend(gfp2)
    return gf
    

def ordreApp(gm,g1,c):###g1 ordre croissant=> ordre gm###
    gfp2=[]
    while len(gfp2)!=len(g1):
        if set([gm[c]])&set(g1)!=set():
            j=set([gm[c]])&set(g1)
            gfp2.append(list(j))
        c=c+1
        if c>=len(gm):
            c=0
    gfp22=[]
    for k in range (0,len(gfp2)):
        l=gfp2[k]
        gfp22.append(l[0])
    
    return gfp22
        
    
    
def algofinal(tpop,nbgeneration,tMutation,tgeninchange):
    t=initialisation(tpop)
    for k in range (0,nbgeneration):
        t=generationSuivante(t,tMutation,tgeninchange)
    t=triepop(t)
    m=t[0]
    print(m,fitness(m))
    return m
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    