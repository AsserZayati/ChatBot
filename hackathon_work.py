from tkinter import *
from tkinter.scrolledtext import ScrolledText

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


L=["Bonjour",
"Salut , je suis votre chatbot 'HeadMaster Bot' ,comment puis-je vous aider?",
"Quel type de maison puis-je construire?",
"Vous pouvez construire une maison individuelle, jumelйe, а йtage, avec plusieurs unitйs (comme une maison composйe), selon vos besoins et votre budget.",
"Oщ puis-je construire ma maison en Tunisie?",
"Cela dйpend de votre terrain ou du lieu souhaitй. Les zones les plus populaires sont Tunis, Ariana, Sousse, Nabeul, et Hammamet. Assurez-vous que le terrain est en zone constructible.",
"Combien coыte une maison composйe?",
" En moyenne, le prix varie entre 1 200 et 1 800 TND/mІ pour la construction. Le coыt total dйpend de la superficie, du nombre de piиces, des matйriaux choisis et de la rйgion.",
"Puis-je avoir une estimation du coыt total?",
"Bien sыr. Dites-nous la surface souhaitйe, le type de maison et la rйgion. Nous vous fournirons une estimation personnalisйe.",
"Est-ce que vous proposez des solutions de financement?",
"Nous pouvons vous orienter vers des partenaires bancaires pour un crйdit immobilier, ou vous aider а monter un dossier de financement.",
"Est-ce que vous fournissez les plans de la maison?",
"Oui, nous proposons la conception de plans personnalisйs selon vos besoins, ou nous pouvons travailler а partir de vos idйes.",
"Combien de temps dure la construction?",
"En moyenne, entre 6 et 12 mois selon la complexitй du projet et les conditions climatiques.",
"Puis-je suivre lavancement des travaux?",
"Oui, nous proposons un suivi rйgulier avec des photos, des rapports et la possibilitй de visiter le chantier.",
"Faut-il un permis de construire?",
"Oui, toute construction en Tunisie nйcessite un permis dйlivrй par la municipalitй. Nous pouvons vous accompagner dans les dйmarches.",
"Le terrain doit-il кtre titrй?",
"Oui, il est indispensable davoir un titre foncier en rиgle pour lancer une construction lйgale.",
"Ou je peut construire ma maison?",
"Votre maison peut etre deplacer dans n'importe quel endroit ,saud dans les milieux qui sont interdit pas la loi."]


chatbot1=ChatBot('HeadMaster Bot')
trainer1=ListTrainer(chatbot1)
trainer1.train(L)

inter=Tk()
inter.geometry('1000x700')

# where the response is gonna show
Scrolled_Text=ScrolledText(inter,width=700,height=35)
Scrolled_Text.pack()

# where the user is gonna ask the question
def msgsend():
    msg=sendPlace.get()
    Scrolled_Text.configure(state="normal")
    Scrolled_Text.insert(INSERT,"You:"+msg.lower()+"\n")
    Scrolled_Text.insert(INSERT,"Chatbot:")
    Scrolled_Text.insert(INSERT,chatbot1.get_response(msg.lower()))
    Scrolled_Text.insert(INSERT,"\n")

def key_handler_function(event):
    msgsend()
    
sendPlace=Entry(inter,font=('Helvetica Neue',16))
sendPlace.pack(side=LEFT)
sendPlace.place(y=600,width=900,height=60)
sendPlace.bind("<Return>", key_handler_function)


#the button  where the user is gonna click and get the answer
photo=PhotoImage(file='send.png')
send=Button(inter,text="submit",command=msgsend,image=photo)
send.pack(side=RIGHT)

inter.mainloop()



