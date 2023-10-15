users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visits_list = {"Общее количество": 0, "Уникальные посещения": 0}
unique_visits = set()
for visit in users:
    unique_visits.add(visit)
visits_list["Общее количество"] = len(users)
visits_list["Уникальные посещения"] = len(unique_visits)
print(visits_list)