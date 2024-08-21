package oop6;

import java.util.Scanner;
public class Asli {

	public static void main(String[] args) {
		Scanner input=new Scanner (System.in);
		Ostad o=new Ostad();
		Haghtadrisostad ho=new Haghtadrisostad();
		Fulltimeostad fo=new Fulltimeostad();
		ho.readAll();
		fo.readAll();
		ho.printAll();
		fo.printAll();
	}

}
