import tkinter as tk
from tkinter import messagebox, scrolledtext

# Colors and styles (Star Wars / Coruscant Guard inspired)
BACKGROUND_COLOR = "#1e1e2e"
FOREGROUND_COLOR = "#f8f8f2"
HIGHLIGHT_COLOR = "#e63946"
BUTTON_COLOR = "#ff4d4d"
FONT = ("Consolas", 12)

# Initialize app
root = tk.Tk()
root.title("Coruscant Guard – Suspect Warning Database")
root.geometry("600x500")
root.configure(bg=BACKGROUND_COLOR)

# Labels
title_label = tk.Label(root, text="🚨 Coruscant Guard Warning System 🚨", 
                       font=("Consolas", 16, "bold"), bg=BACKGROUND_COLOR, fg=HIGHLIGHT_COLOR)
title_label.pack(pady=10)

# Username input
username_label = tk.Label(root, text="Suspect Username:", font=FONT, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
username_label.pack()
username_entry = tk.Entry(root, font=FONT, width=40)
username_entry.pack(pady=5)

# Warning input
warning_label = tk.Label(root, text="Infraction Description:", font=FONT, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
warning_label.pack()
warning_entry = tk.Entry(root, font=FONT, width=40)
warning_entry.pack(pady=5)

# Display box
log_label = tk.Label(root, text="📄 Warning Logs:", font=FONT, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
log_label.pack(pady=(20, 0))
log_display = scrolledtext.ScrolledText(root, font=FONT, width=60, height=10, bg="#2e2e3e", fg=FOREGROUND_COLOR, insertbackground=FOREGROUND_COLOR)
log_display.pack(pady=5)

# Data structure to store warnings for each user
warnings_db = {}

# Add warning to log and track infractions
def add_warning():
    username = username_entry.get().strip()
    warning = warning_entry.get().strip()
    
    if username and warning:
        if username not in warnings_db:
            warnings_db[username] = {}

        if warning in warnings_db[username]:
            warnings_db[username][warning] += 1  # Increment the count for the same warning
        else:
            warnings_db[username][warning] = 1  # Add new warning with count 1

        # Update the warning log display
        update_log_display()

        # Clear the input fields
        username_entry.delete(0, tk.END)
        warning_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Info", "Please enter both a username and a warning.")

# Update the log display with current warnings from the warnings_db
def update_log_display():
    log_display.delete(1.0, tk.END)  # Clear the log display
    for username, infractions in warnings_db.items():
        for warning, count in infractions.items():
            log_display.insert(tk.END, f"👤 {username} – ⚠️ {warning} x{count}\n")

# Clear warnings for a specific user
def clear_user_warnings():
    username = username_entry.get().strip()
    if username:
        if username in warnings_db:
            del warnings_db[username]  # Delete the user's warnings
            update_log_display()
            messagebox.showinfo("Clear Warnings", f"All warnings for {username} have been cleared.")
        else:
            messagebox.showwarning("User Not Found", f"No warnings found for {username}.")
    else:
        messagebox.showwarning("Missing Username", "Please enter a username to clear warnings.")

# Clear all warnings
def clear_all_warnings():
    result = messagebox.askyesno("Clear All?", "Are you sure you want to clear all warnings?")
    if result:
        warnings_db.clear()  # Clear all warnings
        update_log_display()

# Buttons
button_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Warning", font=FONT, bg=BUTTON_COLOR, fg="white", command=add_warning)
add_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="Clear All Warnings", font=FONT, bg=HIGHLIGHT_COLOR, fg="white", command=clear_all_warnings)
clear_btn.grid(row=0, column=1, padx=10)

clear_user_btn = tk.Button(button_frame, text="Clear User Warnings", font=FONT, bg="#ff9900", fg="white", command=clear_user_warnings)
clear_user_btn.grid(row=1, column=0, padx=10, pady=5)

# Run the app
root.mainloop()
