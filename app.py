# import pickle
import joblib
import streamlit as st

import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    st.title('Mobile Price Classification')
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Mobile Price Classification App</h2>
    <h4 style="color:white;text-align:center;">Developer: Tushar Siddik</h4>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    battery_power = st.text_input("Battery Power", '0')
    blue = st.selectbox("Bluetooth", ['0', '1'])
    clock_speed = st.text_input("Clock Speed", '0') 
    dual_sim = st.selectbox("Dual Sim", ['0', '1'])
    fc = st.text_input("Front Camera", '0')   
    four_g = st.selectbox("4G Support", ['0', '1'])
    int_memory = st.text_input("Internal Memory", '0')
    m_dep = st.text_input("Mobile Depth", '0')
    mobile_wt = st.text_input("Mobile Weight", '0')
    n_cores = st.text_input("Number of Cores", '0')
    pc = st.text_input("Primary Camera", '0')
    px_height = st.text_input("Pixel Height", '0')
    px_width = st.text_input("Pixel Width", '0')
    ram = st.text_input("RAM", '0')
    sc_h = st.text_input("Screen Height", '0')
    sc_w = st.text_input("Screen Width", '0')
    talk_time = st.text_input("Talktime", '0')
    three_g = st.selectbox("3G Support", ['0', '1'])
    touch_screen = st.selectbox("Touch Screen", ['0', '1'])
    wifi = st.selectbox("Wifi", ['0', '1'])
    
    with open ('models/model_svc_grid.pkl', 'rb') as f:
        model = joblib.load(f)
    
    if st.button("Predict"):
        # features = [battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]
        
        data = {
            'battery_power' : [float(battery_power)],
            'blue' : [int(blue)],
            'clock_speed' : [float(clock_speed)],
            'dual_sim' : [int(dual_sim)],
            'fc' : [float(fc)],
            'four_g' : [int(four_g)],
            'int_memory' : [float(int_memory)],
            'm_dep' : [float(m_dep)],
            'mobile_wt' : [float(mobile_wt)],
            'n_cores' : [float(n_cores)],
            'pc' : [float(pc)],
            'px_height' : [float(px_height)],
            'px_width' : [float(px_width)],
            'ram' : [float(ram)],
            'sc_h' : [float(sc_h)],
            'sc_w' : [float(sc_w)],
            'talk_time' : [float(talk_time)],
            'three_g' : [int(three_g)],
            'touch_screen' : [int(touch_screen)],
            'wifi' : [int(wifi)],
        }
        
        
        # df = pd.DataFrame([list(data.values())], columns = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi'])
        
        df = pd.DataFrame().from_dict(data)
        
        # std_scaler = StandardScaler()
        # df = std_scaler.fit_transform(df.values)
        
        # features_list = df.values.tolist()
        # prediction = int(model.predict(features_list))
        
        prediction = int(model.predict(df))
        
        if prediction == 0:
            text = 'low cost mobile'
        elif prediction == 1:
            text = 'medium cost mobile'
        elif prediction == 2:
            text = 'high cost mobile'
        else:
            text = 'very high cost mobile'
        
        st.success(f'This is a {text}!')
        # st.success(print(df))
        
if __name__ == '__main__':
    main()
