from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from predict import predict
app = Flask(__name__)

'''
predict.py 에 경로를 자신의 컴퓨터상황에 맞춰서 하시면 끝납니다.
모델에 넣기 위해 이미지 255*255 로 만들고 넣어야 함 

index.html에 주석을 몰라 여기다 적겠습니다. 
일단 우리의 Css를 적용하기 위해서 원래 링크에 주소를 적으면 되지만 flask에서 사용하기 위해서는 url_for에 감싸서 넣어야합니다.


'''
# route 뒤에 '/'를 바꾸면 자기가 원하는 도메인주소에 열림
@app.route('/', methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        file = request.files["image"] # 여기에 우리 업로드 되는 이름 넣으면 됨
        img = Image.open(file)
        img = np.array(img.resize((256,256))).reshape(256,256,3)
        label = predict(img)
        prime = label[0][0]
        choice= label[0][1]
        Select= label[0][2]
        max_prob = max([prime,choice,Select])
        max_label = [prime,choice,Select].index(max([prime,choice,Select]))
        # 이름 넣기위한 코드(하) 
        if max_label == 0:
            max_label = 'Prime'
        elif max_label == 1:
            max_label = 'Choice'
        elif max_label == 2:
            max_label = 'Select'
        return render_template('index.html',max=max_prob,max_label=max_label ,prime = round(prime,2), choice= round(choice,2), Select= round(Select,2), label='등급')
    return render_template('index.html' ,label='고기 사진 주세요')



if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)