r"""°°°
Veri seti hikayesi ve yapisinin incelenmesi
°°°"""
# |%%--%%| <Ynpy4w00lb|vfxbEIthRd>

import seaborn as sns
planets = sns.load_dataset("planets")
planets.head()

# |%%--%%| <vfxbEIthRd|Eqh5HfeKT2>
r"""°°°
Veri setinini hikayesi nedir?
°°°"""
# |%%--%%| <Eqh5HfeKT2|vcji574daW>

df = planets.copy()
df.head()
df.tail()

# |%%--%%| <vcji574daW|6XUkTCzsKA>
r"""°°°
Veri seti yapisal bilgileri
°°°"""
# |%%--%%| <6XUkTCzsKA|qmXmXEwp8W>

df.info()
df.dtypes

import pandas as pd
df.method = pd.Categorical(df.method)
df.dtypes
df.head

# |%%--%%| <qmXmXEwp8W|FPuDy65ibF>
r"""°°°
 Veri setinin betimlenmesi
°°°"""
# |%%--%%| <FPuDy65ibF|vHPA9PW8ga>

import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()
df.head
df.shape
df.columns
df.describe(include="all").T

# |%%--%%| <vHPA9PW8ga|bg0a1FDGAp>
r"""°°°
Eksik degerlerin incelenmesi
°°°"""
# |%%--%%| <bg0a1FDGAp|gOENWSVl2N>

import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()
df.head

# |%%--%%| <gOENWSVl2N|5kJUsfz6n3>
r"""°°°
Hic eksik gozlem (deger) var mi?
°°°"""
# |%%--%%| <5kJUsfz6n3|jBHMEdoUxa>

df.isnull().values.any()

# |%%--%%| <jBHMEdoUxa|wh0gH3APBH>
r"""°°°
Hangi degiskende kacar tane var?
°°°"""
# |%%--%%| <wh0gH3APBH|W4NeaEjSrB>

df.isnull().sum()
df["orbital_period"].fillna(0, inplace = True)
df.isnull().sum()
df["mass"].fillna(df.mass.mean(), inplace = True)
df.isnull().sum()
df.fillna(df.mean(), inplace = True)
df.isnull().sum()
df = planets.copy()
df.head()
df.isnull().sum()

# |%%--%%| <W4NeaEjSrB|Vnj6cRPEcl>
r"""°°°

°°°"""