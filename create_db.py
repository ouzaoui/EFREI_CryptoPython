import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TRAMBLEY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '2789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))


connection.commit()
connection.close()
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fonction pour enregistrer un nouveau client dans la base de données
def enregistrer_client():
    try:
        # Récupération des valeurs des champs de saisie
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        adresse = entry_adresse.get()

        # Vérification que tous les champs sont remplis
        if not nom or not prenom or not adresse:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")
            return

        # Connexion à la base de données
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        # Insertion des données du nouveau client dans la table clients
        cursor.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", (nom, prenom, adresse))

        # Validation de la transaction
        conn.commit()

        # Fermeture de la connexion
        conn.close()

        # Affichage d'un message de succès
        messagebox.showinfo("Succès", "Le client a été enregistré avec succès.")

        # Effacement des champs de saisie
        entry_nom.delete(0, tk.END)
        entry_prenom.delete(0, tk.END)
        entry_adresse.delete(0, tk.END)

    except Exception as e:
        # Affichage d'une fenêtre d'erreur en cas d'échec
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Enregistrement d'un nouveau client")

# Création des champs de saisie
label_nom = tk.Label(fenetre, text="Nom:")
label_nom.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack(pady=5)

label_prenom = tk.Label(fenetre, text="Prénom:")
label_prenom.pack()
entry_prenom = tk.Entry(fenetre)
entry_prenom.pack(pady=5)

label_adresse = tk.Label(fenetre, text="Adresse:")
label_adresse.pack()
entry_adresse = tk.Entry(fenetre)
entry_adresse.pack(pady=5)

# Création du bouton pour enregistrer le nouveau client
btn_enregistrer = tk.Button(fenetre, text="Enregistrer le client", command=enregistrer_client)
btn_enregistrer.pack(pady=20)

# Fonction pour fermer l'application
def quitter_application():
    fenetre.destroy()

# Création du bouton pour quitter l'application
btn_quitter = tk.Button(fenetre, text="Quitter", command=quitter_application)
btn_quitter.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()
