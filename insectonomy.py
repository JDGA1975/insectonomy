import streamlit as st
import pandas as pd
import re

st.title("Página Principal Insectonomy")
st.subheader("Resultados de la busqueda")
#st.text("Página para navegar los datos.")

r=[]

tabla=pd.read_csv("General.csv", sep=";")
tabla2=tabla

def crearDropdown(columna,ll,sust):
    #Crea un menu crearDropdown con las opciones únicas de cada columna
   # ll=tabla.columna.unique()
   # ll=[]
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
        reinos=st.multiselect("Seleccione "+sust+":",realms)

    query=""
    for i in reinos:
        query=query+i+"|"
    query=query[0:-1]
    return query

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
 
query=crearDropdown("Lifestage",tabla.Lifestage.unique(),"la etapa de vida")
tabla2=tabla2[tabla2["Lifestage"].str.contains(query)]

query=crearDropdown("Biogeographicrealm",tabla.Biogeographicrealm.unique(),"los reinos biogeográficos")
tabla2=tabla2[tabla2["Biogeographicrealm"].str.contains(query)]

query=crearDropdown("Climate",tabla.Climate.unique(),"los climas")
tabla2=tabla2[tabla2["Climate"].str.contains(query)]

 
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
    lugares=st.multiselect("Seleccione areas de interés",places)

query=""
for i in lugares:
    query=query+i+"|"
query=query[0:-1]
tabla2=tabla2[tabla2["zone"].str.contains(query)]






st.text("Total especies desplegadas %d"%len(tabla2))

st.dataframe(tabla2)
            
#places
#st.dataframe(tabla2)
#st.image("Kabutomushi-JapaneseBeetle-July2004.jpg",caption="Trypoxylus dichotomus o Rinoceronte japonés")
