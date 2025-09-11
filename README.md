\# Dự án: Dự đoán sinh viên bỏ học 🎓



\# Thành viên của nhóm gồm 

&nbsp;1.Nguyễn Quang Thanh-Mã Sv: 683160

&nbsp;2.Nguyễn Duy Tuấn Việt-Mã Sv: 688709

&nbsp;3.Tạ Văn Hải-Mã Sv: 687599

&nbsp;

\## Giới thiệu về đề tài

Đây là dự án khoa học dữ liệu, sử dụng bộ dữ liệu \*\*Predict Students’ Dropout and Academic Success\*\* từ UCI Machine Learning Repository.  

Mục tiêu: Xây dựng mô hình dự đoán khả năng sinh viên \*\*bỏ học, tiếp tục học, hoặc tốt nghiệp\*\* dựa trên các thông tin nhân khẩu học và học tập.



\## Dataset

\- \*\*Tên dataset\*\*: Predict Students’ Dropout and Academic Success  

\- \*\*Nguồn\*\*: UCI Machine Learning Repository  

\- \*\*Số lượng mẫu\*\*: ~4424 sinh viên  

\- \*\*Số thuộc tính\*\*: 36 (bao gồm thông tin nhân khẩu học, học tập, hoàn cảnh xã hội)  

\- \*\*Nhãn phân loại\*\*: 

&nbsp; - `Dropout` → Bỏ học  

&nbsp; - `Enrolled` → Tiếp tục học  

&nbsp; - `Graduate` → Tốt nghiệp  



🔗 Link tải dataset: \[UCI - Predict Students’ Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict%2Bstudents%2Bdropout%2Band%2Bacademic%2Bsuccess)



\## Cấu trúc thư mục

\- `data/` : chứa dữ liệu (student\_dropout.csv).  

\- `notebooks/` : chứa các notebook Jupyter để phân tích và huấn luyện mô hình.  

\- `output/` : chứa file kết quả dự đoán (nếu có).  

\- `requirements.txt` : danh sách thư viện cần cài đặt.  



\## Cách chạy dự án

1\. Cài đặt các thư viện cần thiết:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

2\. Mở notebook trong thư mục notebooks/:



jupyter notebook



3.Tải dataset từ link ở trên và đặt file .csv vào thư mục data/.

