# Ôn Tập Cuối Kỳ Khai Phá Dữ Liệu (KPDL) - Nguyễn Quang Thanh

# ======================
# PHẦN 1: LÝ THUYẾT CƠ BẢN
# ======================

# Câu 1: Khai phá dữ liệu là gì?
# A. Quá trình thu thập dữ liệu
# B. Quá trình tìm ra tri thức tiềm ẩn trong dữ liệu
# C. Quá trình làm sạch dữ liệu
# D. Phân tích thống kê mô tả
# => Đáp án: B
# Giải thích: Khai phá dữ liệu (Data Mining) là quá trình phát hiện các mẫu, mối quan hệ, hoặc tri thức hữu ích từ tập dữ liệu lớn.

# Câu 2: Quá trình KPDL gồm mấy giai đoạn chính?
# A. 3  B. 5  C. 7  D. 9
# => Đáp án: C
# Giải thích: Gồm 7 bước: Xác định mục tiêu → Thu thập dữ liệu → Tiền xử lý dữ liệu → Khai phá dữ liệu → Đánh giá → Triển khai → Giám sát.

# Câu 3: Phân biệt học có giám sát và không giám sát
# A. Có nhãn và không có nhãn dữ liệu
# => Đáp án: A
# Giải thích: Học có giám sát (Supervised Learning) dùng dữ liệu có nhãn (ví dụ phân lớp, hồi quy), còn học không giám sát (Unsupervised) không có nhãn (ví dụ phân cụm).

# Câu 4: Trong bài toán phân lớp, biến đầu ra (output) là loại biến gì?
# A. Định lượng  B. Định danh / phân loại
# => Đáp án: B
# Giải thích: Vì kết quả của phân lớp thường là các nhãn rời rạc như "Tốt / Xấu", "Có / Không".

# Câu 5: Trong bài toán hồi quy, biến đầu ra là loại biến gì?
# A. Liên tục (số thực)  B. Phân loại
# => Đáp án: A
# Giải thích: Hồi quy dự đoán giá trị thực như giá nhà, thu nhập, điểm số.

# ======================
# PHẦN 2: THUẬT TOÁN CƠ BẢN
# ======================

# Câu 6: KNN là viết tắt của?
# A. K-Nearest Neighbors
# => Đáp án: A
# Giải thích: KNN là thuật toán dựa trên khoảng cách giữa điểm mới và các điểm đã biết để phân lớp hoặc dự đoán.

# Câu 7: Trong KNN, nếu chọn K quá lớn sẽ gây ra điều gì?
# A. Mô hình bị nhiễu
# B. Mô hình bị đơn giản quá mức
# => Đáp án: B
# Giải thích: K quá lớn khiến mô hình coi trung bình nhiều điểm → giảm độ chính xác, khó phân biệt ranh giới giữa các lớp.

# Câu 8: Trong ID3, thuộc tính nào được chọn làm nút gốc?
# A. Thuộc tính có entropy nhỏ nhất (hoặc gain lớn nhất)
# => Đáp án: A
# Giải thích: ID3 chọn thuộc tính mang lại nhiều thông tin nhất (information gain cao nhất) để phân tách đầu tiên.

# Câu 9: Naive Bayes dựa trên nguyên lý gì?
# A. Xác suất có điều kiện và giả định độc lập giữa các thuộc tính
# => Đáp án: A
# Giải thích: Naive Bayes giả định các thuộc tính độc lập và tính xác suất hậu nghiệm theo định lý Bayes.

# Câu 10: Trong hồi quy tuyến tính, hàm dự đoán có dạng:
# A. y = a + bx
# => Đáp án: A
# Giải thích: Đây là mô hình đơn giản nhất (Linear Regression) mô tả mối quan hệ tuyến tính giữa biến độc lập x và phụ thuộc y.

# ======================
# PHẦN 3: KHAI PHÁ LUẬT KẾT HỢP (Apriori)
# ======================

# Câu 11: Support (độ hỗ trợ) biểu thị điều gì?
# A. Tần suất xuất hiện của tập mục trong toàn bộ giao dịch
# => Đáp án: A
# Giải thích: Support(X→Y) = số giao dịch chứa cả X và Y / tổng giao dịch.

# Câu 12: Confidence (độ tin cậy) biểu thị điều gì?
# A. Xác suất Y xảy ra khi X đã xảy ra
# => Đáp án: A
# Giải thích: Confidence(X→Y) = Support(XY) / Support(X).

# Câu 13: Thuật toán Apriori dùng để làm gì?
# A. Khai phá tập mục thường xuyên (Frequent Itemset)
# => Đáp án: A
# Giải thích: Apriori tìm các tập mục xuất hiện thường xuyên để sinh luật kết hợp.

# Câu 14: Liên hệ giữa Support và Confidence?
# => Đáp án: Support đo độ phổ biến của luật, Confidence đo độ mạnh của mối quan hệ.

# ======================
# PHẦN 4: PHÂN CỤM (CLUSTERING)
# ======================

# Câu 15: K-Means là thuật toán học có giám sát hay không giám sát?
# A. Không giám sát
# => Đáp án: A
# Giải thích: Vì K-Means không có nhãn đầu ra, chỉ nhóm các điểm dựa trên khoảng cách.

# Câu 16: Khoảng cách trong K-Means thường dùng là?
# A. Euclidean Distance
# => Đáp án: A
# Giải thích: Đây là khoảng cách phổ biến nhất để tính sự tương tự giữa các điểm dữ liệu.

# Câu 17: Khi K-Means hội tụ nghĩa là gì?
# A. Tâm cụm không thay đổi nữa
# => Đáp án: A
# Giải thích: Khi các điểm không đổi cụm và các tâm cụm ổn định, thuật toán kết thúc.

# ======================
# PHẦN 5: ĐÁNH GIÁ MÔ HÌNH
# ======================

# Câu 18: Độ chính xác (Accuracy) được tính bằng công thức nào?
# A. (TP + TN) / (TP + TN + FP + FN)
# => Đáp án: A

# Câu 19: Khi dữ liệu mất cân bằng (ví dụ 95% mẫu là 1 lớp), nên dùng chỉ số nào thay vì Accuracy?
# A. F1-Score hoặc Precision/Recall
# => Đáp án: A

# Câu 20: Trong hồi quy, chỉ số R^2 biểu diễn điều gì?
# A. Mức độ mô hình giải thích được phương sai của dữ liệu
# => Đáp án: A
# Giải thích: R^2 càng gần 1 thì mô hình càng phù hợp với dữ liệu.