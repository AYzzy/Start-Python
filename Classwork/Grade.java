import java.util.Scanner;

public class Grade{
public static void main(String[] args){

Scanner input = new Scanner(System.in);

System.out.print("Enter score: ");
int number = input.nextInt();

switch(number/10){
	case 8:
		System.out.print("A");
		break;
	case 7:
		System.out.print("B");
		break;
	case 6:
		System.out.print("C");
		break;
	case 5:
		System.out.print("D");
		break;
	case 4:
		System.out.print("E");
		break;
	case 3:
		System.out.print("F");
		break;
}

int numb = -5%1;
System.out.println(numb);

}

}