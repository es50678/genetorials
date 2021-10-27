package main;

public class UserArgument {
  public static void main(String[] args) {
    String person = args.length > 0 ? args[0].toString() : "human";
    String s = String.format("Hi, %1$s. How are you?", person);
    System.out.println(s);
  }

  public static void test() {
    System.out.println("hello world");
  }
}
