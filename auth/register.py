# auth/register.py

import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection

import tkinter as tk
from tkinter import messagebox

def register_user(user_id, password):

    root = tk.Tk()
    root.withdraw()

    try:
        con = get_connection()
        print("Database connection established.")
        cur = con.cursor()

        # Check if user already exists
        cur.execute("SELECT * FROM User WHERE userID = %s", (user_id,))
        if cur.fetchone():
            print("User ID already exists!")
            messagebox.showwarning("Error", "User ID already exists!")
        else:
            # Insert new user
            cur.execute(
                "INSERT INTO User (userID, password) VALUES (%s, %s)",
                (user_id, password)
            )
            con.commit()
            print("Registration Successful!")
            messagebox.showinfo("Success", "Registration Successful!")

    except ValueError:
        print("Invalid input! User ID must be a number.")
        messagebox.showwarning("Invalid Input", "User ID must be a number.")

    except Exception as e:
        print(f"An error occurred during registration: {e}")
        messagebox.showwarning("Error", "An unexpected error occurred.")

    finally:
        try:
            con.close()
            print("Database connection closed.")
        except:
            pass

