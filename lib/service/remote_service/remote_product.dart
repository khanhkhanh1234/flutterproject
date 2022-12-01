import 'package:http/http.dart' as http;

import 'package:fluterproject/const.dart';

class RemoteProductService {
  var client = http.Client();
  var remoteUrl = '$baseUrl/api/products';

  Future<dynamic> get() async {
    var response = await client.get(
        Uri.parse('$remoteUrl?populate=images,tags')
    );
    return response;
  }
  Future<dynamic> getByName({required String keyword}) async{
    var response = await client.get(
      Uri.parse('$remoteUrl?populate=images,tags&filters[name][\$contains]=$keyword')
    );
    return response;
  }
}