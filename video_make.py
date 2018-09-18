import cv2
import cv2
import argparse
import os


def movie_to_image(num_cut):
    

#     video_path = '/hoge/hoge.mov'   # キャプチャ動画のパス（ファイル名含む）
    output_path = '/Users/dukeglacia/Downloads/test_images/'  # 出力するフォルダパス

    # キャプチャ動画読み込み（キャプチャ構造体生成）
    capture = cv2.VideoCapture(0)

    img_count = 0  # 保存した候補画像数
    frame_count = 0  # 読み込んだフレーム画像数

    # フレーム画像がある限りループ
    while(capture.isOpened()):
         # フレーム画像一枚取得
        ret, frame = capture.read()
        if ret == False:
            break

        # 指定した数だけフレーム画像を間引いて保存
        if frame_count % num_cut == 0:
            img_file_name = output_path + str(img_count) + ".jpg"
            cv2.imwrite(img_file_name, frame)
            img_count += 1

        frame_count += 1

    # キャプチャ構造体開放
    capture.release()


if __name__ == '__main__':    

    # 間引き数を10にしてフレーム画像抽出
    movie_to_image(int(1))