#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:32:57 2019

@author: bruno_dbki
"""



import xmltodict
import os
import pandas as pd


values=[]     
# os.chdir("xml")

for xml in os.listdir():
    
    with open(xml) as fd:
        nfe = xmltodict.parse(fd.read())
    
    
    nfe_id = nfe['nfeProc']['NFe']['infNFe']['@Id'] # infNFe Id
    itens = nfe['nfeProc']['NFe']['infNFe']['det']
    
    print("NFe: ", nfe_id)
    print("NCM      |   Equipamento")
    
    for item in itens:
        prods = []
        for key in item['prod'].keys():
            prods.append(item['prod'][key])
        
        values.append(prods)
        prods.append(nfe_id)
        #values.append([item['prod']['NCM'],  item['prod']['xProd']])
        #print(item.keys())
    #    for i in range(len(item)):
    #        values.append(item[i][0])
                
#print(values)
df = pd.DataFrame.from_records(values)
col = list(item['prod'].keys())
col.append('Nfe')
df.columns = col
#print(df)
print(df[['xProd','NCM','CFOP']])
#df.set_index()
