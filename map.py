import folium
import pandas as pd
ambulance_file_path=r'/content/ambulance2022-07-05.xlsx'
cap_path=r'/content/分局資料.xlsx'
ambulance=pd.read_excel(ambulance_file_path)
cap=pd.read_excel(cap_path)
ambulance.keys(),cap.keys(),ambulance
yunlin_map=folium.Map(location=[23.68,120.3],zoom_start=11)  #產生雲林地圖
lat=ambulance['事發緯度']
log=ambulance['事發經度']
cap_go_lat=ambulance['分局緯度']
cap_go_log=ambulance['分局經度']
cap_go_name=ambulance['派遣分局']
accident=ambulance['事發地點']

num=int(input("請輸入想分析的案件:"))
for lat_cap,log_cap,name in zip(cap['緯度'],cap['經度'],cap['分局']): 
        html="""<p>分局名稱:<p>""" + name
        #tooltip=folium.GeoJsonTooltip(fields=['分局名稱'],aliases=[name])
        icon=folium.Icon(icon="user - police",prefix='fa')
        yunlin_map.add_child(folium.Marker(location=[lat_cap,log_cap],icon=icon,tooltip=html)) #將各地點劃記在地圖上
html="""<p>事發地點:<p>""" + accident[num] + """<p>派遣分局:<p>""" + cap_go_name[num] 
accident1=folium.Marker(location=[lat[num],log[num]],icon=folium.Icon(icon='fa-ambulance',color='red',prefix='fa'),tooltip=html)
html_cap="""<p>派遣分局<p>""" + cap_go_name[num]
cap_go=folium.Marker(location=[cap_go_lat[num],cap_go_log[num]],icon=folium.Icon(color='black'),tooltip=html_cap)
yunlin_map.add_child(accident1)
yunlin_map.add_child(cap_go)
yunlin_map
