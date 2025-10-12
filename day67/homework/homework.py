#1
students = {
    "Giorgi": 85,
    "Nino": 92,
    "Luka": 78,
    "Mariam": 96
}
top_student = max(students, key=students.get)
print(f"Top student is {top_student} with {students[top_student]} points.")

#2
hotel = {
    101: ["Giorgi", "Nino"],
    102: [],
    103: ["Luka"],
    104: []
}
print("People who bought a room:")
for room, guests in hotel.items():
    if guests:
        print(f"Room {room}: {', '.join(guests)}")

#3
person = {
    "name": "Giorgi",
    "age": 20
}
print("Before:", person)
person["age"] = 25
print("After:", person)