import streamlit as st

# st.set_page_config()
st.write("heLLO")
message = st.chat_input("say something")
print(message)
#st.line_chart(np.random.randn(30, 3))
if message:
    st.write(f"user input was :{message} ")
print(type(message))
