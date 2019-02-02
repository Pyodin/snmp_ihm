#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from tkinter import *
from pysnmp.hlapi import *
import v3_config as fv3

class Simpleapp_tk(Tk):

#       |
#       |
#       |           PLUS BAS 
#       |
#       \/

    test=0  # <========== JE VOUDRAI MODIFIER CETTE VALEUR A PARTIR DE LAUTRE CLASSE 

#       /\
#       |
#       |           PLUS HAUT 
#       |
#       |

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("900x500")

        self.ip = StringVar()
        self.port = IntVar()
        self.oip = StringVar()
        self.version = StringVar()
        self.type = StringVar()
        self.community = StringVar()
        self.max_rep = IntVar()
        self.retries = IntVar()
        self.timeout = IntVar()

        #snmp v3
        self.context_engine = StringVar()
        self.context_name = StringVar()
        self.username = StringVar()
        self.auth_protocol = StringVar()
        self.auth_password = StringVar()
        self.privacy_password = StringVar()

        self.default()

        self.initialize()


    def initialize(self):

    #==============MENU==========================================
        self.menubar = Menu(self)
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # create more pulldown menus
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.hello)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # display the menu
        self.config(menu=self.menubar) 
        
    #================Frame1========================================
        self.frame1 = LabelFrame(self)
        self.frame1.grid(row=0, column=0,  padx=10, sticky='ns')

        Label(self.frame1, text="Ip Address").grid(row=0, column=0, padx=5, pady=5)
        Label(self.frame1, text="Port").grid(row=1, column=0, padx=5, pady=5)
        Label(self.frame1, text="OIP").grid(row=2, column=0, padx=5, pady=5)
        Label(self.frame1, text="SNMP Version").grid(row=3, column=0, padx=5, pady=5)
        Label(self.frame1, text="Request type").grid(row=4, column=0, padx=5, pady=5)
        Label(self.frame1, text="Community").grid(row=5, column=0, padx=5, pady=5)
        Label(self.frame1, text="Max rep").grid(row=6, column=0, padx=5, pady=5)
        Label(self.frame1, text="Retries").grid(row=7, column=0, padx=5, pady=5)
        Label(self.frame1, text="Timeout").grid(row=8, column=0, padx=5, pady=5)

        Entry(self.frame1, textvariable=self.ip).grid(row=0, column=1, padx=5, pady=5)   
        Entry(self.frame1, textvariable=self.port).grid(row=1, column=1, padx=5, pady=5)   
        Entry(self.frame1, textvariable=self.oip).grid(row=2, column=1, padx=5, pady=5)   

        self.miniframe = Frame(self.frame1)                             #version et config v3
        self.miniframe.grid(row=3, column=1, padx=5, pady=5)
        self.listeversion = ['v1', 'v2', 'v3']
        self.opt_menu= OptionMenu(self.miniframe, self.version, *self.listeversion)
        self.opt_menu.grid(row=0, column = 0, sticky='w')
        Button(self.miniframe, text='v3 Config', command=self.v3_bouton).grid(row=0, column=1, sticky='e')

        self.listeOptions2 = ['Get', 'Set', 'Bulk']                     #request type
        self.opt_menu= OptionMenu(self.frame1, self.type, *self.listeOptions2)
        self.opt_menu.grid(row=4, column = 1, padx=5, pady=5)

        Entry(self.frame1, textvariable=self.community).grid(row=5, column=1, padx=5, pady=5)   
        Entry(self.frame1, textvariable=self.max_rep).grid(row=6, column=1, padx=5, pady=5)   
        Entry(self.frame1, textvariable=self.retries).grid(row=7, column=1, padx=5, pady=5)   
        Entry(self.frame1, textvariable=self.timeout).grid(row=8, column=1, padx=5, pady=5)   

        self.default_bt = Button(self.frame1, text="default", command=lambda:self.default()) # bouoton default
        self.default_bt.grid(row=9, column=0, sticky='ws')

        self.send_bt = Button(self, text='Send', command = self.send_bouton )            #bouton send
        self.send_bt.grid(row=2, sticky = 'ew', padx=10)

        #==================Frame2======================================
        self.frame2 = LabelFrame(self)
        self.frame2.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        self.text1 = Text(self.frame2, wrap=WORD)            # text
        self.text1.grid(row=0, column=0, sticky='e')

        self.scrollbar_t1 = Scrollbar(self.frame2)              #scrollbar text
        self.scrollbar_t1.config(command=self.text1.yview)
        self.scrollbar_t1.grid(row=0, column=1, sticky='nse')
        self.text1.config(yscrollcommand=self.scrollbar_t1.set)

        self.clr1 = Button(self.frame2, text="clear")               #bouton clear
        self.clr1.config(command=lambda: self.text1.delete('1.0', END))
        self.clr1.grid(row=1, column=0, pady=5, sticky='e')
        


    def exit_B(self):
        sys.exit()

    def hello(self):
        print("hello!")

    def default(self):
        self.ip.set('demo.snmplabs.com')
        self.port.set(161)
        self.oip.set('sysLocation')
        self.version.set("v2")
        self.type.set("Get")
        self.community.set("public")
        self.max_rep.set(10)
        self.retries.set(0)
        self.timeout.set(500)

        #snmp v3
        #self.context_engine.set()
        #self.context_name.set()
        self.username.set('bootstrap')
        self.auth_protocol.set('MD5')
        self.auth_password.set('temp_password')
        self.privacy_password.set('DES')
        

    def v3_bouton(self):
        self.v3 = fv3.V3_config(self)
        self.v3.title("SNMPv3 Config")
        self.v3.mainloop()


    def send_bouton(self):
        print(self.test)

"""
        g = getCmd(SnmpEngine(),
        CommunityData(self.community.get(), mpModel=1),
        UdpTransportTarget((self.ip.get(), self.port.get())),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', self.oip.get(), 0)))

        errorIndication, errorStatus, errorIndex, varBinds = next(g)

        if errorIndication: print(errorIndication)

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?')
                )
            
        else:
            for varBind in varBinds:
                self.text1.insert(END, (' = '.join([x.prettyPrint() for x in varBind])) + '\n')

      """  







     

#===== MAIN ========================================================

if __name__ == "__main__":
    mon_app = Simpleapp_tk(None)
    mon_app.title('Snmp IHM')
    mon_app.mainloop()





