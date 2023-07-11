import streamlit as st
import pandas as pd
import re

st.title("Página Principal Insectonomy")
st.subheader("Resultados de la busqueda")
#st.text("Página para navegar los datos.")

r=[]

tabla=pd.read_csv("General.csv", sep=";")
tabla2=tabla

    #tabla=tabla[tabla["Exotic or Native to CO"]=="Native"]

with st.sidebar:
    st.subheader("Parámetros de busqueda")
    st.text("Especie nativa o exótica en Colombia?")
    nat=st.checkbox("Native",value=True)
    exo=st.checkbox("Exotic",value=True)

#Selección de la columna exotic
if nat and not exo:
        tabla2=tabla[tabla["exotic"]=="Native"]
        
else:
    if not nat and exo:
        tabla2=tabla[tabla["exotic"]=="Exotic"]
    else:
        tabla2=tabla
 
#Seleccion de la zona
l=tabla.zone.unique()
places=[]
for i in l:
    j=re.split(",| and", i)
 #       for k in j:
    for k in j:
        k=k.strip()
        if k not in places:
            places.append(k.strip())
places.sort()
with st.sidebar:
    st.text("Selecciones la(s) zona(s)")
    lugares=st.multiselect("Seleccione areas de interés",places)

query=""
for i in lugares:
    query=query+i+"|"
query=query[0:-1]
tabla2=tabla2[tabla2["zone"].str.contains(query)]



 
#Seleccion de la "Biogeographic realm
ll=tabla.Biogeographicrealm.unique()
realms=[]
for i in ll:
    j=re.split(",| and", i)
 #       for k in j:
    for k in j:
        k=k.strip()
        if k not in realms:
            realms.append(k.strip())
realms.sort()
with st.sidebar:
    reinos=st.multiselect("Seleccione los reinos de interés",realms)

query=""
for i in reinos:
    query=query+i+"|"
query=query[0:-1]
tabla2=tabla2[tabla2["Biogeographicrealm"].str.contains(query)]


#Seleccion del CLIMA
cl=tabla.Climate.unique()
with st.sidebar:
    st.text("Selección del clima")
    climas=st.multiselect("Seleccione los climas de interés",cl)
query=""
for i in climas:
    query=query+i+"|"
#    tabla[tabla["zone"].str.contains("America|Europe")]["zone"]
query=query[0:-1]
tabla2=tabla2[tabla2["Climate"].str.match(query)]


st.text("Total especies desplegadas %d"%len(tabla2))

tabla2
            
#places
#st.dataframe(tabla2)
#st.image("Kabutomushi-JapaneseBeetle-July2004.jpg",caption="Trypoxylus dichotomus o Rinoceronte japonés")
