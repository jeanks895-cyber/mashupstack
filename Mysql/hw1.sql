INSERT INTO student (id, name, age, department, grade) VALUES
(1, 'Jean', 22, 'Computer Science', 85),
(2, 'Pranav', 21, 'Physics', 90),
(3, 'Amal', 22, 'Mechanical', 78),
(4, 'Aishwarya', 20, 'Computer Science', 92);

SELECT * FROM student WHERE age > 20;

SELECT * FROM student WHERE department IN ('Computer Science', 'Physics');

SELECT * FROM student WHERE grade = 90;

SELECT * FROM student WHERE grade BETWEEN 70 AND 90;
