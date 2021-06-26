package com.limeguru;

@FunctionalInterface
interface Order {
	public void status(int orderid, String status);
}

public class CustomLambdaExpression {

	public static void main(String[] args) {

		Order myorder = ((orderid, status) -> {
			System.out.println("Your Order is " + status + " Order Id: "+ orderid);
		});
		
		int orderid = 123;
		myorder.status(orderid, "DELIVERED");
	}

}
