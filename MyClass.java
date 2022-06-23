import java.util.*;

public class MyClass
{
  public static void main(String args[])
  {
    Scanner s = new Scanner(System.in);
    
    String str = s.nextLine();
    String res="";
    int k=0;
    
    for(int i=0; i<str.length();i++)
    {
      if(i%2==0)
      {
        System.out.print(str.charAt(i));
      }
    }
  }
}
