self.ui.ID2.setText(_translate("FaceRecognition", key))
                                        self.ui.Name.setText(_translate("FaceRecognition", studentName))
                                        self.ui.Role.setText(_translate("FaceRecognition", studentInfo["Faculty"]))
                                        self.ui.Class.setText(_translate("FaceRecognition", selected_class))   
                                        self.update_student_card_image(key)

                                        ## Ghi chú điểm danh
                                        res = db.reference(f"Students/{key}/Classes/{selected_class}")
                                        count = res.child("AttendanceCount").get()
                                        res.update({"AttendanceCount": count+1,
                                                "Datetime": date})