from tkinter import *
class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk()
    window.wm_title("BancoDB")

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")
    entnome = Entry(window, textvariable=txtNome, width=width_entry)
    entsobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entemail = Entry(window, textvariable=txtEmail, width=width_entry)
    entcpf = Entry(window, textvariable=txtCPF, width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window, text="Ver Todos")
    btnSearch = Button(window, text="Buscar")
    btnInsert = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Itens")
    btnDel = Button(window, text="Apagar Itens")
    btnClose = Button(window, text="Fechar")

    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entnome.grid(row=0, column=1, padx=50, pady=50)
    entsobrenome.grid(row=1, column=1)
    entemail.grid(row=2, column=1)
    entcpf.grid(row=3, column=1)
    listClientes.grid(row=0, column=2,rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnSearch.grid(row=5, column=0, columnspan=2)
    btnInsert.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def run(self):
        Gui.window.mainloop()