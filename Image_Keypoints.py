## SOURCE REFERENCE FOR THIS MODULE:
# https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/


# importing the module
import cv2

kp = ["Nose","Neck","RShoulder","RElbow","RWrist","LShoulder","LElbow","LWrist","MidHip","RHip","RKnee","RAnkle","LHip","LKnee","LAnkle","REye","LEye","REar","LEar","LBigToe","LSmallToe","LHeel","RBigToe","RSmallToe","RHeel"]
kpi = 0
x_kp = []
y_kp = []
# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
	global kpi
	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)
		kpi += 1
		if (kpi < 25): 
			print(kp[kpi])
			x_kp.append(x)
			y_kp.append(y)
		
		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		# cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
		# img = cv2.circle(img, (x,y), radius=0, color=(0, 0, 255), thickness=-1)


		cv2.imshow('image', cv2.circle(img, (x,y), radius=5, color=(0, 0, 255), thickness=-1))

	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv2.imshow('image', img)

# driver function
if __name__=="__main__":
	# reading the image
	img = cv2.imread('media/comparePose1.jpg', 1)

	# displaying the image
	cv2.imshow('image', img)
	# setting mouse handler for the image
	# and calling the click_event() function

	print(kp[kpi])
	cv2.setMouseCallback('image', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	print(x_kp)
	print(y_kp)
	# close the window
	cv2.destroyAllWindows()
