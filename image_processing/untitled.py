import cv2

def fitting_rectangle(contour):
	rect = cv2.minAreaRect(contour)  # 꼭 맞는 사각형 그리기
	box = cv2.boxPoints(rect)  # box포인트로 변경
	return box


if __name__ == "__main__":
    print()
