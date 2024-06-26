                                                                Student Management System


The Student Management System is a graphical application that allows users to manage student information. The application uses a MySQL database to store student records and offers various functionalities such as adding, updating, searching, deleting, and exporting student records as an Excel sheet. 


**Requirements**

-Python 3.x
-PIL (Python Imaging Library)
-Tkinter (should be included in the standard Python library)


**Files**

-login.py: The main Python script containing the code for the login application.
-next_page.py: The Python script contains the code for all the features of the application.
-1695702.jpg: The background image file.
-student.png: The logo image file.
-password.png: The lock logo on login frame.
-username.png: The logo of username on login frame.


**Setup and Execution**

-Download the code and images:
-Download the provided Python script (login.py and next_page.py) and image files (1695702.jpg ,student.png ,password.png ,username.png) into a
 directory of your choice.

-Set up the Python environment:
	-Make sure you have Python 3.x installed on your machine.
	-Install the necessary libraries using the following commands shell:
		pip install pillow


**Run the application**

1. Open PyCharm.
2. Create a new Python project and add the downloaded Python script (`login.py`) to the project.
3. Ensure the image files (`1695702.jpg` and `student.png`) are in the same directory as the Python script.
4. Run the script (`login.py`) using the PyCharm IDE by right-clicking the file in the project explorer and selecting "Run 'login.py'".
5. Alternatively, you can execute the script from a terminal by navigating to the directory containing the script and running the following 
   command: shell
      python login.py



**Using the application**

1. Once the script runs, the login window will appear.
2. Enter the username "Rajat Gupta" (or the built-in username and password) and the password "12345" to log in.
3. If the login is successful, a "success" message will be displayed, and the application will proceed to the next page. Otherwise, you will see an error message box showing "Fields cannot be empty" or "Invalid Credentials" as appropriate.

4. Modify the application as needed to customize it according to your requirements. 
5. Replace the hardcoded username and password with a more secure authentication method, such as database validation, for production use.
6. Ensure that the image file paths are correctly set in the script.

  Login:Rajat Gupta
  Password:12345

-To connect database 
  use your sql password
  HOST NAME:localhost
  USER:your user name in sql{in my case: root)
  Password: Your MySQL Password {in my case :rajat}



**Features**

-Login Page: The login page requires you to fill in both fields; if either is left empty, an error message stating "Fields cannot be empty" will   
 be displayed. If incorrect information is entered, an "Invalid Details" error message will appear. Additionally, when you hover the cursor over 
 the login page, it changes into a hand symbol.

 1. Add Student: Allows users to add new student records to the database.
 2. Search Student: Enables searching for specific student records using various criteria (e.g., Roll No., Name).
 3. Delete Student: Deletes an existing student record from the database.
 4. Update Student: Updates the details of an existing student record.
 5. Show Student: Displays all student records in a table format.
 6. Export Data: Exports student records to a CSV file.


**Usage**
-Connect to Database:
	-Click the "Connect To Database" button.
	-Enter the MySQL host, username, and password details in the pop-up window.
	-Upon successful connection, the database and table will be set up, and you can use the application.


-Add Student:
	-Click the "Add Student" button to open the add student form.
	-Fill in the student details and click "ADD STUDENT" to add the record to the database.



-Search Student:
	-Click the "Search Student" button to open the search student form.
	-Enter the search criteria and click "SEARCH STUDENT" to search the database.



-Delete Student:
	-Select a student record from the table.
	-Click the "Delete Student" button to delete the selected record.



-Update Student:
	-Select a student record from the table.
	-Click the "Update Student" button to open the update student form.
	-Modify the student's information and click "UPDATE STUDENT" to save the changes.


-Show Student:
	-Click the "Show Student" button to display all student records in the table.


-Export Data:
	-Click the "Export Student" button to save student records to a CSV file.(You can save this csv file to the desired location)


-Exit:
	-Click the "Exit" button to close the application.(A popup will be show click "Ok" to exit the application)





**Summary**
 This application provides a user-friendly graphical interface to manage student records efficiently. You can add, search, update, and delete  
 student records from the database and export them as needed. The program is designed to be simple and easy to use for anyone managing student 
 data.




