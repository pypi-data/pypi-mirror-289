 main(List<String> argv) {
final List<int> a = [1, 2];
final int b = (a[0..1] ?? (throw Exception("key not found")));}


