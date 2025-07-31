from utils.utils import cpu,Gpu

def data_cleaning(loaded_data):

    loaded_data = loaded_data.dropna()
    loaded_data = loaded_data.drop_duplicates()
    loaded_data = loaded_data.drop(columns="Unnamed: 0")

    loaded_data["Ram"] = loaded_data["Ram"].str.replace("GB","")
    loaded_data["Ram"] = loaded_data["Ram"].astype(int)

    loaded_data["Weight"] = loaded_data["Weight"].str.replace("kg","")
    loaded_data["Weight"] = loaded_data["Weight"].astype(float)

    loaded_data = loaded_data.drop(columns="Memory")

    loaded_data["ScreenResolution"] = loaded_data["ScreenResolution"].str.extract(r'(\d+x\d+)')
    loaded_data[["width","Height"]] = loaded_data["ScreenResolution"].str.split("x",expand=True)
    loaded_data = loaded_data.drop(columns="ScreenResolution")

    loaded_data['Height'] = loaded_data['Height'].astype(int)
    loaded_data['width'] = loaded_data['width'].astype(int)

    loaded_data["Cpu"] = loaded_data["Cpu"].apply(cpu)
    loaded_data["Gpu"] = loaded_data["Gpu"].apply(Gpu)
    

    for i in loaded_data["Cpu"]:
        if "i5" in i:
            loaded_data["Cpu"] = loaded_data["Cpu"].replace(i,"i5")
        elif "i7" in i:
            loaded_data["Cpu"] = loaded_data["Cpu"].replace(i,"i7")
        elif "i3" in i:
            loaded_data["Cpu"] = loaded_data["Cpu"].replace(i,"i3")
        else:
            loaded_data["Cpu"] = loaded_data["Cpu"].replace(i,"others")


    for i in loaded_data["Gpu"]:
        if "Intel" in i:
            loaded_data["Gpu"] = loaded_data["Gpu"].replace(i,"Intel")
        elif "AMD" in i:
            loaded_data["Gpu"] = loaded_data["Gpu"].replace(i,"AMD")
        else:
            loaded_data["Gpu"] = loaded_data["Gpu"].replace(i,"others")


    return loaded_data