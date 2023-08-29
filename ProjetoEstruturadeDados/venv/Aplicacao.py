from Gui import *
import Backend as core

app = None

def view_comand():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_comand()

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_comand()

def del_command():
    id = selected[0]
    core.delete(id)
    view_comand()

def getSelectedRow(self, event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entnome.delete(0, END)
    app.entnome.insert(END, selected[1])
    app.entsobrenome.delete(0, END)
    app.entsobrenome.insert(END, selected[2])
    app.entemail.delete(0, END)
    app.entemail.insert(END, selected[3])
    app.entcpf.delete(0, END)
    app.entcpf.insert(END, selected[4])
    return selected
    
if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_comand)
    app.btnSearch.configure(command=search_command)
    app.btnInsert.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run