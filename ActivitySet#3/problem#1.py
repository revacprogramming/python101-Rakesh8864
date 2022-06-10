def main():
    iterations = int(input('Number of rectangles - '))
    data_raw = input_rects(iterations)
    data_result = find_areas(data_raw)
    for key, value in data_result.items():
        print (key, '=', value)

# takes tuple i.e, (x1, y1, x2, y2, x3, y3) and returns the area
def area(d):
    return abs((d[0] * (d[3]-d[5])) + (d[2] * (d[5]-d[1])) + (d[4] * (d[1]-d[3])))


def input_rect(**i):
    if i != {}:
      for key,value in i.items():
        if key == 'index':
          temp = input('Rectangle '+ str(value) +' cordinates - ')
    else:
        temp = input('Rectangle cordinates - ')
    temp = temp.split()
    for i in range(0, len(temp)):
        temp[i] = float(temp[i])
    temp = tuple(temp)
    return temp

# takes how many rectangles and returns dict i.e, { 'name' : (points_in_tuple) }
def input_rects(n):
    data_dict = dict()
    t = 'R'
    t_data = None
    for i in range(1,n+1):
        t = t + str(i)
        t_data = input_rect(index = i)
        data_dict.update({t : t_data})
        t = t[0]
    return data_dict

# takes dict i.e, { 'name' : (points_in_tuple) } and returns { 'name' : area }
def find_areas(d):
    for key,value in d.items():
        d[key] = area(value)
    return d
        
main()