import streamlit as st
import pandas as pd
st.title("Página Principal Insectonomy")
st.subheader("Características generales")
st.text("Parrafo de html")
st.markdown("## **Hello** world. *juan*")
st.markdown("> Bloque")
st.markdown("[Google is here](google.com)")

st.code("import pandas as pd")
r=[]
tabla=pd.read_csv("General.csv", sep=";")
tabla2=tabla


            #tabla=tabla[tabla["Exotic or Native to CO"]=="Native"]
nat=st.checkbox("Native",value=True)
exo=st.checkbox("Exotic",value=True)

if nat and not exo:
        st.header("Marco")
        tabla2=tabla[tabla["exotic"]=="Native"]
        
else:
    if not nat and exo:
        st.header("Polo")
        tabla2=tabla[tabla["exotic"]=="Exotic"]
    else:
        tabla2=tabla
 
l=tabla.zone.unique()
import re
places=[]
for i in l:
    j=re.split(",| and", i)
 #       for k in j:
    for k in j:
        k=k.strip()
        if k not in places:
            places.append(k.strip())

places.sort()
lugares=st.multiselect("Seleccione areas de interés",places)

lugares
#r.append(region)
#r
query=""
for i in lugares:
    query=query+i+"|"
#    tabla[tabla["zone"].str.contains("America|Europe")]["zone"]
query=query[0:-1]
tabla2=tabla2[tabla2["zone"].str.contains(query)]

l=tabla.zone.unique()
tabla2
#CLIMAS
cl=tabla.Climate.unique()
climas=st.multiselect("Seleccione los climas de interés",cl)
query=""
for i in climas:
    query=query+i+"|"
#    tabla[tabla["zone"].str.contains("America|Europe")]["zone"]
query=query[0:-1]
climas

tabla2=tabla2[tabla2["Climate"].str.match(query)]


tabla2
            
#places
#st.dataframe(tabla2)
#st.image("Kabutomushi-JapaneseBeetle-July2004.jpg",caption="Trypoxylus dichotomus o Rinoceronte japonés")
