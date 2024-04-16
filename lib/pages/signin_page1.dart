import 'package:flutter/material.dart';

class signin_page1 extends StatelessWidget {
  signin_page1({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/images/img_2_2x_8_1.png',
              width: 200,
              height: 500,
            ),
            Text(
              "تسجيل الدخول",
              style: TextStyle(
                color: Colors.blueGrey,
                fontSize: 25,
              ),
            ),
            SizedBox(height: 20),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 50.0),
              child: Column(
                children: [
                  ElevatedButton(
                    onPressed: () {
                      print('Login button pressed');
                    },
                    child: Text(
                      'الطلاب',
                      style: TextStyle(
                        fontSize: 20,
                      ),
                    ),
                    style: ElevatedButton.styleFrom(
                        // Set the buttons' size
                        ),
                  ),
                  SizedBox(height: 10),
                  ElevatedButton(
                    onPressed: () {
                      print('Register button pressed');
                    },
                    child: Text(
                      'اعضاء هيئة التدريس',
                      style: TextStyle(
                        fontSize: 20,
                      ),
                    ),
                    style: ElevatedButton.styleFrom(),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
