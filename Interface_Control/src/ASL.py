from roboflow import Roboflow
rf = Roboflow(api_key="6ZANGYXLjoRIUYFMuSMm")
project = rf.workspace().project("asl-omrvrl")
model = project.version(1).model
import cv2 as cv
import numpy as np


def PredictviaCam():

    # f = cv.VideoCapture(0)

    # while True:
        # ret, frame = f.read()
        # cv.imshow('frame', frame)
        # cv.imwrite('temp.jpg',frame)
        # infer on a local image
    prediction =[]
    pred_letters=model.predict("temp.jpg").json()['predictions'][0]['predictions'].keys()
    prediction = model.predict("temp.jpg").json()['predictions'][0]['predictions']
    pred_letters = list(pred_letters)
    max_key = max(prediction, key=lambda k: max(prediction[k].values()))
    print(max_key)
    return max_key

        # predictions = model.predict('temp.jpg')
        # predictions_json = predictions.json()
        # printing all detection results from the image
        # print(predictions_json)
        # accessing individual predicted boxes on each image
        # for bounding_box in predictions:
            # x0 = bounding_box['x'] - bounding_box['width'] / 2#start_column
            # x1 = bounding_box['x'] + bounding_box['width'] / 2#end_column
            # y0 = bounding_box['y'] - bounding_box['height'] / 2#start row
            # y1 = bounding_box['y'] + bounding_box['height'] / 2#end_row
            # class_name = bounding_box['class']
            # confidence_score = bounding_box['confidence']
            # # c1 = x0,y0  
            # # c2 = x1,y1
            # # cv.rectangle('temp.jpg',(int(c1[0]), int(c1[1])), (int(c2[0]), int(c2[1])),(0,0,250),2)

            # detection_results = bounding_box
            # class_and_confidence = (class_name, confidence_score)
            # print(class_and_confidence, '\n')
        # if cv.waitKey(1) & 0xFF == ord('q'):
    #     #     break

    # f.release()
    # cv.destroyAllWindows()



    # # max_key = max(prediction, key=lambda keys: prediction[keys])
    # # print(max_key)

    # ## Arama algoritması
    # max_key = max(prediction, key=lambda k: max(prediction[k].values()))
    # print(max_key)




# visualize your prediction
#model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())