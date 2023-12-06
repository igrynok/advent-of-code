input_file = "input"

data = open(input_file).readlines()

seeds = list(map(int, data[0].split(':')[1].strip().split()))

seed_to_soil = []
soil_to_fertil = []
fertil_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humidity = []
humidity_to_location = []


def parse(lines, out):
    for line in lines:
        dest, source, step = list(map(int, line.strip().split()))
        out.append([(source, source + step - 1), (dest, dest + step - 1)])


parse(data[3:39], seed_to_soil)
parse(data[41:65], soil_to_fertil)
parse(data[67:101], fertil_to_water)
parse(data[103:149], water_to_light)
parse(data[151:180], light_to_temp)
parse(data[182:212], temp_to_humidity)
parse(data[214:252], humidity_to_location)


def get_dist(source, mapping):
    dist = -1
    for elem in mapping:
        if elem[0][0] <= source <= elem[0][1]:
            dist = elem[1][0] + (source - elem[0][0])
            break
    if dist == -1:
        dist = source
    return dist


answer = []
for seed in seeds:
    soil = get_dist(seed, seed_to_soil)
    fertil = get_dist(soil, soil_to_fertil)
    water = get_dist(fertil, fertil_to_water)
    light = get_dist(water, water_to_light)
    temp = get_dist(light, light_to_temp)
    humidity = get_dist(temp, temp_to_humidity)
    location = get_dist(humidity, humidity_to_location)
    answer.append(location)

print(min(answer))



