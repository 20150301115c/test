import streamlit as st

# 设置页面标题
st.set_page_config(page_title="Hello Streamlit", page_icon=":sunglasses:")

# 打印中文问候语
st.write("你好，欢迎来到我们的Streamlit测试应用！")

# 打印英文问候语
st.write("Hello, welcome to our Streamlit test app!")

# 用text_input创建一个输入框，让用户输入他们的名字
name = st.text_input("请问你叫什么名字？(What is your name?): ")

# 判断用户是否输入了名字，并提供个性化的问候
if name:
    st.write(f"很高兴认识你，{name}！(Nice to meet you, {name}!)")
else:
    st.write("你没有输入名字。(You didn't enter a name.)")

# 你可以添加更多的交互式元素，图表，数据框等
