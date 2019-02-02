from tkinter import *

class V3_config(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.geometry("380x220")

        self.context_engine = StringVar()
        self.context_name = StringVar()
        self.username = StringVar()
        self.auth_protocol = StringVar()
        self.auth_password = StringVar()
        self.privacy_password = StringVar()


#       |
#       |
#       |           PLUS BAS 
#       |
#       \/

        self.parent.test=1 #   <========== L'ERREUR EST ICI 

#       /\
#       |
#       |           PLUS HAUT 
#       |
#       |


    
        self.initialize()
        
        
       
        
    def initialize(self):
        self.frame1 = Frame(self)
        self.frame1.grid(row=0, column=0)
        
        Label(self.frame1, text="Context Engine ID").grid(row=0, column=0, padx=5, pady=5)
        Label(self.frame1, text="Context Name").grid(row=1, column=0, padx=5, pady=5)
        Label(self.frame1, text="Username").grid(row=2, column=0, padx=5, pady=5)
        Label(self.frame1, text="Authentification Protocol").grid(row=3, column=0, padx=5, pady=5)
        Label(self.frame1, text="Authentification Password").grid(row=4, column=0, padx=5, pady=5)
        Label(self.frame1, text="Privacy Password").grid(row=5, column=0, padx=5, pady=5)

        Entry(self.frame1).grid(row=0, column=1)
        Entry(self.frame1).grid(row=1, column=1)
        Entry(self.frame1).grid(row=2, column=1)
        Entry(self.frame1).grid(row=4, column=1)
        Entry(self.frame1).grid(row=5, column=1)

        #radiobutton
        self.miniframe = Frame(self.frame1)
        self.miniframe.grid(row=3, column=1)
        self.vals = ['A', 'B']
        self.etiqs = ['MD5', 'SHA']
        self.varGr = StringVar()
        self.varGr.set(self.vals[0])
        for i in range(len(self.etiqs)):
            self.b = Radiobutton(self.miniframe, variable=self.varGr,
             text=self.etiqs[i], value=self.vals[i], indicatoron=0)
            self.b.grid(row=0, column=i, pady=5, sticky='ew')


        self.frame2 = LabelFrame(self)
        self.frame2.grid(row=1, column=0, sticky='e', pady=10)
        Button(self.frame2, text='OK', command = self.ok_bouton).grid(row=1, column=0, sticky='w')
        Button(self.frame2, text='Cancel', command=self.destroy).grid(row=1, column=1) 


    def ok_bouton(self):
        """
        parent.context_engine = self.context_engine.get()
        parent.context_name = self.context_name.get()
        parent.username = self.username.get() 
        parent.auth_protocol = self.auth_protocol.get()
        parent.auth_password = self.auth_password.get()
        parent.privacy_password = self.privacy_password.get() 
        """

        self.destroy()




#===== MAIN ========================================================

if __name__ == "__main__":
    my_window = V3_config(None)
    my_window.title('Snmp-v3 config')
    my_window.mainloop()
