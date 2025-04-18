import pandas as pd
import streamlit as st
import folium

# 讀取資料
ambulance = pd.read_excel(r'ambulance2022-07-05.xlsx')
cap = pd.read_excel(r'分局資料.xlsx')

# 顯示標題
st.title("救護車派遣地圖")

# 函數：繪製分局位置標記
def add_station_markers(yunlin_map, cap):
    for lat_cap, log_cap, name in zip(cap['緯度'], cap['經度'], cap['分局']):
        html = f"<p>分局名稱: {name}</p>"
        # icon = folium.Icon()
        folium.Marker(location=[lat_cap, log_cap], tooltip=html).add_to(yunlin_map)

# 函數：繪製事發地點和派遣分局標記
def add_accident_and_dispatch_markers(yunlin_map, ambulance, cap, num):
    lat = ambulance['事發緯度'][num]
    log = ambulance['事發經度'][num]
    cap_go_lat = ambulance['分局緯度'][num]
    cap_go_log = ambulance['分局經度'][num]
    cap_go_name = ambulance['派遣分局'][num]
    accident = ambulance['事發地點'][num]

    # 事發地點標記
    accident_html = f"<p>事發地點: {accident}</p><p>派遣分局: {cap_go_name}</p>"
    accident_marker = folium.Marker(
        location=[lat, log],
        icon=folium.Icon(icon='fa-ambulance', color='red', prefix='fa'),
        tooltip=accident_html
    )
    accident_marker.add_to(yunlin_map)

    # 派遣分局標記
    cap_go_html = f"<p>派遣分局: {cap_go_name}</p>"
    cap_go_marker = folium.Marker(
        location=[cap_go_lat, cap_go_log],
        icon=folium.Icon(color='black'),
        tooltip=cap_go_html
    )
    cap_go_marker.add_to(yunlin_map)

# 建立雲林地圖
yunlin_map = folium.Map(location=[23.68, 120.3], zoom_start=11)

# 輸入案件編號
num = int(st.text_input("請輸入想分析的案件:"))

# 根據案件編號進行分析
if num:
    try:
        # 繪製分局位置
        add_station_markers(yunlin_map, cap)
        
        # 繪製事發地點和派遣分局
        add_accident_and_dispatch_markers(yunlin_map, ambulance, cap, num)

        # 顯示地圖
        st.components.v1.html(folium.Figure().add_child(yunlin_map).render(), height=500)

    except ValueError:
        st.error("請輸入正確的案件編號")
        st.stop()
