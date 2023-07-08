from doread import *
import streamlit as st

path = r"C:\Users\Navid\PycharmProjects\web_develpment\web_data.txt"
lest = reader()


def new_item():
    conditions = {}
    todo = st.session_state["new_todo"] + '\n'
    tool = False
    if len(todo) > 2:
        tool = True
    conditions['length']: tool
    duplicate = True
    for existing in lest:
        if existing == todo:
            duplicate = False
    conditions['duplicate']: duplicate
    if all(conditions.values()):
        lest.append(todo)
    writer(lest, path)


st.title('get your ass moving you useless piece of shit')
st.subheader('get your shit together doug')
st.write('you are a disappointment')
for index, i in enumerate(lest):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        lest.pop(index)
        writer(lest, path)
        del st.session_state[i]
        st.experimental_rerun()

new_todo = st.text_input('shit', placeholder='enter a problem that make you miserable',
                         key='new_todo', on_change=new_item)
print('activity')
st.session_state
