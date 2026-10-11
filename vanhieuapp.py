import streamlit as st
import pandas as pd

# Cau hinh trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide")

# Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write("Ứng dụng quản lý điểm và thống kê kết quả học tập.")

# Du lieu minh hoa cua 10 sinh vien
du_lieu = {
    "Họ tên": [
        "Hoàng", "Khoa", "Ngân", "Yến", "Trúc",
        "Quỳnh", "Tân", "Hiếu", "Phương", "Phượng"
    ],
    "Chuyên cần": [9, 8, 10, 7, 8, 9, 6, 8, 9, 7],
    "Giữa kỳ":    [8, 7, 9, 6, 8, 7, 5, 8, 9, 6],
    "Cuối kỳ":    [9, 8, 10, 7, 9, 8, 6, 7, 10, 8]
}

df = pd.DataFrame(du_lieu)

# Tinh diem tong ket theo trong so
# Chuyen can 20%, giua ky 30%, cuoi ky 50%
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# Xep loai
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 1. Hien thi bang diem
st.subheader("1. Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# 2. Thong ke tong quan
st.subheader("2. Thống kê kết quả học tập")

diem_tb = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = (df["Tổng kết"] >= 5).sum()

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
cot2.metric("Điểm cao nhất", f"{sv_cao_nhat['Tổng kết']:.2f}")
cot3.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tổng kết']:.2f}")
cot4.metric("Số sinh viên đạt", f"{so_sv_dat}/10")

st.write(
    f"**Sinh viên cao nhất:** {sv_cao_nhat['Họ tên']}"
)
st.write(
    f"**Sinh viên thấp nhất:** {sv_thap_nhat['Họ tên']}"
)

# 3. Chon sinh vien bang Selectbox
st.subheader("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Họ tên"].tolist()
)

sv = df[df["Họ tên"] == ten_sv].iloc[0]

a, b, c, d, e = st.columns(5)
a.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
b.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")
d.metric("Tổng kết", f"{sv['Tổng kết']:.2f}")
e.metric("Xếp loại", sv["Xếp loại"])

# 4. Bieu do cot diem tong ket
st.subheader("4. Biểu đồ điểm tổng kết")

bieudo = df.set_index("Họ tên")[["Tổng kết"]]
st.bar_chart(bieudo, y_label="Điểm tổng kết")

# 5. Thong tin nguoi tao
st.divider()
st.caption("Người tạo ứng dụng: Trần Văn Hiếu | MSSV: "051208002451")





