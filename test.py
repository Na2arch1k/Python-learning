# students = {}

# for i in range(5):
#     name = input(f"Введіть ім'я учня №{i+1}: ")
#     score = int(input(f"Введіть бал учня {name}: "))
#     students[name] = score
#     min_score = min(students.values())
# print("Учні з найнижчим балом:")

# for name, score in students.items():
#     if score == min_score:
#         print(f"{name} - {score}")
        
# students = {}

# for i in range(5):
#     name = input(f"Введіть ім'я учня №{i+1}: ")
#     score = int(input(f"Введіть бал учня {name}: "))
#     students[name] = score
#     max_score = max(students.values())
# print("Учні з найвижчим балом:")

# for name, score in students.items():
#     if score == max_score:
#         print(f"{name} - {score}")



# students = {}

# for i in range(5):
#     name = input("Введіть ім'я учня: ")
#     score = int(input("Введіть оцінку учня: "))
#     students[name] = score

# print ("Якщо бал від 80 до 100 ви відмінник")
# for name, score in students.items():
#     if 80 <= score <= 100:
#         print(f"{name}: {score}")




# students = {}

# for i in range(5):
#     name = input("Введіть ім'я учня: ")
#     score = int(input("Введіть бал учня: "))
#     students[name] = score


# for name, score in students.items():
#     if score % 2 == 0:
#         print(f"{name}: {score}")


# students = {}

# for i in range(5):
#     name = input("Введіть ім'я учня: ")
#     score = int(input("Введіть бал учня: "))
#     students[name] = score

# medium_score = sum(students.values()) / len(students)

# print("Ваш бал вищий за середній:")
# for name, score in students.items():
#     if score > medium_score :
#         print(f"{name}: {score}")



# product = {"яблуко": 10, "груша": 15, "банан": 12}
# while True:
#     name = input("Введіть назву товару: ")
#     if name == "стоп":
#         break
#     if name in product:
#         cost = product[name]
#         if cost <= 12:
#             print("Товар доступний і не дорогий")
#         else:
#             print("Товар доступний, але дорогий")
#     else:
#         print("Товар не знайдено")

# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
# i = 0
# while i < len(num):
#     current = num[i]
#     i += 1 
#     if current % 3 == 0 and current % 5 == 0:
#         print (f"Число {current} ділиться на 3 і на 5")
#     elif current % 3 == 0:
#         print (f"Число {current} ділиться на 3")
#     elif current % 5 == 0:
#         print (f"Число {current} ділиться на 5")


# symvol = input("Введіть рядок: ")
# dic = {}
# for s in symvol:
#     if s in dic:
#         dic[s] += 1
#     else:
#         dic[s] = 1
# for key, value in dic.items():
#     if value == 1:
#         print (key)





# numbers = []
# for i in range(7):
#     num = int(input(f"Введіть число №{i+1}: "))
#     numbers.append(num)

# my_tuple = tuple(numbers)

# my_dict = {}
# for n in numbers:
#     my_dict[n] = n ** 2

# print(numbers[::-1])
# print(my_tuple[1], my_tuple[4])
# for key, value in my_dict.items():
#     if value > 25:
#         print(key)


# words = []
# for i in range(5):
#     word = input(f"Введіть слово №{i+1}: ")
#     words.append(word)

# my_tuple = tuple(words)

# my_dict = {}
# for n in words:
#     my_dict[n] = len(n)

# for key, value in my_dict.items():
#     if value > 5:
#         print(key)

# word_length = set()
# for length in my_dict.values():
#     word_length.add(length)
# print(word_length)


# logs = [
#     "2024-06-07 12:01:05, OK, sensor_1",
#     "2024-06-07 12:01:06, ERROR, sensor_2",
#     "2024-06-07 12:01:07, OK, sensor_3",
#     "2024-06-07 12:01:08, WARNING, sensor_1",
#     "2024-06-07 12:01:09, ERROR, sensor_3",
#     "2024-06-07 12:01:10, OK, sensor_2",
# ]

# sensors = {}
# for log in logs:
#     parts = log.split(', ')
#     status = parts[1]
#     sensor = parts[2]
#     if sensor in sensors:
#         sensors[sensor].append(status)
#     else:
#         sensors[sensor] = [status]

# for sensor, statuses in sensors.items():
#     error_count = statuses.count("ERROR")
#     print(f"{sensor}: {error_count} помилок")




# grades = [
#     ("Іван", 12), ("Марія", 8), 
#     ("Олена", 10), ("Іван", 9), 
#     ("Марія", 12), ("Олена", 7)
# ]

# marks_students = {}

# for name, marks in grades:
#     if name in marks_students:
#         marks_students[name].append(marks)
#     else:
#         marks_students[name] = [marks]

# for name, marks in marks_students.items():
#     average_score = sum(marks) //  len(marks)
#     print(name, average_score)


# string = input("Ведіть рядок: ")

# words = {}

# words_list = string.split()

# for word in words_list:
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1 


# for word, count in words.items():
#     if count == 1:
#         print(word)



# results = [
#     ("cat", "cat"), ("dog", "dog"), ("cat", "dog"),
#     ("dog", "dog"), ("cat", "cat"), ("dog", "cat"),
#     ("cat", "cat"), ("dog", "dog"), ("cat", "cat")
# ]

# test_model = {}


# for real,  predicted in results:
#     if real == predicted:
#         if real in test_model:
#             test_model[real] += 1
#         else:
#             test_model[real] = 1

# for real, count in test_model.items():
#     print(f"{real}: {count} правильних відповвідей")



# results = [
#     ("cat", "cat"), ("dog", "dog"), ("cat", "dog"),
#     ("dog", "dog"), ("cat", "cat"), ("dog", "cat"),
#     ("cat", "cat"), ("dog", "dog"), ("cat", "cat"),
#     ("mouse", "cat"), ("mouse", "mouse"), ("cat", "mouse"),
#     ("mouse", "dog"), ("dog", "mouse"), ("mouse", "mouse")
# ]

# test_model = {}
# real_count = {}
# pred_count = {}

# for real, predicted in results:
#     if real == predicted:
#         if real in test_model:
#             test_model[real] += 1
#         else:
#             test_model[real] = 1

# for real, count in test_model.items():
#     print(f"{count} {real}")

# for real, predicted in results:
#     if real in real_count:
#         real_count[real] += 1
#     else:
#         real_count[real] = 1

# for real, predicted in results:
#     if predicted in pred_count:
#         pred_count[predicted] += 1
#     else:
#         pred_count[predicted] = 1
    
# accuracy = pred_count[predicted] / len(real_count)
# print(accuracy)

# labels = set(real_count) | set(pred_count) | set(test_model)
# for label in labels:
#     correct = test_model.get(label, 0)
#     real = real_count.get(label, 0)
#     predicted = pred_count.get(label, 0)
#     if real > 0: 
#         accuracy = correct / real
#     else:
#         accuracy = 0
#     share = predicted / len(results)
#     print(f"{label}: accuracy={accuracy:.2f}, share={share:.2f}")

# 


# logs = [
#     "2025-06-08 10:01:05, OK, sensor_1",
#     "2025-06-08 10:01:06, ERROR, sensor_2",
#     "2025-06-08 10:01:07, OK, sensor_3",
#     "2025-06-08 10:01:08, WARNING, sensor_1",
#     "2025-06-08 10:01:09, ERROR, sensor_3",
#     "2025-06-08 10:01:10, OK, sensor_2",
#     "2025-06-08 10:01:11, ERROR, sensor_1",
#     "2025-06-08 10:01:12, OK, sensor_1",
# ]

# sensors = {}

# for log in logs:
#     parts = log.split(', ')
#     status = parts[1]
#     sensor = parts[2]
#     if sensor in sensors:
#         sensors[sensor].append(status)
#     else:
#         sensors[sensor] = [status]

# for sensor, statuses in sensors.items():
#     error_count = statuses.count("ERROR")
#     print(f"{sensor}: {error_count}")

# for sensor, statuses in sensors.items():
#     error_count = statuses.count("ERROR")
#     if error_count > 1:
#         print(f"{sensor} має більше одної помилки")


# max_error = 0
# max_sensor = None
# for sensor, statuses in sensors.items():
#     error_count = statuses.count("ERROR")
#     if error_count > max_error:
#         max_error = error_count
#         max_sensor = sensor
# print(f"Сенсор з найбільшою кількістю помилок {max_sensor}: {max_error}")
    


# purchases = [
#     ("apple", 2), ("banana", 3), ("apple", 1),
#     ("orange", 5), ("banana", 2), ("apple", 4)
# ]

# products = {}

# for name, count in purchases:
#     if name in products:
#         products[name] += count
#     else:
#         products[name] = count

# for name, total in products.items():
#     print(f"{name}: {total}")

# max_product = max(products, key=products.get)
# print(f"Найбільше купували {max_product} ({products[max_product]})")

# for name, total in products.items():
#     if total == 1:
#         print(f"Товар який купували 1 раз {name}")


    
# grades = [
#     ("Ivan", "math", 12), ("Maria", "math", 10), ("Ivan", "physics", 9),
#     ("Maria", "physics", 12), ("Ivan", "chemistry", 8), ("Maria", "chemistry", 11),
#     ("Oleh", "math", 7), ("Oleh", "physics", 8), ("Oleh", "chemistry", 10)
# ]

# students = {}
 
# for name, subjeckt, grade in grades:
#     if name in students:
#         students[name].append(grade)
#     else:
#         students[name] = [grade]


# max_averange = 0
# best_student = ""
# for name, grades_list in students.items():
#     averange = sum(grades_list) / len(grades_list)
#     print(f"{name}: {averange:.1f}")
#     if averange > max_averange:
#         max_averange = averange
#         best_student = name
# print(f"Судент з найвищим середнім балом: {best_student} - {max_averange}")

# subjects = {}

# for name, subject, grade in grades:
#     if subject not in subjects or grade > subjects[subject][1]:
#         subjects[subject] = (name, grade)

# for subject, (name, grade) in subjects.items():
#     print(f"Найвища оцінка з {subject}: {grade} в {name}")


# def greet(name, age):
#     print(f"Привіт, {name}! Тобі {age} років. ")

# greet("Олег", 20) 
# greet(age=25, name="Марія")

def power(x, n=2):
    print(f"{x ** n}")

power(5)
power(2, 3)
