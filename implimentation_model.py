import joblib
import numpy as np
import pandas as pd
model = joblib.load('my_model')














# with h5py.File('test.hdf5', 'r') as model:
#     y_cnn = model.predict("\Python\7_0.jpg")
#     plt.figure(figsize=(20,40)) 
#     for i in range(0,43) :
#         plt.subplot(10,5,i+1)
#         plt.axis('off')
#         ny = y_cnn[i]*255
#         image = cv2.rectangle(X_test[i],(int(ny[0]),int(ny[1])),(int(ny[2]),int(ny[3])),(0, 255, 0))
#         plt.imshow(image)