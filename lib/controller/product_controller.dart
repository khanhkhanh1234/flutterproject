import 'package:fluterproject/service/remote_service/remote_product.dart';
import 'package:flutter/widgets.dart';
import 'package:get/get.dart';

import '../model/product.dart';

class ProductController extends GetxController {
  static ProductController instance = Get.find();
  TextEditingController searchTextEditController = TextEditingController();
  RxString searchVal = ''.obs;
  RxList<Product> productList = List<Product>.empty(growable: true).obs;
  RxBool isProductLoading = false.obs;

  @override
  void onInit() {
    getProducts();
    super.onInit();
  }

  void getProducts() async {
    try {
      isProductLoading(true);
      var result = await RemoteProductService().get();
      if(result != null) {
        productList.assignAll(productListFromJson(result.body));
      }
    } finally {
      isProductLoading(false);
      print(productList.length);
    }
  }
  void getProductByName({required String keyword}) async
  {
    try {
      isProductLoading(true);
      var result = await RemoteProductService().getByName(keyword: keyword);
      if(result != null){
        productList.assignAll(productListFromJson(result.body));
      }
    } finally{
  isProductLoading(false);
  print(productList.length);
    }
  }
}