import 'package:get/get_navigation/get_navigation.dart';
import '../view/dashboard/dashboard_binding.dart';
import '../view/dashboard/dashboard_screen.dart';

import 'app_route.dart';

class AppPage {
  static var list = [
    GetPage(
        name: AppRoute.dashboard,
        page: () => const DashboardScreen(),
        binding: DashboardBinding()
    )
  ];

}