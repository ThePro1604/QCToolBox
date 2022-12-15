import os
import cv2

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        full_path = os.path.join(folder,filename)
        if "." in full_path:
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                print(img)
                images.append(img)
    return images

load_images_from_folder("N:\Images\Shahaf\SupportBatch\Airbnb_ARE_Passport_Null")