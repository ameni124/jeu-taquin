from copy import deepcopy
def etat_depart ():
  t=[[1,2,3],[8,6,0],[7,5,4]]
  return t 
def estEtatFinal (t):
  return t==[[1,2,3],[8,0,4],[7,6,5]] 


def position_case_vide (t) :
  for i in range(len(t)):
    for j in range(len(t[i])):
      if t[i][j]==0 :
        return i,j

        
def numero(t, x, y) :
  return t[x][y]

def permuter (t, c1, c2):
  t2=deepcopy(t)
  p=t2[c1[0]][c1[1]]
  t2[c1[0]][c1[1]]= t2[c2[0]][c2[1]]
  t2[c2[0]][c2[1]]= p
  return t2

def afficher_taquin (t) :
    for i in range(len(t)):
      print("+---+---+---+")
      print("|",t[i][0],"|",t[i][1],"|",t[i][2],"|")
    print("+---+---+---+")

    
def transition(t):
  def trantion_possible (t,p):
    poses =[]
    if p[0]>0:
      poses.append((p[0]-1,p[1]))
    if p[1]>0:
      poses.append((p[0],p[1]-1))
    if p[0]< len(t)-1:
      poses.append((p[0]+1,p[1]))
    if p[1]< len(t)-1:
      poses.append((p[0],p[1]+1))
    return poses
  p=position_case_vide (t)
  poses = trantion_possible (t,p)
  trans = []
  for pose in poses :
    trans.append(permuter (t, p, pose)) 
  return trans






#****************Recherche en largeur**************

def recherche_largeur(t, ef):
  open=[]
  closed=[]
  etat=0
  open.append(t)
  niveau=[0]
  n=0
  print ("---------le niveau",n,"-------")
  while (open != []):
    m=n
    noeud = open.pop(0)
    closed.append(noeud)
    n=niveau.pop(0)
    if n!=m :
      print ("---------le niveau",n,"-------")
    print ("l'état ",etat)
    etat+=1
    afficher_taquin(noeud)
    if (noeud==ef):
      print("le resultat est dans l'etat ",etat-1)
      return noeud
    childs = transition(noeud)
    for child in childs :
      if not child in closed :
        open.append(child)
        niveau.append(n+1)

#****************Recherche en profondeur**************

def recherche_profondeur(t, ef):
  open=[]
  closed=[]
  niveau=0
  open.append(t)
  while (open != []):
    print ("le niveau ",niveau)
    niveau+=1
    noeud = open.pop(0)
    closed.append(noeud)
    afficher_taquin(noeud)
    if (noeud==ef):
      print("le resultat est dans le niveau",niveau-1)
      return noeud
    childs = transition(noeud)
    for child in childs :
      if not child in closed :
        open.insert(0,child)


#****************Recherche en profondeur limité**************

def dls(t,ef,open,level,limite):
  print("current level ",level)
  afficher_taquin(t)
  open.append(t)
  if (t==ef):
    print("result found ")
    return True
  print("result not found")
  if level==limite :
    return False
  childs = transition(t)
  for child in childs :
    if not child in open  :
      if dls(child,ef,open,level+1,limite):
        return True
      open.pop()
  return False

#****************Recherche a*  **************

def h(t, ef):
  cpt=0
  for i in range(len(t)):
    for j in range(len(t[i])):
      if (t[i][j] != ef[i][j])and (t[i][j]!=0):
        cpt=cpt+1;
  return cpt
def recherche_heuristique (t,ef):
  open=[]
  closed=[]
  niveau=0
  success = False
  open.append(t)
  while (open != [] and not success):
    noeud = open [0]
    print ("le niveau ",niveau)
    afficher_taquin(noeud)
    niveau+=1
    open.remove(noeud)
    closed.append(noeud)
    if (noeud==ef):
      success=True
      print("le resultat est dans le niveau",niveau-1)
      afficher_taquin(noeud)
    else :
      childs = transition(noeud)
      for child in childs :
        if (child in open)or(child in closed):
          childs.remove(child)
      open= open+childs
      open.sort(key=lambda e:(niveau+h(e,ef)))


#****************  Main **************

t=[]
t=etat_depart()
ef = [[1,2,3],[8,0,4],[7,6,5]] 
#BFS
#r=recherche_largeur(t, ef)
#DFS
#r=recherche_profondeur(t, ef)
#LDFS
open=[]
#dls(t,ef,open,0,5)
#a*
recherche_heuristique (t,ef)




        
