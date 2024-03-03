import pickle
import numpy as np

def car_price_prediction(normalizedlosses, wheelbase, width, curbweight, enginesize, horsepower, citympg ,highwaympg ):
    with open(r'artifacts\random_forest_reg_model.pkl', 'rb') as f:
        model = pickle.load(f)

   # test_array = np.zeros((model.n_features_in_))
   # test_array[0,0] = normalizedlosses
  #  test_array[0,1] = wheelbase
   # test_array[0,2] = width
    #test_array[0,3] = curbweight
    #test_array[0,4] = enginesize
    #test_array[0,5] = horsepower
    #test_array[0,6] = citympg
    #test_array[0,7] = highwaympg
    test_array1 =np.array([[normalizedlosses, wheelbase, width, curbweight, enginesize, horsepower, citympg ,highwaympg ]])
    print('****')

    predicted_price = model.predict(test_array1)
    print("predicted_price :",predicted_price)

    return predicted_price

