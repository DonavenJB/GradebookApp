# Variables for user selection
user_option = ''

student_names = []
student_ids = []
test_score1 = []
test_score2 = []
test_score3 = []

# Function to fill the lists
def fill_arrays():
  for idx in range(0, 4):
    student_names.append(input("Please enter a student's name :\n"))
    student_ids.append(int(input("Please enter the student's ID:\n")))
    test_score1.append(int(input("Please enter the first score:\n")))
    test_score2.append(int(input("Please enter the second score:\n")))
    test_score3.append(int(input("Please enter the third score:\n")))

# Function to calculate the average and letter grade
def calculate_grade():
  student_found = -1
  student_id = int(input("Please enter the ID of the student:\n"))
  for idx in range(0, 4):
    if student_id == student_ids[idx]:
      student_found = 1
      average_score = (test_score1[idx] + test_score2[idx] + test_score3[idx]) / 3
      print("The average is: " + str(average_score))
      if average_score >= 90:
        print("The grade is: A")
      elif average_score <= 89 and average_score >= 80:
        print("The grade is: B")
      elif average_score <= 79 and average_score >= 70:
        print("The grade is: C")
      elif average_score <= 69 and average_score >= 60:
        print("The grade is: D")
      else:
        print("The grade is: F")
  return student_found

# Function to update student information
def update_student_info():
  student_id = int(input("Please enter the ID of the student:\n"))
  student_found = -1
  for idx in range(0, 4):
    if student_id == student_ids[idx]:
      student_found = 1
      # Show the current information
      print("The student name is: " + student_names[idx] + "\nID is: " +
            str(student_ids[idx]) + "\nFirst score  is: " + str(test_score1[idx]) +
            "\nSecond score  is: " + str(test_score2[idx]) +
            "\nThird score  is: " + str(test_score3[idx]))
      test_score1[idx] = int(input("Please enter the first score:\n"))
      test_score2[idx] = int(input("Please enter the second score:\n"))
      test_score3[idx] = int(input("Please enter the third score:\n"))

  return student_found

# Function to display student information
def show_student_info():
  student_id = int(input("Please enter the ID of the student:\n"))
  student_found = -1
  for idx in range(0, 4):
    if student_id == student_ids[idx]:
      student_found = 1
      # Display the student details
      print("The student name is: " + student_names[idx] + "\nID is: " +
            str(student_ids[idx]) + "\nFirst score  is: " + str(test_score1[idx]) +
            "\nSecond score  is: " + str(test_score2[idx]) +
            "\nThird score  is: " + str(test_score3[idx]))

  return student_found

# Function to display the menu options
def menu_options(selected_option):
  while selected_option != "E":
    print("**** MENU OPTIONS ****")
    selected_option = input(
      "Type P to populate the student information.\n" +
      "Type U to update student Information\n" +
      "Type D to display the student information.\n" +
      "Type C to calculate the Grade.\n" + "Type E to exit\n" +
      "Please enter your choice:\n")
    if selected_option == "P":
      fill_arrays()
      selected_option = ''
    elif selected_option == "U":
      result_id = update_student_info()
      if result_id < 0:
        print("The ID is not found!")
    elif selected_option == "D":
      result_id = show_student_info()
      if result_id < 0:
        print("The ID is not found!")
    elif selected_option == "C":
      result_id = calculate_grade()
      if result_id < 0:
        print("The ID is not found!")
    elif selected_option == "E":
      print("Thank you for using the program.\n" + "Bye")
    else:
      print("Invalid choice. Please try again!")

# Start the program by calling the menu
menu_options(user_option)