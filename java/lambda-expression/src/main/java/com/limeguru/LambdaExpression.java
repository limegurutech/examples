package com.limeguru;

import java.util.ArrayList;
import java.util.List;

public class LambdaExpression {

	public static void main(String[] args) {

		List<String> orders = new ArrayList();
		orders.add("101");
		orders.add("102");
		orders.add("103");

		orders.forEach((order) -> {
			System.out.println(order);
		});
	}

}
