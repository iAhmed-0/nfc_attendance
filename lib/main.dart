import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:nfc_attendance/pages/HomePage.dart';
import 'package:nfc_attendance/pages/NFCReaderPage.dart';

void main() {
  runApp(GetMaterialApp(
    home: NFCReaderPage(),
  ));
}
