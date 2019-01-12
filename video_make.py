import cv2
import cv2
import argparse
import os


def movie_to_image(num_cut):
    


    output_path = '/Users/dukeglacia/Downloads/test_images/'  # 出力するフォルダパス

    # capture video 
    capture = cv2.VideoCapture(0)

    img_count = 0  # No of images saved
    frame_count = 0  # No of frames read

    # while there is a frame input
    while(capture.isOpened()):
         # collect one frame
        ret, frame = capture.read()
        if ret == False:
            break

  
        if frame_count % num_cut == 0:
            img_file_name = output_path + str(img_count) + ".jpg"
            cv2.imwrite(img_file_name, frame)
            img_count += 1

        frame_count += 1

    # release the capture
    capture.release()


if __name__ == '__main__':    

    # read frames per numcut frames
    movie_to_image(int(1))
