def calculate_data(self):
        if student_data:
            if self.tableWidget.rowCount() == 0:
                QtWidgets.QMessageBox.warning(None, 'Calculate', 'No data to calculate.')
                return

            # Lấy tên lớp đang được chọn
            selected_class_name = self.label_class.text().split(": ")[1]

            # Tạo một danh sách các sinh viên thuộc lớp đã chọn
            selected_class_students = [student_id for student_id, student_info in student_data.items() if selected_class_name in student_info.get("Classes", [])]

            # Hiển thị hộp thoại cho người dùng để chọn liệu muốn sắp xếp điểm hay không
            reply = QtWidgets.QMessageBox.question(None, 'Sort Points', 'Do you want to sort points?', QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                # Hiển thị hộp thoại cho người dùng để chọn kiểu sắp xếp
                sort_options = ['Ascending', 'Descending']
                sort, ok = QtWidgets.QInputDialog.getItem(None, 'Sort Options', 'Choose sort order:', sort_options, 0, False)
                if ok and sort:
                    reverse = True if sort == 'Descending' else False
                    selected_class_students.sort(key=lambda student_id: student_data[student_id]['Classes'][selected_class_name]['AttendanceCount'], reverse=reverse)

            for row, student_id in enumerate(selected_class_students):
                student_info = student_data.get(student_id)
                if student_info:
                    # Lấy giá trị AttendanceCount từ dữ liệu của sinh viên
                    attendance_count = student_info.get("Classes", {}).get(selected_class_name, {}).get("AttendanceCount", 0)

                    # Tính điểm dựa trên AttendanceCount (ví dụ: 1 điểm cho mỗi lần điểm danh)
                    # Bạn có thể điều chỉnh công thức tính điểm theo nhu cầu của bạn
                    points = attendance_count
                    
                    # Tạo một QTableWidgetItem để hiển thị điểm
                    points_item = QtWidgets.QTableWidgetItem(str(points))
                    # Đặt điểm vào cột "Điểm" của hàng hiện tại
                    self.tableWidget.setItem(row, 6, points_item)
                    set_read_only_flags(self.tableWidget)

            # Hiển thị thông báo khi tính toán hoàn thành
            QtWidgets.QMessageBox.information(None, 'Calculate', 'Calculation completed successfully.')

        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a class.")



        def export_data(self):
            if student_data:
                file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx)")
                if file_path:
                    workbook = Workbook()
                    sheet = workbook.active
                    sheet.title = "Student Data"

                    # Ghi tiêu đề cột
                    for column in range(self.tableWidget.columnCount()):
                        sheet.cell(row=1, column=column + 1, value=self.tableWidget.horizontalHeaderItem(column).text())

                    # Ghi dữ liệu từ tableWidget vào file Excel
                    for row in range(self.tableWidget.rowCount()):
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item is not None:
                                sheet.cell(row=row + 2, column=column + 1, value=item.text())

                    try:
                        workbook.save(file_path)
                        QtWidgets.QMessageBox.information(None, 'Export', f'Data exported to {file_path} successfully.')
                    except Exception as e:
                        QtWidgets.QMessageBox.warning(None, 'Export', f'Error occurred while exporting data: {str(e)}')
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Please select a class.")
            
def set_read_only_flags(table_widget):
    for row in range(table_widget.rowCount()):
        for column in range(table_widget.columnCount()):
            item = table_widget.item(row, column)
            if item:
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)