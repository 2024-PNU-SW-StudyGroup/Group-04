from flask import Flask, Response
import cv2
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 웹캠 사용 (기본 0번 웹캠)
save_path = "saved_images"  # 이미지를 저장할 폴더

# 저장 폴더가 존재하지 않으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)

def generate_frames():
    frame_count = 0  # 저장할 이미지에 대한 파일 이름을 관리하는 카운터

    while True:
        success, frame = camera.read()  # 웹캠에서 프레임 읽기
        if not success:
            break
        else:
            # 이미지를 jpg로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_data = buffer.tobytes()

            # 스트리밍 데이터 생성
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')
            
            # 파일로 이미지 저장
            frame_filename = os.path.join(save_path, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)  # 프레임을 jpg 파일로 저장
            frame_count += 1

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
