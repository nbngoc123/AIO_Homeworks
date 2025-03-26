import streamlit as st

st.title("Ứng dụng quản lý công việc")

task_name = st.text_input("Tên công việc")
priority = st.slider("Mức độ ưu tiên", 1, 5, 3)
status = st.selectbox("Trạng thái công việc", ["Chưa làm", "Đang làm", "Hoàn thành"])

if st.button("Thêm công việc"):
    st.write(f"Tên: {task_name}, Ưu tiên: {priority}, Trạng thái: {status}")

if st.button("Xóa danh sách"):
    st.write("Danh sách đã được xóa")
