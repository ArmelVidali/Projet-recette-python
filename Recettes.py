########## Début Mise en page TKINTER #############



import tkinter as tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter.font import Font
from PIL import Image, ImageTk
import sqlite3



       
def popupwin_recette():  # Ouverture d'une pop-up avec deux champs d'entrée et boutons pour enregistrer
   #Fenetre
    pop= tk.Toplevel(fen)
    pop.geometry("450x150")
    pop.title("Ajouter une recette")

   #Entrées
    aliment_label = tk.Label(pop, text = "Aliment")
    aliment_label.grid(column = 0, row = 4)
   
    poid_label = tk.Label(pop, text = "Poid")
    poid_label.grid(column = 0, row = 5)

    recette_label = tk.Label(pop, text= "Nom de la recette")
    recette_label.grid(column = 0, row = 0)

    poidtotal_label = tk.Label(pop, text= "Poid total recette")
    poidtotal_label.grid(column = 0, row = 1)

    r_entry = tk.Entry(pop, width = 25) #Entrée nom recette
    r_entry.grid(column = 1, row = 0)

    poidtotal_entry = tk.Entry(pop, width = 25) #Entrée du poid total de la recette
    poidtotal_entry.grid(column = 1, row = 1)

    
    a_entry= tk.Entry(pop, width= 25) #Entrée nom aliment
    a_entry.grid(column = 1, row = 4)
   
    p_entry= tk.Entry(pop, width= 25) #Entrée poid aliment
    p_entry.grid(column = 1, row = 5)

        
    def enreg(): #Entrée de la recette + des kcal en fonction du poid ajouté en récupérant l'information de la table liste_aliments
        poid = p_entry.get()
        poid1 = float(poid)
        poidtotal =  poidtotal_entry.get()
        poidtotal1 = float(poidtotal)
        kcal = 0.0
        a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(a_entry.get(),)) #Verifier si l'aliment est dans la base de donnée
        results = a.fetchall()
        if results : #Si l'aliment existe, début de l'enregistrement de la recette
            a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(a_entry.get(),))
            results = a.fetchall()
            for  al , kc in results :
                kcal = kc 
            r.execute("INSERT INTO liste_recettes VALUES(:nom_recette, :aliment, :poid, :kcal, :poid_total)",{'nom_recette':r_entry.get(),'aliment':a_entry.get(),'poid':poid, 'kcal':kcal*poid1/100, 'poid_total' :poidtotal1 }) 
            a_entry.delete(0, "end")
            p_entry.delete(0, "end")
            data_recettes.commit()
        else : #Message d'erreur
            pop1 = tk.Toplevel(pop)
            pop1.geometry("480x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : cet aliment n'est pas dans la base de donnée!", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)

   #Boutons
    enreg = tk.Button(pop, text = "Enregistrer", command = enreg)
    enreg.grid(column = 1, row = 6)

def popupwin_aliments():  # Ouverture d'une pop-up avec deux champs d'entrée et boutons pour enregistrer des alients
   #Fenetre
    pop= tk.Toplevel(fen)
    pop.geometry("250x100")
    pop.title("Ajouter des aliments")

   #Entrées
    aliment_label = tk.Label(pop, text = "Aliment")
    aliment_label.grid(column = 0, row = 0)
   
    poid_label = tk.Label(pop, text = "Kcal/100g")
    poid_label.grid(column = 0, row = 1)

    a_entry= tk.Entry(pop, width= 25) #aliment
    a_entry.grid(column = 1, row = 0)
   
    k_entry= tk.Entry(pop, width= 25) #calorie de l'aliment
    k_entry.grid(column = 1, row = 1)
  
        
    def enreg_aliments(): # Enregistrement d'un aliment et des calories/100g
        check = a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(a_entry.get(),))
        results = a.fetchall()
        if results: #Si l'aliment est déjà dans la base de donnée : message d'erreur
            pop1 = tk.Toplevel(pop)
            pop1.geometry("480x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cet aliment est déjà dans la base de donnée !", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)          
        else : #Sinon, enrregistrement
            a.execute("INSERT INTO liste_aliments VALUES(:aliment, :kcal)",{'aliment':a_entry.get(),'kcal':k_entry.get()})
            data_aliments.commit()
            a_entry.delete(0, "end")
            k_entry.delete(0, "end")



    #Boutons
    enreg_aliments = tk.Button(pop, text = "Enregistrer", command = enreg_aliments)
    enreg_aliments.grid(column=1, row =2)

def popwin_suppaliment(): # Ouverture d'une pop-up avec un champ d'entrée pour supprimer des aliments
    pop= tk.Toplevel(fen)
    pop.geometry("250x100")
    pop.title("Supprimer des aliments")

    aliment_label = tk.Label(pop, text = "Aliment")
    aliment_label.grid(column = 0, row = 0)

    a_entry= tk.Entry(pop, width= 25)
    a_entry.grid(column = 1, row = 0)

    

    def supp_aliment(): #supprimer un aliment dans la base de donnée SQL
        check = a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(a_entry.get(),))
        results = a.fetchall()
        if results: #Si l'aliment est dans la base de donnée, suppression
            a.execute("DELETE FROM liste_aliments WHERE aliment = ?",(a_entry.get(),))
            a_entry.delete(0, "end")
            data_aliments.commit()
        else: #Sinon, erreur
            pop1 = tk.Toplevel(pop)
            pop1.geometry("485x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cet aliment n'est pas dans la base de donnée!", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)  
                  
    supp_aliments = tk.Button(pop, text = "Supprimer de la base de donnée", command = supp_aliment)
    supp_aliments.grid(column=1, row =2)

def popwin_supprecette(): # Ouverture d'une pop-up avec un champ d'entrée pour supprimer des recettes
    pop= tk.Toplevel(fen)
    pop.geometry("250x100")
    pop.title("Supprimer des recettes")

    recette_label = tk.Label(pop, text = "recette")
    recette_label.grid(column = 0, row = 0)

    r_entry= tk.Entry(pop, width= 25)
    r_entry.grid(column = 1, row = 0)
    

    def supp_recette(): #supprimer une recette dans la base de donnée SQL
        check = r.execute("SELECT * FROM liste_recettes WHERE nom_recette = ?",(r_entry.get(),))
        results = r.fetchall()
        if results :
            r.execute("DELETE FROM liste_recettes WHERE nom_recette = ?",(r_entry.get(),))
            r_entry.delete(0, "end")
            data_recettes.commit()
        else :
            pop1 = tk.Toplevel(pop)
            pop1.geometry("500x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cette recette n'est pas dans la base de donnée!", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)  
                        
    supp_aliments = tk.Button(pop, text = "Supprimer de la base de donnée", command = supp_recette)
    supp_aliments.grid(column=1, row =2)

    
def popwin_printaliment(): #Afficher un aliment et les kcal par portions
    pop= tk.Toplevel(fen)
    pop.geometry("250x100")
    pop.title("Calculer les kcal d'une portion d'aliment")

    aliment_label = tk.Label(pop, text = "Aliment")
    aliment_label.grid(column = 0, row = 0)

    a_entry= tk.Entry(pop, width= 25)
    a_entry.grid(column = 1, row = 0)

    poid_label = tk.Label(pop, text = "Poid")
    poid_label.grid(column = 0, row = 1)

    p_entry= tk.Entry(pop, width= 25)
    p_entry.grid(column = 1, row = 1)


    def print_aliment():
        poid = float(p_entry.get())
        aliment = a_entry.get()
        check = a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(aliment,))
        results1 = a.fetchall()
        if results1: #Si l'aliment est déjà dans la base de donnée : message d'erreur
            a.execute("SELECT * FROM liste_aliments WHERE aliment = ?",(aliment,))
            results = a.fetchall()
            print_c =''
            for r , i in results:
                if aliment[0] in ['a','e','i','o','u','y','h']: #apostrophe si l'aliment commence par une voyelle ou h 
                    print_c =  print_c + str(poid) + " grammes d'" + aliment + " = " + str(poid*i/100) + "kcal" #Affichage des kcal/poid entré par l'utilisateur
                else :
                    print_c =  print_c + str(poid) + " grammes de " + aliment + " = " + str(poid*i/100) + "kcal"
            affichage_calories = tk.Label(pop, text = print_c)
            affichage_calories.grid(row = 4, column =1, columnspan = 5)
        else:
            pop1 = tk.Toplevel(pop)
            pop1.geometry("490x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cet aliment n'est pas dans la base de donnée !", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)
            
       
        a_entry.delete(0, "end")
        p_entry.delete(0, "end")
        data_aliments.commit()
       
                
    supp_aliments = tk.Button(pop, text = "Calculer les calories", command = print_aliment)
    supp_aliments.grid(column=1, row =2)    



def popwin_printrecette():
    pop= tk.Toplevel(fen)
    pop.geometry("350x200")
    pop.title("Calculer les kcal d'une portion de recette")

    recette_label = tk.Label(pop, text = "Nom de la recette")
    recette_label.grid(column = 0, row = 0)

    r_entry= tk.Entry(pop, width= 25) #entrée du nom de la recette
    r_entry.grid(column = 1, row = 0)

    poid_label = tk.Label(pop, text = "Poid de la portion")
    poid_label.grid(column = 0, row = 1)

    p_entry= tk.Entry(pop, width= 25) #entrée du poid de la recette
    p_entry.grid(column = 1, row = 1)


    def print_recette():
        poid = float(p_entry.get())
        recette = r_entry.get()
        check = r.execute("SELECT * FROM liste_recettes WHERE nom_recette = ?",(recette,))
        results1 = r.fetchall()
        kcal_total = 0 #Kcal total de la recette, en ajoutant un a un les kcal des aliments
        poid_totalr = 0 #poid total de la recette
        if results1: 
            r.execute("SELECT * FROM liste_recettes WHERE nom_recette = ?",(recette,))
            results = r.fetchall()
            print_c =''
            for nr , al , pd , kc , pdt in results: #Nom de la recette, aliment, poid, kcal, poid total
                if recette[0] in ['a','e','i','o','u','y','h']: #apostrophe si l'aliment commence par une voyelle ou h
                    kcal_total = kcal_total + kc
                    poid_totalr = pdt
                    print_c  = str(poid) + " grammes d'" + recette + " = " #Affichage des kcal/poid entré par l'utilisateur
                else :
                    kcal_total = kcal_total + kc
                    poid_totalr = pdt
                    print_c = str(poid) + " grammes de " + recette + " = "
            
            
            affichage_calories = tk.Label(pop, text = print_c + str(poid*kcal_total/poid_totalr)+"kcal")
            
            affichage_calories.grid(row = 4, column =1, columnspan = 5)
        
        else:
            pop1 = tk.Toplevel(pop)
            pop1.geometry("500x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cette recette n'est pas dans la base de donnée!", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)
            
        r_entry.delete(0, "end")
        p_entry.delete(0, "end")
        data_aliments.commit()
        
    def print_ingredients():
        check = r.execute("SELECT * FROM liste_recettes WHERE nom_recette = ?",(r_entry.get(),))
        results1 = r.fetchall()
        ingredients = ''
        if results1: 
            r.execute("SELECT * FROM liste_recettes WHERE nom_recette = ?",(r_entry.get(),))
            results = r.fetchall()
            for nr , al , pd , kc , pdt in results: #Nom de la recette, aliment, poid, kcal, poid total
                ingredients = ingredients + al + " : " + str(pd) + " grammes" + "\n"
                    
            affichage_calories = tk.Label(pop, text = ingredients)
            affichage_calories.destroy()
            affichage_calories = tk.Label(pop, text = ingredients)
            affichage_calories.grid(row = 4, column =1, columnspan = 5)
        
        else:
            pop1 = tk.Toplevel(pop)
            pop1.geometry("500x29")
            pop1.title("Erreur")
            erreur = tk.Label(pop1, text="Erreur : Cette recette n'est pas dans la base de donnée!", bg = 'red', font = ("Arial", 15))
            erreur.grid(column = 0, row =0)
            
        r_entry.delete(0, "end")
        p_entry.delete(0, "end")
        data_aliments.commit()
        
       
                
    calcul_kcal = tk.Button(pop, text = "Calculer les calories", command = print_recette)
    calcul_kcal.grid(column=1, row =2)

    affichage_ingredients = tk.Button(pop, text = "Afficher les ingrédients de la recette", command = print_ingredients)
    affichage_ingredients.grid(column=1, row =3)


 

fen = tk.Tk() ######### fenetre ########
fen.title("Receuil de cuisine")
fen.geometry('960x500')
background = ImageTk.PhotoImage(file="background.jpg")

canvas= tk.Canvas(fen, width = 960, height = 500)
canvas.grid(columnspan= 100, rowspan=50)

canvas.create_image(0,0, image =background,anchor = "nw")

typo = Font(family="Times", size = 20, weight = "bold" ,slant = "roman")

data_aliments = sqlite3.connect('aliments2.db')
a = data_aliments.cursor()
a.execute("""CREATE TABLE liste_aliments("aliment" str, "kcal" float)""")


data_recettes = sqlite3.connect('recettes.db')
r = data_recettes.cursor()
r.execute("""CREATE TABLE liste_recettes("nom_recette" str, "aliment" str ,"poid" float, "kcal" float, "poid_total" float)""")



#######texte de la page de garde##############
    
ajouter_label = tk.Label(fen, text = "Ajouter", height = 1, font = typo, bg = "green", fg = "white")
ajouter_label.grid(column=0, row = 35)



supp_label = tk.Label(fen, text = "Supprimer",height = 1 ,font = typo, bg="red", fg = "white")
supp_label.grid(column=53, row = 35)

afficher_label = tk.Label(fen, text = "Afficher",height = 1, font= typo, bg = "blue", fg = "white")
afficher_label.grid(column=97, row = 35)


###### Boutons de la page de garde###########
bou1 = tk.Button(fen, text = 'Recette', command=popupwin_recette) #Pop up : ajouter  recettes
bou1_window = canvas.create_window(50 , 450, anchor= 'center', window = bou1)

bou2 = tk.Button(fen, text = ' Aliment', command=popupwin_aliments) #Pop up :  ajouter  aliments
bou2_window = canvas.create_window(50 , 400, anchor= 'center', window = bou2)

bou3 = tk.Button(fen, text = ' Recette', command= popwin_supprecette) #Pop up : Supprimer recette
bou3_window = canvas.create_window(500 , 450, anchor= 'center', window = bou3)

bou4 = tk.Button(fen, text = ' Aliment', command=popwin_suppaliment) #Pop up : Supprimer aliment
bou4_window = canvas.create_window(500 , 400, anchor= 'center', window = bou4)



bou5 = tk.Button(fen, text = ' Recette', command=popwin_printrecette) #Pop up : afficher recette
bou5_window = canvas.create_window(900 , 450, anchor= 'center', window = bou5)

bou6 = tk.Button(fen, text = ' Aliment', command= popwin_printaliment) #Pop up : afficher aliment
bou6_window = canvas.create_window(900 , 400, anchor= 'center', window = bou6)


fen.mainloop()

########## Fin Mise en page TKINTER #############

    
        

    


        
