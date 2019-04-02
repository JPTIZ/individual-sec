import java.math.BigInteger;

public class Foo {
    public static void main(String... args) {
        var x = BigInteger.ONE;

        for (var i = 0; i < 100; i++) {
            x = x.multiply(new BigInteger(new byte[] {(byte)(i + 1)}));
        }

        System.out.println("Factorial of 100 is " + x);
    }
}