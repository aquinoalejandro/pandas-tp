import pandas as pd


edadeslist = [20,30,19,20,21,18,17,18,19,19,19,19,19,25,18,21,21,22,23,24,20,30,19,20,21,18,17,18,19,19]
def analisis_estadistico(edadeslist):
    data_frame = pd.DataFrame()
    data_frame["edades"] = pd.Series((sorted(set(edadeslist))))
    data_frame["fi"] = data_frame['edades'].map(edadeslist.count)
    data_frame["Fi"] = data_frame['fi'].cumsum()
    data_frame["ri"] = data_frame['fi'] / data_frame['fi'].sum()
    data_frame["Ri"] = data_frame['ri'].cumsum()
    data_frame["pi%"] = data_frame['ri'] * 100
    data_frame["Pi%"] = data_frame['pi%'].cumsum()
    return data_frame

print(analisis_estadistico(edadeslist))