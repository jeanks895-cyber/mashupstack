attendance = [18, 20, 19, 15, 21]

full_count = 0
total_attendance = 0

for students in attendance:
    if students >= 20:
        print("Full")
        full_count += 1
    else:
        print("Not Full")
    
    total_attendance += students

print("Number of full days:", full_count)
print("Total attendance for 5 days:", total_attendance)
