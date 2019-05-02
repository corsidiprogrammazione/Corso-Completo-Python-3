import folium

mappa = folium.Map(location=[45.495523, 9.190973],zoom_start=8,tiles="Mapbox Bright")

mia_mappa = folium.FeatureGroup(name="Mia Mappa")

mia_mappa.add_child(folium.Marker(location=[45.495523, 9.190973],popup="Milano",icon=folium.Icon(color='red')))

mia_mappa.add_child(folium.Marker(location=[41.901210, 12.585783],popup="Roma",icon=folium.Icon(color='blue')))


mia_mappa.add_child(folium.CircleMarker(location=[45.495523, 8.190973],popup="Milano",radius=10,color='violet',fill_color="green",fill_opacity=1))

regioni = folium.FeatureGroup(name="Regioni")

regioni.add_child(folium.GeoJson(data=open("geo.json","r",encoding="utf-8-sig").read()))

mappa.add_child(mia_mappa)

mappa.add_child(regioni)

mappa.add_child(folium.LayerControl())

mappa.save('mappa1.html')