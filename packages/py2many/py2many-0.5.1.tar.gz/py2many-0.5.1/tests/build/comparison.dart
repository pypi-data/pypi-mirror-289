// @dart=3.4
import 'package:sprintf/sprintf.dart';

compare_with_integer_variable() {
  int i = 0;
  int s = 1;
  var s;

  if (i) {
    s = 2;
  } else {
    s = 3;
  }
  assert(s == 3);
}

use_zero_for_comparison() {
  int i = 0;
  int s = 1;
  var s;

  if (0) {
    s = 2;
  } else {
    s = 3;
  }
  assert(s == 3);
}

main(List<String> argv) {
  compare_with_integer_variable();
  use_zero_for_comparison();
  print(sprintf("%s", ["OK"]));
}
