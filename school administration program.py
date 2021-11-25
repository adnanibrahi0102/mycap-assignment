#student Information Program
import csv
def write_csv(info_list):
  with open("student_info.csv",'a',newline='')as csv_file:
    writer =csv.writer(csv_file)
    writer.writerow(["Name","Age","Contact Number","Email-id"])
    writer.writerow(info_list)
#main function
if __name__ == '__main__':
  condition=True
  while(condition):
   student_info=input("enter student information in the following format (Name Age Contact_number Email id :\n")
   print("entered information",student_info)
   student_info_list=student_info.split(' ')
   print(student_info_list)
   write_csv(student_info_list)
#condition check for loop
   condition_check=input("enter (yes/no) if you want to enter information for another student \n")
   if condition_check=="yes" :
    condition= True
   elif condition_check=="no":
    condition=False