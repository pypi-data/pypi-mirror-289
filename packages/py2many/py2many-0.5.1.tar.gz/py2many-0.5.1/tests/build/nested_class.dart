class Foo {


 class Inner {


 int f1() {
return f2();}


int f2() {
return 20;}


}

}

 main() {
Foo.Inner().f1();}


