def find_common_participants(first_str, second_str, delimiter=','):
    first_group = first_str.split(delimiter)
    second_group = second_str.split(delimiter)
    common_participants = set(first_group).intersection(set(second_group))
    return sorted(list(common_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, '|'))
