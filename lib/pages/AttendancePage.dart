import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:nfc_attendance/pages/HomePage.dart';
import 'package:nfc_attendance/widgets/AttendanceWidget.dart';

class AttendancePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey,
      appBar: AppBar(
        backgroundColor: Colors.grey,
        elevation: 0,
        title: Text('مسح بطاقة NFC', style: TextStyle(color: Colors.white)),
        centerTitle: true,
        actions: [
          GestureDetector(
            child: Text('رجوع', style: TextStyle(color: Colors.white)),
            onTap: () {
              Get.to(HomePage());
            },
          ),
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Attendance History',
              style: TextStyle(
                fontSize: 20,
              ),
            ),
            SizedBox(height: 16),
            AttendanceWidget(
              dateTime: DateTime.now().subtract(Duration(days: 1)),
              attendanceStatus: 'Present',
            ),
            SizedBox(height: 16),
            AttendanceWidget(
              dateTime: DateTime.now().subtract(Duration(days: 2)),
              attendanceStatus: 'Absent',
            ),
          ],
        ),
      ),
    );
  }
}
