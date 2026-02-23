import json
students={
    "Pooja":{"marks":90,"status":"PASS"},
    "Rama":{"marks":45,"status":"FAIL"}
}
#writing the file
with open("students.json","w") as file:
    json.dump(students,file)
print("Data written sucessfully!")
#reading the file
with open("students.json","r") as file:
  data=json.load(file)
  print("Data read from file:")
  print(data)