import random


def k_means(objects, clusters):
    get_distance = lambda obj, centroid: abs(centroid[0] - obj[0]) + abs(
        centroid[1] - obj[1])  # cпрощена формула для визначення дистанції

    all_objects = [obj for obj in objects]
    centroids = [random.choice(all_objects) for _ in range(clusters)]  # обираємо випадкові точки як центроїди

    while True:
        centroids_and_objs = {index: [] for index, _ in enumerate(centroids)}  # створення словника центроїдів і об'єктів

        for obj in all_objects:
            distances_list = [get_distance(obj, centroid) for centroid in centroids]  # список з дистанціями від об'єкту до центроїдів

            min_centroid = distances_list.index(min(distances_list))  # знаходження мінімальної дістанції

            centroids_and_objs[min_centroid].append(obj)  # додаємо об'єкт до центроїда з мінімальною дистанцією

        centroid_states = []
        for centroid, objects in centroids_and_objs.items():
            # якщо довжина списку об'єктів центроїду нульова, тоді замість нього обираємо іншу рандомну точку
            if len(objects) == 0:
                centroids[centroid] = random.choice(all_objects)
                break

            sum_x, sum_y = 0, 0
            for obj in objects:
                sum_x += obj[0]
                sum_y += obj[1]

            new_centroid = [round(sum_x / len(objects), 2), round(sum_y / len(objects), 2)]  # розрахування нового центроїду для об'єктів

            # якщо новий центроїд не дорівнює попередньому перезаписуємо попередній
            if centroids[centroid] != new_centroid:
                centroids[centroid] = new_centroid
                centroids_and_objs[centroid].clear()
                centroid_states.append(True)
            else:
                centroid_states.append(False)  # додовання до списку станів центроїдів, що не потрібно його розраховувати

        # якщо ніякий з центроїдів не потрібно розраховувати завершуємо алгоритм
        if not any(centroid_states):
            return centroids, centroids_and_objs


# функція для обробки результатів
def print_result(centroids, centroids_and_objs):
    for centroid in centroids_and_objs.keys():
        print(f'centroid testint {centroids[centroid]}:', centroids_and_objs[centroid])


result = k_means([[1, 1], [0, 0], [2, 0], [4, 4], [5, 5], [5, 3]], 2)
print_result(result[0], result[1])
