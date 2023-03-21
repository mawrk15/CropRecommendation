import streamlit as st
import pickle
import pickle
import sklearn
import pandas as pd
import numpy as np
model = pickle.load(open('model.sav', 'rb'))

st.title('Crop Recommendation Prediction')
st.sidebar.header('Environment Data')


# FUNCTION
def user_report():
  N = st.sidebar.slider('Nitrogen', 0,100, 1 )
  P = st.sidebar.slider('Phosphorus', 0,100, 1 )
  K = st.sidebar.slider('Potassium', 0,100, 1 )
  Temp = st.sidebar.slider('Temperature', 10,45, 1 )
  Hum = st.sidebar.slider('Humidity', 0,100, 0.01 )
  pH = st.sidebar.slider('pH', 3,9, .001)
  Rain = st.sidebar.slider('Rainfall', 0,400, 1)


  user_report_data = {
      'Nitrogen':N,
      'Phosphorus':P,
      'Potassium':K,
      'Temperature':Temp,
      'Humidity':Hum,
      'pH':pH,
      'Rainfall':Rain,
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Environment Data')
st.write(user_data)

crop_name = model.predict(user_data)
for predict1 in range(len(crop_name)):
	if crop_name[i]==1:
		if predict1 == 0:
			crop_name = 'Apple'
		elif predict1 == 1:
        		crop_name = 'Banana'
		elif predict1 == 2:
			crop_name = 'Blackgram'
		elif predict1 == 3:
			crop_name = 'Chickpea'
		elif predict1 == 4:
	 		crop_name = 'Coconut'
		elif predict1 == 5:
			crop_name = 'Coffee'
		elif predict1 == 6:
			crop_name = 'Cotton'
		elif predict1 == 7:
			crop_name = 'Grapes'
		elif predict1 == 8:
			crop_name = 'Jute'
		elif predict1 == 9:
			crop_name = 'Kidneybeans'
		elif predict1 == 10:
			crop_name = 'Lentil'
		elif predict1 == 11:
			crop_name = 'Maize'
		elif predict1 == 12:
			crop_name = 'Mango'
		elif predict1 == 13:
		    	crop_name = 'Mothbeans'
		elif predict1 == 14:
			crop_name = 'Mungbeans'
		elif predict1 == 15:
		    	crop_name = 'Muskmelon'
		elif predict1 == 16:
		    	crop_name = 'Orange'
		elif predict1 == 17:
		    	crop_name = 'Papaya'
		elif predict1 == 18:
		    	crop_name = 'Pigeonpeas'
		elif predict1 == 19:
		    	crop_name = 'Pomegranate'
		elif predict1 == 20:
		    	crop_name = 'Rice'
		elif predict1 == 21:
	    		crop_name = 'Watermelon'
st.subheader('Crop Recommended')
st.subheader(str(crop_name))
