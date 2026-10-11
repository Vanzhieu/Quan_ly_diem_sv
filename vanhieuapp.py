
# Quan_ly_diem_sv
import streamlit as st
st.set_page_config(page_title="QUẢN LÍ ĐIỂM SINH VIÊN")
import pandas as pd

# tạo bảng dữ liệu
du_lieu={"Ho_ten":["Hoàng","Khoa","Ngân","Yến","Trúc","Quỳnh","Tân","Hiếu","Phương","Phượng"],"Điểm_chuyên_cần":[9,8.5,7,9.5,6.5,7,8.5,9,6,8.5],"diem_gk":[9,7.5,6.5,9,6,7,8,8.5,5.5,8],"diem_ck":[8,8.5,6.8,9.2,6.2,7.5,7.8,8.8,5.8,8.3]}
df=pd.DataFrame(du_lieu)
# tính điểm tổng kết
df["Tong_ket"]=(0.2*df["Điểm_chuyên_cần"]+0.3*df["diem_gk"]+0.5*df["diem_ck"])
# xếp loại sinh viên
def xep_loai(diem):
  if diem >=8.5 :
    return " Gioi"
  elif diem >=7 :
    return " Khhá"
  elif diem >=5 :
    return " Trung binh"
  else:
    return " Yếu "
df["Xep_loại"]=df["Tong_ket"].apply(xep_loai)
# làm tròn điểm tổng kết
df["Tong_ket"]=df["Tong_ket"].round(2)
# In kết quả
print(df)
# Thống kê
print("-Điểm trung bình:",(df["Tong_ket"].mean().round(2)))
print("-Sv điểm tổng kết cao nhất",(df["Tong_ket"].max()))
print("-Sv điểm tổng kết thấp nhất",(df["Tong_ket"].min()))
print("-Số sinh viên đạt",(df["Tong_ket"]>=5).sum())






