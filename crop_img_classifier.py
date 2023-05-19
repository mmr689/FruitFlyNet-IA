import cv2

import os
from datetime import datetime as dt


def draw_rectangle(event,x,y,flags,param):
    """
    Function to:
      · draw a 15x15 "rectangle" when the left mouse button is clicked
      · and crop the image.
    """
    size = 16
    if event == cv2.EVENT_LBUTTONDOWN:
        crop_img = img_clean[y-size:y+size, x-size:x+size]
        if crop_img.shape[0] >= size*2 and crop_img.shape[1] >= size*2:
            now = dt.now().strftime("%y%m%d%H%M%S")
            cv2.imwrite(f'dataset/original/{label}/{now}.png', crop_img)
            cv2.rectangle(img,(x-size,y-size),(x+size,y+size),colors[col_index],1)
        else:
             print('NO')
      



def main():
    global img, img_clean, label
    img_path = r'C:\Users\migue\OneDrive - Universitat de les Illes Balears\Proyectos\ZAP\FruitFlyNet\Files\images\N10_20150828-20151015\pic_Node_10_2015-09-10.jpg'

    #file_path = r'C:\Users\migue\OneDrive - Universitat de les Illes Balears\Proyectos\ZAP\FruitFlyNet\scripts\imgs'
    #imgs_name_list = [filename for filename in os.listdir(file_path) if filename.endswith('.jpg')]
    
    
    # Rectangle color list 
    global colors, col_index
    colors =[(0,255,0),(255,0,0),(0,0,255),
             (255,0,255),(0,255,255),(255,255,0)]
    col_index = 0

	# Working image
    img = cv2.imread(img_path)
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img_clean = img.copy() # Img with never contours or rectangles
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_rectangle)
    
    # Check if the data folder exists
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
    if not os.path.exists('dataset/original'):
        os.makedirs('dataset/original')
    # loop1 - Define the different labels when the space bar is pressed
    loop1 = True
    while loop1:
        print('¿Nombre etiqueta?')
        label = input()
        # Validate if folder exists
        if not os.path.exists(label):
            os.makedirs(f'dataset/original/{label}')
        # loop2 - Captures mouse clicks since the space bar or Esc key has been pressed.
        loop2 = True
        while loop2:
            cv2.imshow('image',img)
            k = cv2.waitKey(20) & 0xFF
            if k == 27: # Esc key
                now = dt.now().strftime("%y%m%d%H%M%S")
                cv2.imwrite(f'dataset/original/{now}_original.png', img_clean)
                cv2.imwrite(f'dataset/original/{now}_result.png', img)
                loop1, loop2 = False, False
            if k == 32: # Space bar
                 col_index += 1
                 if col_index >= len(colors):
                        print('Maximum 6 labels per run')
                        now = dt.now().strftime("%y%m%d%H%M%S")
                        cv2.imwrite(f'dataset/original/{now}_original.png', img_clean)
                        cv2.imwrite(f'dataset/original/{now}_result.png', img)
                        loop1 = False
                 loop2 = False



if __name__ == '__main__':
	main()