def cal_distance(x1, x2, y1, y2):
	return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

def cal_width_height(contour):
	x_min = min([i[0][0] for i in contour])
	x_max = max([i[0][0] for i in contour])
	y_min = min([i[0][1] for i in contour])
	y_max = max([i[0][1] for i in contour])
	width = x_max - x_min
	height = y_max - y_min
	center_x = float((x_max + x_min) / 2)
	center_y = float((y_max + y_min) / 2)
	return width, height, center_x, center_y

if __name__ == "__main__":
    print()
