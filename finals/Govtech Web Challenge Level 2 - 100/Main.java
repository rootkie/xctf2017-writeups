
import java.security.MessageDigest;
import java.util.Random;


public class Main {
   public static String flag1 = "flag1{7171a60f8cf4a789b7fa5906aa78f3e7}";

   public static void main(String[] var0) {
      march_on(flag1);
   }
   public static String md5(String var0) {
      MessageDigest var1 = null;

      try {
         var1 = MessageDigest.getInstance("MD5");
      } catch (Exception var8) {
         var8.printStackTrace(System.out);
      }

      var1.update(var0.getBytes());
      byte[] var2 = var1.digest();
      StringBuffer var3 = new StringBuffer();
      byte[] var4 = var2;
      int var5 = var2.length;

      for(int var6 = 0; var6 < var5; ++var6) {
         byte var7 = var4[var6];
         var3.append(String.format("%02x", var7 & 255));
      }

      return var3.toString();
   }

   public static void march_on(String var0) {
    String var2 = "00000";
    for(int var12 = 0; var12 < 100000000; ++var12) {
    var0 = md5(var0 + var12);
    if (var0.startsWith(var2)) {
        System.out.println("flag2{" + var0 + "}");
        return;
    }
   }
  }
}
