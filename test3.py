import math
from itertools import permutations

#locations
locations = [
    ("branch 1", "Uttara Branch", 23.8728568, 90.3984184),
    ("branch 2", "City Bank Airport Branch", 23.8513998, 90.3944536),
    ("branch 3", "City Bank Nikunjo", 23.8330429, 90.4092871),
    ("branch 4", "City Bank Beside Uttara Diagnostic", 23.8679743, 90.3840879),
    ("branch 5", "City Bank Mirpur 12", 23.8248293, 90.3551134),
    ("branch 6", "City Bank Le Meridien", 23.827149, 90.4106238),
    ("branch 7", "City Bank Shaheed Sarani", 23.8629078, 90.3816318),
    ("branch 8", "City Bank Narayanganj", 23.8673789, 90.429412),
    ("branch 9", "City Bank Paliabl", 23.8248938, 90.3549467),
    ("branch 10", "City Bank JFP", 23.813316, 90.4147498),
]

def calculate_distance(coord1, coord2):
    R = 6371  # Radius of the Earth in kilometers
    branch_no, Name, lat1, lon1 = coord1
    branch_no, Name, lat2, lon2 = coord2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

#distances between all pairs of locations
distances = {}
for i in range(len(locations)):
    for j in range(len(locations)):
        distances[(i, j)] = calculate_distance(locations[i], locations[j])

#brute force
best_route = None
min_distance = float("inf")

#starting from uttara branch
start_index = 0

for i in range(len(locations)):
    if locations[i][0] == "branch 1":
        start_index = i
        break

for route in permutations(range(len(locations)), len(locations)):
    if route[0] == start_index:
        distance = sum(distances[(route[i], route[i+1])] for i in range(len(route) - 1))
        if distance < min_distance:
            min_distance = distance
            best_route = route

# Print the best route
print("Best Optimized Traffic Route:")
destination=1
for index in best_route:
    print(f"destination {destination}: {locations[index][0:2]}")
    destination+=1



print(f"Total distance: {min_distance} kilometers")
