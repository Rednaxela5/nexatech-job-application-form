from pathlib import Path
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import tkinter as tk
from tkinter import ttk
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from mysql.connector import Error

def hard_1_main():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame13"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back_clicked():
        window.destroy()
        from _5_0_hard_window import hard_main
        hard_main()
    
    def hard_2_clicked():
        window.destroy()
        from _5_2_hardprob import hard_2_main
        hard_2_main()

    def display_hard_1_clicked():
        # Display the mysql codes in the box
        canvas.create_text(
            5.0,
            348.0,
            anchor="w",
            text="""            SELECT A.applicantNo, A.name, S.schoolName, 
            TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) AS 'Years Worked'
            FROM applicant_details AS A
            JOIN school AS S ON A.applicantNo = S.applicantNo
            JOIN work_experience AS E ON S.applicantNo = E.applicantNo
            WHERE S.schoolName = 'Polytechnic University of the Philippines'
            AND TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) >= 3;""",
            fill="#0F2634",
            font=("Montserrat", 24 * -1)
        )
        try:
            connection = mysql.connector.connect(host=MYSQL_HOST,
                                                    user=MYSQL_USER,
                                                    password=MYSQL_PASSWORD,
                                                    database=MYSQL_DATABASE)
            cursor = connection.cursor()
            # Execute the MySQL query
            query = "SELECT A.applicantNo, A.name, S.schoolName, TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) AS 'Years Worked' FROM applicant_details AS A JOIN school AS S ON A.applicantNo = S.applicantNo JOIN work_experience AS E ON S.applicantNo = E.applicantNo WHERE S.schoolName = 'Polytechnic University of the Philippines'AND TIMESTAMPDIFF(YEAR, E.workStarted, E.workEnded) >= 3;"
            cursor.execute(query)

            # Fetch all the rows from the result
            rows = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Display the results in a separate toplevel window
            result_window = Toplevel(window)
            result_window.title("Query Results")

            #Change the style of font in the treeview
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Gotham", 11, "bold"))
            style.configure("Treeview", font=("Gotham", 9))

            # Create a Treeview widget to display the data in tabular format
            tree = ttk.Treeview(result_window, columns=("applicantNo", "name", "schoolName", "Years Worked"), show="headings")
            tree.heading("applicantNo", text="applicantNo", anchor="w")
            tree.heading("name", text="name", anchor="w")
            tree.heading("schoolName", text="schoolName", anchor="w")
            tree.heading("Years Worked", text="Years Worked", anchor="w")

            # Insert the data into the treeview
            for row in rows:
                tree.insert("", "end", values=row)
            tree.pack()
        except Error as e:
            print(f"Error connecting to the database: {e}")


    window = Tk()

    window.geometry("1024x568")
    window.configure(bg = "#CCD4D9")
    window.title("Nexatech System Administration")

    canvas = Canvas(
        window,
        bg = "#CCD4D9",
        height = 568,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        512.0,
        22.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=display_hard_1_clicked,
        relief="flat"
    )
    button_1.place(
        x=436.0,
        y=519.0,
        width=134.0,
        height=36.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        512.0,
        85.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        511.0,
        153.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        511.0,
        348.0,
        image=image_image_4
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=back_clicked,
        relief="flat"
    )
    button_2.place(
        x=14.0,
        y=64.0,
        width=113.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=hard_2_clicked,
        relief="flat"
    )
    button_3.place(
        x=879.0,
        y=65.0,
        width=129.0,
        height=42.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    hard_1_main()