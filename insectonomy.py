import streamlit as st
import pandas as pd
import re

st.title("Insectonomy Species Navigator")
#st.text("Página para navegar los datos.")

r=[]

tablasust=pd.read_csv("SustPot.csv", sep=";")


tablaGen=pd.read_csv("GenAsp.csv", sep=";")

tabla=pd.merge(tablaGen, tablasust, left_index=True, right_index=True)

tabla2=tabla
tabla2[['minHoldPre','maxHoldPre']] = tabla2.HoldPre.str.split("-",expand=True)
tabla2.minHoldPre=pd.to_numeric(tabla2.minHoldPre)
tabla2.maxHoldPre=pd.to_numeric(tabla2.maxHoldPre)

tabla2[['minHoldAD','maxHoldAD']] = tabla2.HoldAD.str.split("-|–",expand=True)
tabla2.minHoldAD=pd.to_numeric(tabla2.minHoldAD)
tabla2.maxHoldAD=pd.to_numeric(tabla2.maxHoldAD)
               
#st.sidebar.subheader('Columns')
col1, col2 = st.sidebar.columns(2)
with col1:
    st.header('General')
#with col2:
#    st.header('Use')



def crearDropdown(columna,ll,sust):
    ##Crea un menu crearDropdown con las opciones únicas de cada columna
   ## ll=tabla.columna.unique()
   ## ll=[]
    realms=[]
    for i in ll:
##        print(i)
        if isinstance(i,str):
            print(i)
            j=re.split(",", i)
        ##       for k in j:
            for k in j:
                k=k.strip()
                if k not in realms:
                    realms.append(k.strip())
    realms.sort()
    
    with columna:
        reinos=st.multiselect("Select "+sust+":",realms)

    query=""
    for i in reinos:
        query=query+i+"|"
    query=query[0:-1]
    return query

query=crearDropdown(col1,tabla.SciNa.unique(),"Scientific Name (SciNa)")
tabla2=tabla2[tabla2["SciNa"].str.contains(query)]

query=crearDropdown(col1,tabla.Or.unique(),"Order (Or)")
tabla2=tabla2[tabla2["Or"].str.contains(query)]

query=crearDropdown(col1,tabla.Fam.unique(),"Family (Fam)")
tabla2=tabla2[tabla2["Fam"].str.contains(query)]

query=crearDropdown(col1,tabla.ComNa.unique(),"Common Name (ComNa)")
tabla2=tabla2[tabla2["ComNa"].str.contains(query)]

#query=crearDropdown(col1,tabla.BiogRe.unique(),"Biogeographic realm (BiogRe)")
#tabla2=tabla2[tabla2["BiogRe"].str.contains(query)]

query=crearDropdown(col1,tabla.CITES.unique(),"CITES classification (CITES)")
tabla2=tabla2[tabla2["CITES"].str.contains(query)]


query=crearDropdown(col1,tabla.IUCN.unique(),"IUCN classification (IUCN)")
tabla2=tabla2[tabla2["IUCN"].str.contains(query)]

#query=crearDropdown(col1,tabla.BiogZo.unique(),"Biogeographic Zone (BiogZo)")
#tabla2=tabla2[tabla2["BiogZo"].str.contains(query)]

query=crearDropdown(col1,tabla.HoldBio.unique(),"Holdrige Biome (HoldBio)")
tabla2=tabla2[tabla2["HoldBio"].str.contains(query)]

query=crearDropdown(col1,tabla.HoldTemp.unique(),"Holdrige Temperature (HoldTemp)")
tabla2=tabla2[tabla2["HoldTemp"].str.contains(query)]

query=crearDropdown(col1,tabla.HoldAB.unique(),"Holdridge, Altitudinal belts (HoldAB)")
tabla2=tabla2[tabla2["HoldAB"].str.contains(query)]

query=crearDropdown(col1,tabla.HoldLR.unique(),"Holdridge, Latitudinal regions (HoldLR)")
tabla2=tabla2[tabla2["HoldLR"].str.contains(query)]

query=crearDropdown(col1,tabla.HabAct.unique(),"Habit of activity (HabAct)")
tabla2=tabla2[tabla2["HabAct"].str.contains(query)]

query=crearDropdown(col1,tabla.HabPat.unique(),"Habitat use patterns (HabPat)")
tabla2=tabla2[tabla2["HabPat"].str.contains(query)]

query=crearDropdown(col1,tabla.LSG.unique(),"Life Stage Generations Biome (LSG)")
tabla2=tabla2[tabla2["LSG"].str.contains(query)]


def crearDropdownNum(columna,ll,sust):
    ##Crea un menu crearDropdown con las opciones únicas de cada columna
   ## ll=tabla.columna.unique()
   ## ll=[]
    realms=[]
    for i in ll:
##        print(i)
        if isinstance(i,int):
            print(i)
            if k not in realms:
                realms.append(k)
    realms.sort()
    
    with columna:
        reinos=st.multiselect("Select "+sust+":",realms)

    query=""
    for i in reinos:
        query=query+i+"|"
    query=query[0:-1]
    return query


#query=crearDropdownNum(col2,tabla.GEconEnvResEffWa.unique(),"Scientific Name (GEconEnvResEffWa)")
#tabla2=tabla2[tabla2["GEconEnvResEffWa"].str.contains(query)]







with st.sidebar:
    st.subheader("Parámetros de busqueda")
    ##st.text("Especie nativa o exótica en Colombia?")
    ##nat=st.checkbox("Native",value=True)
    ##exo=st.checkbox("Exotic",value=True)
    values = st.slider(
    label='Holdrige, Annual precipitation (HoldPre)',
    min_value=0,max_value= 5000, value= (0, 5000))
    valuesAD = st.slider(
    label='Holdrige, Altitudinal distribution (HoldAD)',
    min_value=0,max_value= 3500, value= (0, 3500))


###Selección de la columna exotic
##if nat and not exo:
        ##tabla2=tabla[tabla["exotic"]=="Native"]
        
##else:
    ##if not nat and exo:
        ##tabla2=tabla[tabla["exotic"]=="Exotic"]
    ##else:
        ##tabla2=tabla
    
tabla2=tabla2[tabla2["minHoldPre"]>=values[0]]
tabla2=tabla2[tabla2["maxHoldPre"]<=values[1]]

tabla2=tabla2[tabla2["minHoldAD"]>=valuesAD[0]]
tabla2=tabla2[tabla2["maxHoldAD"]<=valuesAD[1]]

print(tabla2)
print(values)
st.subheader("Generales")
#st.dataframe(tabla2)
st.dataframe(tabla2.loc[:, ~tabla2.columns.isin(['minHoldPre', 'maxHoldPre',"minHoldAD","maxHoldAD"])])

#st.dataframe(tablasust)
st.text("Displayed species: %d"%len(tabla2))
#print(col2)
    ##tabla=tabla[tabla["Exotic or Native to CO"]=="Native"]
 ##GenAsp: General aspects
##Cl: Class
##Or: Order
##Fam: Family
##ComNa: Common name
##SciNa: Scientific name
##BiogRe: Biogeographic realm
##CITES: CITES classification
##IUCN: IUCN classification
##BiogZo: Biogeographic zone
##Hold: Holdridge
##HoldBio: Holdridge, Biome
##HoldPre: Holdridge, Annual precipitation
##HoldTemp: Holdridge, Temperature
##HoldAB: Holdridge, Altitudinal belts
##HoldLR: Holdridge, Latitudinal regions
##HoldAD: Holdridge, Altitudinal distribution
##HabAct: Habit of activity
##HabPat: Habitat use patterns
##LSG: Life stage generations
##Use: Use
#query=crearDropdown(col1,tabla.SciNa.unique(),"Scientific Name (SciNa)")
#tabla2=tabla2[tabla2["SciNa"].str.contains(query)]



#query=crearDropdown(col1,tabla.LSG.unique(),"Life stage generations (LSG)")
#tabla2=tabla2[tabla2["LSG"].str.contains(query)]

#query=crearDropdown(col1,tabla.HoldAB.unique(),"Holdrige altitudinal belts (HoldAB)")
#tabla2=tabla2[tabla2["HoldAB"].str.contains(query)]





#query=crearDropdown(col1,tabla.BiogRe.unique(),"Biogeographic Realm (BiogRe)")
#tabla2=tabla2[tabla2["BiogRe"].str.contains(query)]

#query=crearDropdown(col1,tabla.Fam.unique(),"Family (Fam)")
#tabla2=tabla2[tabla2["Fam"].str.contains(query)]

##query=crearDropdown("CITES",tabla.CITES.unique(),"clasificación CITES")
##tabla2=tabla2[tabla2["CITES"].str.contains(query)]



##query=crearDropdown("LatitudinalRegions",tabla.LatitudinalRegions.unique(),"región latitudinal")
##tabla2=tabla2[tabla2["LatitudinalRegions"].str.contains(query)]

##query=crearDropdown("HabitOfActivity",tabla.HabitOfActivity.unique(),"hábitos")
##tabla2=tabla2[tabla2["HabitOfActivity"].str.contains(query)]

 
###Seleccion de la zona
##l=tabla.zone.unique()
##places=[]
##for i in l:
    ##j=re.split(",| and", i)
 ###       for k in j:
    ##for k in j:
        ##k=k.strip()
        ##if k not in places:
            ##places.append(k.strip())
##places.sort()
##with st.sidebar:
    ##lugares=st.multiselect("Seleccione areas de interés",places)

##query=""
##for i in lugares:
    ##query=query+i+"|"
##query=query[0:-1]
##tabla2=tabla2[tabla2["zone"].str.contains(query)]

#tablaB=pd.read_csv("Use.csv", sep=";")
#tablaB["MarMP"].fillna("None", inplace=True)

#tablaB2=tablaB


##query=crearDropdown(col1,tabla.Fam.unique(),"Family (Fam)")
##tabla2=tabla2[tabla2["Fam"].str.contains(query)]


#query=crearDropdown(col2,tablaB.MarMP.unique(),"clasificación IUCN")
#tablaB2=tablaB2[tablaB2["MarMP"].str.contains(query)]
#print(query)
#st.text(query)
##query=crearDropdown(col2,tablaB.MaUSubs.unique(),"clasificación IUCN")
##tablaB2=tablaB2[tablaB2["MaUSubs"].str.contains(query)]

##query=crearDropdown(col2,tablaB.MarMP.unique(),"clasificación IUCN")
##tablaB2=tablaB2[tabla2["MarMP"].str.contains(query)]




##st.text("Total especies desplegadas %d"%len(tabla2))
#st.subheader("Generales")
#st.dataframe(tabla2)
#st.subheader("Uso")
#st.dataframe(tablaB2)
            
##places
##st.dataframe(tabla2)
##st.image("Kabutomushi-JapaneseBeetle-July2004.jpg",caption="Trypoxylus dichotomus o Rinoceronte japonés")
