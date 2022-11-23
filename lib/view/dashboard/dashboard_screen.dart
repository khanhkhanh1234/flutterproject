import 'package:fluterproject/view/home/home_screen.dart';
import 'package:fluterproject/view/product/product_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_snake_navigationbar/flutter_snake_navigationbar.dart';
import 'package:get/get.dart';

import '../../controller/dashboard_controller.dart';
class DashboardScreen extends StatelessWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GetBuilder<DashboardController>(
      builder: (controller) => Scaffold(
        body: SafeArea(
            child: IndexedStack(
                index: controller.tabIndex,
                children:[
                  const HomeScreen(),
                  const ProductScreen(),
                  Container(
                    color: Colors.blue,
                  ),
                  Container(
                    color: Colors.orange,
                  ),
                ]
            )
        ),
        bottomNavigationBar: Container(
          decoration: BoxDecoration(
              color: Colors.white,
              border: Border(
                  top: BorderSide(
                      color: Theme.of(context).colorScheme.secondary,
                      width: 1
                  )
              )
          ),
          child: SnakeNavigationBar.color(
            behaviour: SnakeBarBehaviour.floating,
            snakeShape: SnakeShape.circle,
            padding: const EdgeInsets.symmetric(vertical: 5),
            unselectedLabelStyle: const TextStyle(fontSize: 11),
            snakeViewColor: Theme.of(context).colorScheme.secondary,
            showUnselectedLabels: true,
            currentIndex: controller.tabIndex,
            onTap: (val) {
            controller.updateIndex(val);
            },
            items: const [
              BottomNavigationBarItem(icon: Icon(Icons.home), label: 'home'),
              BottomNavigationBarItem(icon: Icon(Icons.category), label: 'category'),
              BottomNavigationBarItem(icon: Icon(Icons.menu), label: 'menu'),
              BottomNavigationBarItem(icon: Icon(Icons.account_circle), label: 'account')
            ],
          ),
        ),
      ),
    );
  }
}
