import tkinter as tk
from tkinter import messagebox

appointments = []

def is_valid_name(name):
    return name.strip() != "" and all(c.isalpha() or c.isspace() for c in name)

def is_filled(field):
    return field.strip() != ""

def show_welcome_screen():
    root = tk.Tk()
    root.title("Hospital Booking System")
    root.geometry("400x250")

    tk.Label(root, text = "🏥 Welcome to Hospital Appointment Booking",
             font =("Times New Roman", 14), wraplength = 350, justify = "center").pack(pady = 40)

    tk.Button(root, text = "Start", width = 20, command = lambda: open_main_menu(root)).pack(pady = 10)
    root.mainloop()

def open_main_menu(current_window):
    current_window.destroy()
    win = tk.Tk()
    win.title("Main Menu")
    win.geometry("350x300")

    tk.Label(win, text="Main Menu", font=("Times New Roman", 16)).pack(pady=20)

    tk.Button(win, text = "Book Appointment", width = 25, command = lambda: open_booking_screen(win)).pack(pady = 10)
    tk.Button(win, text = "View Appointments", width = 25, command = lambda: open_view_screen(win)).pack(pady = 10)
    tk.Button(win, text = "Cancel Appointment", width = 25, command = lambda: open_cancel_screen(win)).pack(pady = 10)
    tk.Button(win, text = "Exit", width = 25, command = win.quit).pack(pady = 20)

def open_booking_screen(current_window):
    current_window.destroy()
    win = tk.Tk()
    win.title("Book an Appointment")
    win.geometry("400x400")

    tk.Label(win, text = "Book a New Appointment", font =("Times New Roman", 14)).pack(pady=10)

    tk.Label(win, text = "Patient Name:").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Doctor Name:").pack()
    doctor_entry = tk.Entry(win)
    doctor_entry.pack()

    tk.Label(win, text="Preferred Time (e.g., 10:30 AM):").pack()
    time_entry = tk.Entry(win)
    time_entry.pack()

    # --- PLACEHOLDER: Calendar widget and time dropdown would go here ---
    # Future: Use a calendar widget like tkcalendar.DateEntry
    # Future: Time slot dropdown (e.g., Combobox) instead of free text

    def book_now():
        name = name_entry.get()
        doctor = doctor_entry.get()
        time = time_entry.get()

        if not is_valid_name(name):
            messagebox.showerror("Input Error", "Please enter a valid name (letters only).")
            return
        if not is_filled(doctor):
            messagebox.showerror("Input Error", "Doctor's name is required.")
            return
        if not is_filled(time):
            messagebox.showerror("Input Error", "Time is required.")
            return

        appointments.append((name, doctor, time))
        messagebox.showinfo("Success", f"Appointment booked!\n{name} with {doctor} at {time}.")
        open_main_menu(win)

    tk.Button(win, text = "Submit", command=book_now).pack(pady=10)
    tk.Button(win, text = "Back", command=lambda: open_main_menu(win)).pack()

def open_view_screen(current_window):
    current_window.destroy()
    win = tk.Tk()
    win.title("View Appointments")
    win.geometry("400x400")

    tk.Label(win, text = "Scheduled Appointments", font = ("Times New Roman", 14)).pack(pady = 10)

    if not appointments:
        tk.Label(win, text="(Nothing here yet)").pack()
    else:
        for idx, (name, doctor, time) in enumerate(appointments):
            tk.Label(win, text = f"{idx + 1}. {name} with {doctor} at {time}").pack(anchor = "w")

    tk.Button(win, text = "Back", command=lambda: open_main_menu(win)).pack(pady=20)

def open_cancel_screen(current_window):
    current_window.destroy()
    win = tk.Tk()
    win.title("Cancel Appointment")
    win.geometry("400x400")

    tk.Label(win, text = "Cancel Appointment", font = ("Times New Roman", 14)).pack(pady = 10)

    if not appointments:
        tk.Label(win, text = "No appointments to cancel.").pack()
        tk.Button(win, text = "Back", command = lambda: open_main_menu(win)).pack(pady = 20)
        return

    choice = tk.IntVar()
    for idx, (name, doctor, time) in enumerate(appointments):
        text = f"{idx + 1}. {name} with {doctor} at {time}"
        tk.Radiobutton(win, text = text, variable = choice, value = idx).pack(anchor = "w")

    def cancel_selected():
        selected = choice.get()
        if 0 <= selected < len(appointments):
            removed = appointments.pop(selected)
            messagebox.showinfo("Cancelled", f"Removed appointment for {removed[0]} at {removed[2]}.")
            open_main_menu(win)
        else:
            messagebox.showerror("Error", "Select one to cancel.")

    tk.Button(win, text="Cancel Selected", command = cancel_selected).pack(pady=10)
    tk.Button(win, text="Back", command = lambda: open_main_menu(win)).pack()

if __name__ == "__main__":
    show_welcome_screen()
