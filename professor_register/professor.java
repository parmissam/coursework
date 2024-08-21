package oop6;
import java.util.Scanner;
public class Ostad {
	private int x=tedad();
	private String name[]=new String[x];
	
	public int tedad () {
		Scanner input=new Scanner (System.in);
		System.out.println("tedad KOL OSTAD:");
		int n=input.nextInt();
		return n;
	}	
	public Ostad() {}
	public Ostad(String[] name ) {
		setName(name);
		
	}
	public void setName(String name[]) {
		this.name=name;
	}
	public String[] getName() {
		return name;
	}
	public void printAll() {
		System.out.println("name:"+name);
	}
	public void readAll() {
		Scanner input=new Scanner (System.in);
		for (int i=0;i<x;i++) {
			System.out.println("name:");
			name[i]=input.next();}
		setName(name);
	}
}
