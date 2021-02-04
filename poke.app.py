import streamlit as st
import pandas as pd

# Mask Code
def maskdata(LIST):
    if LIST.any():
        dfret = df[LIST]
    if not LIST.any():
        dfret = df
    return dfret

# Read Data
df = pd.read_csv("https://raw.githubusercontent.com/h3mps/pokemon/main/Pokedex-01-2021-advanced.csv", dtype=object)
df.fillna('', inplace=True)
df_P = df

TAKEN = []
# Display Variables
# displayvars = ["name", "type1", "type2", "tier", "hp", "atk", "def", "spa", "spd", "spe", "bst", "ourank", "rank1"]

POKEMON = list(df['name'].unique())
MON_SELECT = st.sidebar.multiselect('Pokemon', POKEMON, key=1)
mask_mon = df['name'].isin(MON_SELECT)

TYPES = list(df['type1'].unique())
TYPE_SELECT = st.sidebar.multiselect('Select Types', TYPES)
mask_types = df['type1'].isin(TYPE_SELECT) | df['type2'].isin(TYPE_SELECT)

TIER = list(df['tier'].unique())
TIER_SELECT = st.sidebar.multiselect('Select Tier', TIER)
mask_tier = df['tier'].isin(TIER_SELECT)

ROLE = list(df['roletype'].unique())
ROLE_SELECT = st.sidebar.multiselect('Select Role', ROLE)
mask_role = df['roletype'].isin(ROLE_SELECT)

RECOVERY = list(df['recovery'].unique())
RECOVERY_SELECT = st.sidebar.multiselect('Recovery?', RECOVERY)
mask_recovery = df['recovery'].isin(RECOVERY_SELECT)

HAZARDS = list(df['hazards'].unique())
HAZARDS_SELECT = st.sidebar.multiselect('Hazards?', HAZARDS)
mask_hazards = df['hazards'].isin(HAZARDS_SELECT)

MOM = list(df['momentum'].unique())
MOM_SELECT = st.sidebar.multiselect('Momentum?', MOM)
mask_mom = df['momentum'].isin(MOM_SELECT)

HAZARDSR = list(df['hazremoval'].unique())
HAZARDSR_SELECT = st.sidebar.multiselect('Hazard Removal?', HAZARDSR)
mask_hazardsr = df['hazremoval'].isin(HAZARDSR_SELECT)

# RANK_SELECT = st.sidebar.slider('Select Tier', min_value=0, max_value=250)
# mask_rank = df['rank1'].isin(RANK_SELECT)

df = maskdata(mask_mon)
df = maskdata(mask_types)
df = maskdata(mask_tier)
df = maskdata(mask_role)
df = maskdata(mask_recovery)
df = maskdata(mask_hazards)
df = maskdata(mask_mom)
df = maskdata(mask_hazardsr)
# df = maskdata(mask_rank)

# displaydf = df[displayvars]

g = df['code1']
h = df['code2']
j = df['font1']
k = df['font2']

# apply the colors to style for columns A and B
def highlight_color1(x):
    return ['background-color: {}'.format(i) for i in g]

def highlight_color2(x):
    return ['background-color: {}'.format(i) for i in h]

def highlight_text1(x):
    return ['color: {}'.format(i) for i in j]

def highlight_text2(x):
    return ['color: {}'.format(i) for i in k]

st.title("Pokemon Draft App")
st.write("Use this app to filter pokemon and see what your team is missing. Select options on the sidebar to filter Pokemon. Fill out the key roles for your team at the bottom.")
st.dataframe(df.style.apply(highlight_color1, subset=['type1'])\
             .apply(highlight_color2, subset=['type2'])\
             .apply(highlight_text1, subset=['type1'])\
             .apply(highlight_text2, subset=['type2']), width=2000, height=500)

st.write("Fill out the key roles for your team below!")
st.subheader("Offensive Mons")
POKEMON_O = list(df_P['name'].unique())
MON_SELECT_O = st.multiselect('Pokemon', POKEMON_O, key=2)
mask_mon_O = df_P['name'].isin(MON_SELECT_O)
df_O = df_P[mask_mon_O]
g = df_O['code1']
h = df_O['code2']
j = df_O['font1']
k = df_O['font2']
st.dataframe(df_O.style.apply(highlight_color1, subset=['type1'])\
             .apply(highlight_color2, subset=['type2'])\
             .apply(highlight_text1, subset=['type1'])\
             .apply(highlight_text2, subset=['type2']), width=2000, height=800)

st.subheader("Defensive Mons")
POKEMON_D = list(df_P['name'].unique())
MON_SELECT_D = st.multiselect('Pokemon', POKEMON_D, key=3)
mask_mon_D = df_P['name'].isin(MON_SELECT_D)
df_D = df_P[mask_mon_D]
g = df_D['code1']
h = df_D['code2']
j = df_D['font1']
k = df_D['font2']
st.dataframe(df_D.style.apply(highlight_color1, subset=['type1'])\
             .apply(highlight_color2, subset=['type2'])\
             .apply(highlight_text1, subset=['type1'])\
             .apply(highlight_text2, subset=['type2']), width=2000, height=800)

st.subheader("Utility Mons")
POKEMON_U = list(df_P['name'].unique())
MON_SELECT_U = st.multiselect('Pokemon', POKEMON_U, key=4)
mask_mon_U = df_P['name'].isin(MON_SELECT_U)
df_U = df_P[mask_mon_U]
g = df_U['code1']
h = df_U['code2']
j = df_U['font1']
k = df_U['font2']
st.dataframe(df_U.style.apply(highlight_color1, subset=['type1'])\
             .apply(highlight_color2, subset=['type2'])\
             .apply(highlight_text1, subset=['type1'])\
             .apply(highlight_text2, subset=['type2']), width=2000, height=800)