import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;

public class XCTF extends URLClassLoader {
   public static void main(String[] var0) throws Exception {
      XCTF var1 = new XCTF(XCTF.class.getClassLoader(), new File("."));
      Thread.currentThread().setContextClassLoader(var1);
      Class var2 = var1.loadClass("Main");
      Method var3 = var2.getMethod("main", String[].class);
      String[] var4 = new String[0];
      var3.invoke((Object)null, var4);
   }

   public Class loadClass(String var1, boolean var2) throws ClassNotFoundException {
      Class var3 = null;
      var3 = this.findLoadedClass(var1);
      if (var3 == null) {
         Class var4 = null;

         try {
            var4 = this.getParent().loadClass(var1);
            if (var4.getClassLoader() != this.getParent()) {
               var3 = var4;
            }
         } catch (ClassNotFoundException var7) {
            ;
         } catch (ClassFormatError var8) {
            ;
         }

         if (var3 == null) {
            try {
               var3 = this.findClass(var1);
            } catch (ClassNotFoundException var6) {
               var3 = var4;
            }
         }
      }

      if (var3 == null) {
         throw new ClassNotFoundException(var1);
      } else {
         if (var2) {
            this.resolveClass(var3);
         }

         return var3;
      }
   }

   protected Class findClass(String var1) throws ClassNotFoundException {
      String var2 = var1.replace('.', '/') + ".class";
      URL var3 = this.getResource(var2);
      if (var3 == null) {
         throw new ClassNotFoundException(var1);
      } else {
         InputStream var4 = null;

         Class var6;
         try {
            var4 = var3.openStream();
            byte[] var5 = readFully(var4);
            crypt(var5);
            var6 = this.defineClass(var1, var5, 0, var5.length);
         } catch (IOException var15) {
            throw new ClassNotFoundException(var1);
         } finally {
            if (var4 != null) {
               try {
                  var4.close();
               } catch (Exception var14) {
                  ;
               }
            }

         }

         return var6;
      }
   }

   private XCTF(ClassLoader var1, File var2) throws MalformedURLException {
      super(new URL[]{var2.toURL()}, var1);
      if (var1 == null) {
         throw new IllegalArgumentException("XCTF requires a non-null delegation parent");
      }
   }

   private static void crypt(byte[] var0) {
      char[] var1 = new char[257];
      char[] var2 = new char[257];
      String var6 = "nomorepptplease!";
      boolean var8 = false;
      boolean var5 = false;
      boolean var7 = false;

      int var3;
      for(var3 = 0; var3 < 256; ++var3) {
         var1[var3] = (char)var3;
      }

      var3 = 0;

      int var4;
      for(var4 = 0; var3 < 256; ++var3) {
         if (var4 == var6.length()) {
            var4 = 0;
         }

         var2[var3] = var6.charAt(var4++);
      }

      var4 = 0;

      char var13;
      for(var3 = 0; var3 < 256; ++var3) {
         var4 = (var4 + var1[var3] + var2[var3]) % 256;
         var13 = var1[var3];
         var1[var3] = var1[var4];
         var1[var4] = (char)var13;
      }

      char var10 = 0;
      char var12 = 0;

      for(int var9 = 0; var9 < var0.length; ++var9) {
         var10 = (char)((var10 + 1) % 256);
         var12 = (char)((var12 + var1[var10]) % 256);
         var13 = var1[var10];
         var1[var10] = var1[var12];
         var1[var12] = (char)var13;
         int var11 = (var1[var10] + var1[var12]) % 256;
         char var14 = var1[var11];
         var0[var9] = (byte)(var0[var9] ^ var14);
      }

   }

   private static byte[] readFully(InputStream var0) throws IOException {
      ByteArrayOutputStream var1 = new ByteArrayOutputStream();
      byte[] var2 = new byte[8192];

      int var3;
      while((var3 = var0.read(var2)) > 0) {
         var1.write(var2, 0, var3);
      }

      return var1.toByteArray();
   }
}
