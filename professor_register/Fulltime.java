package oop6;
import java.util.Scanner;
public class Fulltimeostad extends Ostad{
	protected int n=tedad();
	private double code[]=new double[n];
	
	
	public int tedad () {
		Scanner input=new Scanner (System.in);
		System.out.println("tedad ostad tamam vaght");
		int n=input.nextInt();
		return n;
	}
	public Fulltimeostad() {}
	public Fulltimeostad(double[] code) {
		setCode(code);
	}
	public void setCode(double[]code) {
		Scanner input=new Scanner(System.in);
		this.code=code;
		for (int i=0;i<n;i++) {
			if (code[i]<10000) {
				System.out.println("code "+super.getName()[i]+" is wrong try again");
				code[i]=input.nextDouble();
				setCode(code);
			}
		}
	}
	public double[] getCode() {
		return code;
	}
	public void readAll() {
		Scanner input=new Scanner(System.in);
		System.out.println("TAMAM VAGHT::::");
		super.readAll();
		for (int i=0;i<n;i++) {
			System.out.println("code"+super.getName()[i]+":");
			code[i]=input.nextDouble();
		}
	}
	public void printAll() {
		for(int i=0;i<n;i++) {
			System.out.println(super.getName()[i]);
			System.out.println("code"+code[i]);
		}
		
	}
	
}
