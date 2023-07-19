# Day 8: Functions with inputs

def paint_calc(height,width,cover):
    num_of_cans = (height*width)/(cover)
    print(round(num_of_cans))


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

