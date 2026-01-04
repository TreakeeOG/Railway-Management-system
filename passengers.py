import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection

import tkinter as tk
from tkinter import messagebox


def add_passenger():
    root = tk.Tk()
    root.withdraw()

    con = get_connection()
    cur = con.cursor()

    print("ADD PASSENGER")

    try:
        pid = int(input("Enter Passenger ID: "))
        name = input("Enter Passenger Name: ")
        age = input("Enter Age (leave blank if not available): ")
        gender = input("Enter Gender (leave blank if not available): ")
        phone = input("Enter Phone Number (leave blank if not available): ")

        # Convert optional fields
        age = int(age) if age else None
        phone = int(phone) if phone else None

        cur.execute(
            """
            INSERT INTO Passenger
            (PassengerID, Passenger_Name, Age, Gender, Phone_Number)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (pid, name, age, gender, phone)
        )

        con.commit()
        print("Passenger Added Successfully")
        messagebox.showinfo("Sucess","Passenger Added Successfully")
    except Exception:
        print("Error adding passenger")
        messagebox.showwarning("Error","Error adding passenger")
    finally:
        input("Press Enter to continue...")
        con.close()

def view_passengers():
    root = tk.Tk()
    root.withdraw()

    con = get_connection()
    cur = con.cursor()

    print("PASSENGER LIST")

    cur.execute("SELECT * FROM Passenger")
    records = cur.fetchall()

    if not records:
        print("No passenger records found.")
        messagebox.showwarning("Error","No passenger records found")
    else:
        print("\nID | Name | Age | Gender | Phone")
        print("-" * 55)
        for row in records:
            print(f"{row[0]:2} | {row[1]:15} | {row[2]} | {row[3]} | {row[4]}")

    input("\nPress Enter to continue...")
    con.close()

