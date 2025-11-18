import mysql.connector

# connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",      # your MySQL host
    user="root",           # your MySQL username
    password="12345",      # your password (MUST be in quotes)
    database="RMS"         # your database name
)


#-------------------------DATABASE-------------------------

#                    +---------------+
#                    | Tables_in_rms |
#                    +---------------+
#                    | user          |
#                    +---------------+
#                    | train         |
#                    +---------------+
#                    | passenger     |
#                    +---------------+
#                    | booking       |
#                    +---------------+



# create cursor
cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE RMS")
# print("✔ Database RMS created")



#-------------------------TABLES-------------------------



#Table creation of user --------->

#+----------+-------------+------+-----+---------+-------+
#| Field    | Type        | Null | Key | Default | Extra |
#+----------+-------------+------+-----+---------+-------+
#| userID   | int(11)     | NO   | PRI | NULL    |       |
#| password | varchar(40) | NO   |     | NULL    |       |
#+----------+-------------+------+-----+---------+-------+
"""
cursor.execute('''
CREATE TABLE user(
    userID INT PRIMARY KEY,
    password VARCHAR(40) NOT NULL
)
''')

print("✔ Table user created")
"""

#Table creation of Train --------->

#+----------------+-------------+------+-----+---------+-------+
#| Field          | Type        | Null | Key | Default | Extra |
#+----------------+-------------+------+-----+---------+-------+
#| TrainID        | int(11)     | NO   | PRI | NULL    |       |
#| Train_Name     | varchar(30) | NO   |     | NULL    |       |
#| Source_Station | varchar(30) | NO   |     | NULL    |       |
#| Destination    | varchar(30) | NO   |     | NULL    |       |
#| Day            | date        | NO   |     | NULL    |       |
#+----------------+-------------+------+-----+---------+-------+
"""
cursor.execute('''
CREATE TABLE Train(
    TrainID INT PRIMARY KEY,
    Train_Name VARCHAR(30) NOT NULL,
    Source_Station VARCHAR(30) NOT NULL,
    Destination VARCHAR(30) NOT NULL,
    Day DATE NOT NULL
)
''')

print("✔ Table Train created")
"""

#Table creation of Passenger --------->

#+----------------+-------------+------+-----+---------+-------+
#| Field          | Type        | Null | Key | Default | Extra |
#+----------------+-------------+------+-----+---------+-------+
#| PassengerID    | int(11)     | NO   | PRI | NULL    |       |
#| Passenger_Name | varchar(30) | NO   |     | NULL    |       |
#| Age            | int(11)     | YES  |     | NULL    |       |
#| Gender         | varchar(10) | YES  |     | NULL    |       |
#| Phone_Number   | bigint(20)  | YES  | UNI | NULL    |       |
#+----------------+-------------+------+-----+---------+-------+
"""
cursor.execute('''
CREATE TABLE Passenger(
    PassengerID INT PRIMARY KEY,
    Passenger_Name VARCHAR(30) NOT NULL,
    Age INT CHECK (Age>0),
    Gender VARCHAR(10),
    Phone_Number BIGINT UNIQUE
)
''')

print("✔ Table Passenger created")
"""

#Table creation of Booking --------->

#+----------------+---------+------+-----+---------+-------+
#| Field          | Type    | Null | Key | Default | Extra |
#+----------------+---------+------+-----+---------+-------+
#| PNR_No         | int(11) | NO   | PRI | NULL    |       |
#| TrainID        | int(11) | YES  | MUL | NULL    |       |
#| PassengerID    | int(11) | YES  | MUL | NULL    |       |
#| Booking_Date   | date    | NO   |     | NULL    |       |
#| Departure_Date | date    | NO   |     | NULL    |       |
#| Fare           | int(11) | YES  |     | NULL    |       |
#+----------------+---------+------+-----+---------+-------+
"""
cursor.execute('''
CREATE TABLE Booking(
    PNR_No INT PRIMARY KEY,
    TrainID INT,
    PassengerID INT,
    Booking_Date DATE NOT NULL,
    Departure_Date DATE NOT NULL,
    Fare INT CHECK (Fare >= 0),

    FOREIGN KEY (TrainID) REFERENCES Train(TrainID),
    FOREIGN KEY (PassengerID) REFERENCES Passenger(PassengerID)
)
''')

print("✔ Table Booking created")
"""

#Table creation of Cancellation --------->

#+-------------------+---------+------+-----+---------+-------+
#| Field             | Type    | Null | Key | Default | Extra |
#+-------------------+---------+------+-----+---------+-------+
#| PNR_No            | int(11) | YES  | MUL | NULL    |       |
#| Cancellation_Date | date    | NO   |     | NULL    |       |
#| Refund_Amount     | int(11) | YES  |     | NULL    |       |
#+-------------------+---------+------+-----+---------+-------+
"""
cursor.execute('''
CREATE TABLE Cancellation(
    PNR_No INT,
    Cancellation_Date DATE NOT NULL,
    Refund_Amount INT CHECK (Refund_Amount >= 0),

    FOREIGN KEY (PNR_No) REFERENCES Booking(PNR_No)
)
''')

print("✔ Table Cancellation created")
"""
