import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import ticket_base


app=customtkinter.CTk()
app.title('Ticket Booking System')
app.geometry('600x600')
app.config(bg='#18161D')
app.resizable(False,False)

f1=('Arial',25,'bold')
f2=('Arial',13,'bold')
f3=('Arial',18,'bold')
def add_to_treeview():
    tickets=ticket_base.get_tc()
    for tc in tickets:
        if tc[2]>0:
            tree.insert('',END,values=tc)
def reservation(name,movie,quantity,price):
    customer_name=name
    movie_name=movie
    booked_qn=quantity
    ticket_price=price
    total_price=ticket_price*booked_qn
    
    return total_price

    
def booktc():
    customer_name=name_entry.get()
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose a ticket to book!')
    elif not customer_name:
        messagebox.showerror('Error','Enter Your Name!')
    else:
        row=tree.item(selected_item)['values']
        movie_name=row[1]
        ticket_price=row[3]
        booked_qn=int(variable1.get())
        if booked_qn>row[2]:
            messagebox.showerror('Error','Not Enough Tickets')
        else:
            ticket_base.upd_qn(row[0],booked_qn)
            add_to_treeview()
            total_price=reservation(customer_name,movie_name,booked_qn,ticket_price)
            with open('Tickets.txt','a') as file:
                file.write(f'Customer Name: {customer_name}\n')
                file.write(f'Movie Name: {movie_name}\n')
                file.write(f'Total Price: {total_price}INR\n')
            messagebox.showinfo('Success','Tickets are booked! you can download the ticket/s<3')
            create_ticket()


def create_ticket():
    name=name_entry.get()
    selected_it=tree.focus()
    rw=tree.item(selected_it)['values']
    movie=rw[1]
    booked_qn=int(variable1.get())
    tickets=booked_qn

    # Create a new window for the ticket
    ticket_window = tk.Tk()
    ticket_window.title("Movie Ticket")

    # Create a canvas to draw the ticket
    canvas = tk.Canvas(ticket_window, width=350, height=200)
    canvas.pack()

    # Draw the ticket outline with a different background color
    canvas.create_rectangle(50, 20, 500, 180, outline="#5D478B", fill="#8968CD", width=2)
    canvas.create_text(190, 60, text="Movie Ticket<3", font=("Courier New", 12, "bold"))
    # Draw lines to separate sections
    canvas.create_line(50, 80, 500, 80, fill="#5D478B", width=1)
    canvas.create_line(50, 110, 500, 110, fill="#5D478B", width=1)
    

    # Draw labels and user information
    canvas.create_text(100, 123, text='Movie:', font=("Courier New", 10))
    canvas.create_text(180, 123, text=f'{movie}', font=("Courier New", 10))
    canvas.create_text(100, 133, text="Date:", font=("Courier New", 10))
    canvas.create_text(180, 133, text="20/03/2024", font=("Courier New", 10))

    canvas.create_text(100, 143, text="Time:", font=("Courier New", 10))
    canvas.create_text(180, 143, text="15:00PM", font=("Courier New", 10))

    canvas.create_text(100, 153, text="Seat:", font=("Courier New", 10))
    canvas.create_text(180, 153, text="A12", font=("Courier New", 10))

    # Display user's name on the ticket
    canvas.create_text(100, 95, text='Name:', font=("Courier New", 10))
    canvas.create_text(180, 95, text=f'{name}', font=("Courier New", 10))
    
    # Run the main loop for the ticket window
    ticket_window.mainloop()
               
            
title1_label=customtkinter.CTkLabel(app,font=f1,text='Available Movies', text_color='#fff',bg_color='#18161D')
title1_label.place(x=200,y=20)

img1=PhotoImage(file="1.png")
img1_label=Label(app,image=img1,bg='#18161D')
img1_label.place(x=130,y=10)
img2=PhotoImage(file="2.png")
img2_label=Label(app,image=img2,bg='#18161D')
img2_label.place(x=610,y=3)

name_label=customtkinter.CTkLabel(app,font=f3,text='Customer Name:',text_color='#fff',bg_color='#18161D')
name_label.place(x=120,y=300)
name_entry=customtkinter.CTkEntry(app,font=f3,text_color='#000',fg_color='#fff',border_color='#AA04A7',border_width=2,width=160)
name_entry.place(x=290,y=300)
num_label=customtkinter.CTkLabel(app,font=f3,text='Number Of Tickets:',text_color='#fff',bg_color='#18161D')
num_label.place(x=122,y=350)

variable1=StringVar()
opt=['1','2','3']

durop=customtkinter.CTkComboBox(app,font=f3,text_color='#000',fg_color='#fff',dropdown_hover_color='#AA04A7',button_color='#AA04A7',width=160,variable=variable1,values=opt,state='readonly')
durop.set('1')
durop.place(x=290,y=350)

book=customtkinter.CTkButton(app,command=booktc,font=f3,text_color='#fff',text='Book Ticket/s',fg_color='#AA04A7',hover_color='#6D006B',bg_color='#18161D',cursor='hand2',corner_radius=15,width=200)
book.place(x=190,y=400)

style=ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=f2,foreground='#fff',background='#000',fieldbackground='#292933')
style.map('Treeview',background=[('selected','#AA04A7')])

tree=ttk.Treeview(app,height=5)

tree['columns']=('Ticket ID','Movie Name','Available Tickets','Ticket Price')
tree.column('#0',width=0,stretch=tk.NO)
tree.column('Ticket ID',anchor=tk.CENTER,width=120)
tree.column('Movie Name',anchor=tk.CENTER,width=200)
tree.column('Available Tickets',anchor=tk.CENTER,width=120)
tree.column('Ticket Price',anchor=tk.CENTER,width=120)

tree.heading('Ticket ID',text='Ticket ID')
tree.heading('Movie Name',text='Movie Name')
tree.heading('Available Tickets',text='Available Tickets')
tree.heading('Ticket Price',text='Ticket Price')
tree.place(x=160,y=250)

add_to_treeview()
app.mainloop()



