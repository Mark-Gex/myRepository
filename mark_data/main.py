import streamlit as st
import pandas as pd

st.write("## 早上好！")
st.image("./test_data/yang.png",width=400)

df = pd.DataFrame({
"学号":["01","02","03","04"],
"班级":["一班","二班","二班","三班"],
"成绩":["100","80","90","89"]
}
)
st.dataframe(df)