#Implement display_dico(dico) a Python function that takes a dictionary as 
#parameter and print the content of the dictionary, one paired element per line

def dispaly_dico(dico):
    for x, y in dico.items():
        print (x , "-->" , y)
    
dispaly_dico({'un' : 1, 'deux' : 2, 'trois' : 3})