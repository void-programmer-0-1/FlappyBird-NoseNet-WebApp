
import cv2
import numpy as np

def draw_annotation():
    
    image = cv2.imread("cat_dog.jpg")

    cat = (199,413)
    dog = (375,260)

    image = cv2.circle(image, (cat[0],cat[1]), radius=5, color=(0, 0, 255), thickness=-1)
    image = cv2.circle(image, (dog[0],dog[1]), radius=5, color=(0, 0, 255), thickness=-1)

    cv2.imwrite("original_result.jpg",image)


def draw_annotation_resized_image():

    cat = (199,413)
    dog = (375,260)

    resized_x = 224
    resized_y = 224

    image = cv2.imread("cat_dog.jpg")

    original_x = image.shape[1]
    original_y = image.shape[0]

    image = cv2.resize(image,(resized_x,resized_y))

    x_scale = (resized_x / original_x)
    y_scale = (resized_y / original_y)

    cat_x = int(np.round(cat[0] * x_scale))
    cat_y = int(np.round(cat[1] * y_scale))

    print("cat x :: ",cat_x)
    print("cat y :: ",cat_y)

    dog_x = int(np.round(dog[0] * x_scale))
    dog_y = int(np.round(dog[1] * y_scale))

    print("dog x :: ",dog_x)
    print("dog y :: ",dog_y)


    image = cv2.circle(image, (cat_x,cat_y), radius=5, color=(0, 0, 255), thickness=-1)
    image = cv2.circle(image, (dog_x,dog_y), radius=5, color=(0, 0, 255), thickness=-1)

    cv2.imwrite("resized_result.jpg",image)


draw_annotation()
draw_annotation_resized_image()