import streamlit as st

st.title('website của tôi!')

st.write("Tại đây bạn sẽ có thể thấy mặt trời mọc ở trên đầu bạn nơi này chính là 'Quả Đất'")


a = st.text_input("Bạn tên là gì ?")
b = st.text_input("Bạn bạn bao nhiêu tuổi ?")
gift = ["'NY'", "'Em gái nuôi'", "'Mô hình Doraemon màu hồng'"]
if st.button('Nhấn vào đây'):
    if int(b) < 10:
        st.write(f"Chúc mừng {a} nhận được {gift[0]}")
    elif int(b) > 18:
        st.write(f"Chúc mừng {a} nhận được {gift[1]}")
    elif int(b) >= 10 and int(b) <= 18:
        st.write(f"Chúc mừng {a} nhận được {gift[2]}")