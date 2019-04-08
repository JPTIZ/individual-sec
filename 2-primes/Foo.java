import java.math.BigInteger;

public class Foo {
    public static void main(String... args) {
        var start = System.currentTimeMillis();

        var x = BigInteger.ONE;

        for (var i = 0; i < 100; i++) {
            x = x.multiply(new BigInteger(new byte[] {(byte)(i + 1)}));
        }

        var end = System.currentTimeMillis();

        System.out.println("Factorial of 100 is " + x);
        System.out.println("(" + (end - start) + "ms)");
    }
}
