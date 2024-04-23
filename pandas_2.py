#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pandas


# In[4]:


import pandas as pd


# Crear una serie
# 

# arreglo unidimensional de datos
# 

# In[18]:


miSerie=pd.Series((34,56,78,23,34))
miSerie


# #DICCRIONARIO EN PYTHON
# Estructura que guarda datos en una funcion de objetos llave-valor

# In[41]:


miDiccionario={
    "Nombre": "Casa_1",
    "Area":  120 ,
    "Baños": 3,
    "Propietarios": [
                "Paulo","Diana"
    ],
     "Barrio": {
         "Nombre": "Gran Britalia",
         "Localidad":"Bosa"
     }
         
     
}
    
miDiccionario     


# In[44]:


miDataframe = pd.DataFrame ({"si":[10,15],"no":[50,68]})
miDataframe


# In[ ]:





# In[ ]:





# In[ ]:




