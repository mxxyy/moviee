from tkinter import *
import tkinter as tk


def create_ticket():
    name=name_entry.get()
    movie=tree.focus()
    booked_qn=int(variable1.get())
    tickets=booked_qn

    # Create a new window for the ticket
    ticket_window = tkk.Tk()
    ticket_window.title("Movie Ticket")

    # Create a canvas to draw the ticket
    canvas = tkk.Canvas(ticket_window, width=350, height=200)
    canvas.pack()

    # Draw the ticket outline with a different background color
    canvas.create_rectangle(50, 20, 300, 180, outline="#5D478B", fill="#8968CD", width=2)
    canvas.create_text(175, 60, text="Movie Ticket<3", font=("Courier New", 12, "bold"))
    # Draw lines to separate sections
    canvas.create_line(50, 80, 300, 80, fill="#5D478B", width=1)
    canvas.create_line(50, 110, 300, 110, fill="#5D478B", width=1)
    

    # Draw labels and user information
    canvas.create_text(100, 120, text=f'Movie:{movie}', font=("Courier New", 10))
    canvas.create_text(100, 133, text="Date:", font=("Courier New", 10))
    canvas.create_text(180, 133, text="20/03/2024", font=("Courier New", 10))

    canvas.create_text(100, 143, text="Time:", font=("Courier New", 10))
    canvas.create_text(180, 143, text="15:00PM", font=("Courier New", 10))

    canvas.create_text(100, 153, text="Seat:", font=("Courier New", 10))
    canvas.create_text(180, 153, text="A12", font=("Courier New", 10))

    # Display user's name on the ticket
    canvas.create_text(100, 95, text=f'Name:{name}', font=("Courier New", 10))
    # Run the main loop for the ticket window
    ticket_window.mainloop()
                
create_ticket()
