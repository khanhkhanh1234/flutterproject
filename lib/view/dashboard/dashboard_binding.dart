import 'package:fluterproject/controller/home_controller.dart';
import 'package:get/get.dart';

import '../../controller/dashboard_controller.dart';
class DashboardBinding extends Bindings{
  @override
  void dependencies() {
      Get.put(DashboardController());
      Get.put(HomeController());
  }

}