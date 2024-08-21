package oop6;
import java.util.Scanner;
public class Haghtadrisostad extends Ostad{
	protected int n=tedad();
	private double payment[]=new double[n];
	private double karkard[]=new double[n];
	
	public int tedad () {
		Scanner input=new Scanner (System.in);
		System.out.println("tedad ostad hagh tadris:");
		int n=input.nextInt();
		return n;
	}
	public  Haghtadrisostad () {}
	public Haghtadrisostad(double[] payment,double[] karkard) {
		setPayment(payment);
		setKarkard(karkard);
	}
	
	public double[] getPayment() {
		return payment;
	}
	public void setPayment(double[] payment) {
		this.payment = payment;
		Scanner input=new Scanner(System.in);
		for(int i=0;i<n;i++) {
			if (payment[i]<6000000) {
			System.out.println("payment "+super.getName()[i]+" is wrong try again");
			payment[i]=input.nextDouble();
			setPayment(payment);}
		}
	}
	public double[] getKarkard() {
		return karkard;
	}
	public void setKarkard(double[] karkard) {
		Scanner input=new Scanner(System.in);
		this.karkard = karkard;
		for(int i=0;i<n;i++) {
			if (karkard[i]>31*24) {
			System.out.println("karkard "+super.getName()[i]+" is wrong try again");
			karkard[i]=input.nextDouble();
			setKarkard(karkard);}
		}
	}
	public void readAll() {
		Scanner input=new Scanner(System.in);
		System.out.println("HAGH TADRIS::::");
		super.readAll();
		for(int i=0;i<n;i++) {
			System.out.println("payment"+super.getName()[i]+":");
			payment[i]=input.nextDouble();
		}
		setPayment(payment);
		for(int i=0;i<n;i++) {
			System.out.println("karkard"+super.getName()[i]+":");
			karkard[i]=input.nextDouble();
		}
		setKarkard(karkard);
	}
	public void printAll() {
		for(int i=0;i<n;i++) {
			System.out.println(super.getName()[i]);
			System.out.println("payment"+payment[i]);
			System.out.println("karkard"+karkard[i]);
		}
		
	}
}
