import base64
from PIL import Image
from io import BytesIO
import numpy as np
import pyodbc # type: ignore

# Establish a connection to your SQLite database using pyodbc
connection_string = 'Driver={SQL Server};Server=DESKTOP-ACEO563\SQLEXPRESS;Database=milahow_Space_Optimizer;Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)
# Create a cursor object
cursor = conn.cursor()

# Define your parameters
UserDetailID_fk = 1
Index = 1
ContainerID = 7
IDs = '32 '

# Call the stored procedure with parameters
cursor.execute(f"EXEC SP_User_Shape_Query @P_UserDetailID_fk=?, @P_Index=?, @P_ContainerID=?, @P_IDs=?", UserDetailID_fk, Index, ContainerID, IDs)

