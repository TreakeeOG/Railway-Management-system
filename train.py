import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection

import tkinter as tk
from tkinter import messagebox


def add_train():
    root = tk.Tk()
    root.withdraw()

    try:
        con = get_connection()
        print("Database connection established.")
        cur = con.cursor()

        print("ADD TRAIN DETAILS")

        try:
            trainID = int(input("Enter Train Number: "))
            train_name = input("Enter Train Name: ")
            source_station = input("Enter Source Station: ")
            destination = input("Enter Destination Station: ")

            cur.execute(
                "INSERT INTO Train VALUES (%s, %s, %s, %s)",
                (trainID, train_name, source_station, destination)
            )
            con.commit()

            print("Train Added Successfully")
            messagebox.showinfo("Success!", "Train Added Successfully")

        except Exception as e:
            print(f"Error adding train: {e}")
            messagebox.showerror("Error", f"Error adding train: {e}")

    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        messagebox.showerror("Database Error", f"Could not connect to the database: {e}")

    finally:
        input("Press Enter to continue...")
        try:
            con.close()
            print("Database connection closed.")
        except:
            pass

def view_trains():
    root = tk.Tk()
    root.withdraw()

    try:
        con = get_connection()
        print("Database connection established.")
        cur = con.cursor()

        print("AVAILABLE TRAINS")

        cur.execute("SELECT * FROM Train")
        records = cur.fetchall()

        if not records:
            print("No train records found.")
            messagebox.showinfo("Info", "No Train Records found")
        else:
            print("\nTrain No | Train Name | Source | Destination")
            print("-" * 50)
            for row in records:
                print(f"{row[0]:8} | {row[1]:10} | {row[2]:6} | {row[3]}")

    except Exception as e:
        print(f"Error fetching train records: {e}")
        messagebox.showerror("Error", f"Error fetching train records: {e}")

    finally:
        input("\nPress Enter to continue...")
        try:
            con.close()
            print("Database connection closed.")
        except:
            pass

def update_train():
    root = tk.Tk()
    root.withdraw()

    try:
        con = get_connection()
        print("Database connection established.")
        cur = con.cursor()

        print("UPDATE TRAIN DETAILS")

        try:
            trainID = int(input("Enter Train Number to Update: "))

            # Check if train exists
            cur.execute(
                "SELECT * FROM Train WHERE trainID = %s",
                (trainID,)
            )
            record = cur.fetchone()

            if not record:
                print("Train Not Found")
                messagebox.showwarning("Invalid Input", "Train Not found")
                input("Press Enter to continue...")
                return

            # New details
            train_name = input("Enter New Train Name: ")
            source_station = input("Enter New Source Station: ")
            destination = input("Enter New Destination Station: ")

            cur.execute(
                """
                UPDATE Train
                SET train_name = %s, source_station = %s, destination = %s
                WHERE trainID = %s
                """,
                (train_name, source_station, destination, trainID)
            )

            con.commit()
            print("Train Updated Successfully")
            messagebox.showinfo("Success", "Train Updated successfully")

        except ValueError:
            print("Invalid Train Number")
            messagebox.showwarning("Error", "Invalid train number")

        except Exception as e:
            print(f"Error updating train: {e}")
            messagebox.showerror("Error", f"Error updating train: {e}")

    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        messagebox.showerror("Database Error", f"Could not connect to the database: {e}")

    finally:
        input("Press Enter to continue...")
        try:
            con.close()
            print("Database connection closed.")
        except:
            pass

def delete_train():
    con = get_connection()
    cur = con.cursor()

    print("DELETE TRAIN")

    try:
        trainID = int(input("Enter Train Number to Delete: "))

        # Check if train exists
        cur.execute(
            "SELECT * FROM Train WHERE trainID = %s",
            (trainID,)
        )

        if not cur.fetchone():
            print("Train Not Found")
            messagebox.showwarning("Error","Train Not Found")
            input("Press Enter to continue...")
            return

        # Delete train
        cur.execute(
            "DELETE FROM Train WHERE trainID = %s",
            (trainID,)
        )
        con.commit()

        print("Train Deleted Successfully")
        messagebox.showinfo("Sucess","Train Deleted Successfully")

    except ValueError:
        print("Invalid Train Number")
        messagebox.showwarning("Error","Invalid trian Number")
    finally:
        input("Press Enter to continue...")
        con.close()

