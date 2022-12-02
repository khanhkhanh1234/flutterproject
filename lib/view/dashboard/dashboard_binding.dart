import 'package:fluterproject/controller/home_controller.dart';
import 'package:fluterproject/controller/product_controller.dart';
import 'package:get/get.dart';

import '../../controller/category_controller.dart';
import '../../controller/dashboard_controller.dart';
class DashboardBinding extends Bindings{
  @override
  void dependencies() {
      Get.put(DashboardController());
      Get.put(HomeController());
      Get.put(ProductController());
      Get.put(CategoryController());

  }

}