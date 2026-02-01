import java.util.Arrays;

public class ProcessarMatriz{
  public static int somaMatrizFor(int[][] matriz){
    int soma = 0;
    for (int[] linha : matriz){
      for (int elemento : linha){
        soma += elemento;
      }
    }
    return soma;
  }

  public static int somaMatrizSimple(int[][] matriz){
    return Arrays.stream(matriz)
      .flatMapToInt(Arrays::stream)
      .sum();
  }
}
