public class Calculadora{
  public static int soma (int a, int b){
    return a + b;
  }
  public static int subtração (int a, intb){
    return a - b;
  }
  public static int multiplicacao (int a, int b){
    return a * b;
  }
  public static int divisao (int a, int b){
    if (b == 0){
      throw new IllegalArgumentExcpetion("Divisão por zero não é permitida");
    }
    return a / b;
  }
}
