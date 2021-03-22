<?php
//http://localhost//it135-8l/le2_ambataj/checkout.html
echo "<link rel='stylesheet' type='text/css' href='LE2_CSS.css' />";
echo "<head> <meta charset='utf-8' /> </head>";
echo "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>";

	//personal information
	$input_name =  $_POST['user_name'];
	$input_contact =  $_POST['contact_number'];
	$input_address =  $_POST['address'];
	
	//select products
	$input_product_name = $_POST['medical_drug_name'];
	$input_product_price = $_POST['medical_drug_price'];
	$input_product_quantity = $_POST['medical_drug_quantity'];
	
	//payment information
	$input_privilege = $_POST['privilege'];
	$input_payment = $_POST['payment'];
	
	class Customer{
		private $customer_name;
		private $customer_contact;
		private $customer_address;
		private $customer_privilege;
		private $customer_payment;
		
		function __construct($customer_name, $customer_contact, $customer_address, $customer_privilege, $customer_payment){
			$this->customer_name = $customer_name;
			$this->customer_contact = $customer_contact;
			$this->customer_address = $customer_address;
			$this->customer_privilege = $customer_privilege;
			$this->customer_payment = $customer_payment;
		}
		
		function getName(){
			return $this->customer_name;
		}
		
		function getContact(){
			return $this->customer_contact;
		}
		
		function getAddress(){
			return $this->customer_address;
		}
		
		function getPrivilege(){
			return $this->customer_privilege;
		}
		
		function getPayment(){
			return $this->customer_payment;
		}
	}
		
	class Product{
		private $product_name;
		private $product_price;
		private $product_quantity;
		
		function __construct($product_name, $product_price, $product_quantity){
			$this->product_name = $product_name;
			$this->product_price = $product_price;
			$this->product_quantity = $product_quantity;
		}
		
		function getProductName(){
			return $this->product_name;
		}
		
		function getProductPrice(){
			return $this->product_price;
		}
		
		function getProductQuantity(){
			return $this->product_quantity;
		}
	}
	
	//class 
	class Summary{
		private $selected_product;
		private $customer_details;
		
		function __construct($selected_products, $customer_details){
			$this->selected_products = $selected_products;
			$this->customer_details = $customer_details;
		}

		//Process
		
		function getTotalAmount(){//gets the total amount of the selected products
			$total_amount = 0;
			for($i=0 ; $i<count($this->selected_products) ; $i++){
				$total_amount = $total_amount + ($this->selected_products[$i]->getProductPrice() * $this->selected_products[$i]->getProductQuantity());
			}
			return $total_amount;
		}
		
		function getSelectedProducts(){//outputs the products selected
			$item_counter = 1;
			echo "<table class='table-php-items'>
			 <tr>
					 <th>Item Name</th>
					 <th>Price</th>
					 <th>Quantity</th>
			 	</tr>";
			
			for($j=0 ; $j<count($this->selected_products) ; $j++){
				if($this->selected_products[$j]->getProductQuantity()>0){
					echo "<tr>
						 <td>".$this->selected_products[$j]->getProductName()."</td>
						 <td>₱".number_format($this->selected_products[$j]->getProductPrice(), 2, '.', ',')."</td>
						 <td>".$this->selected_products[$j]->getProductQuantity()."</td>
						</tr>";
						$item_counter++;
				}
			}
			echo "</table>";
		}
		
		function getVAT($privilege){//gets the VAT
			$vat = 0;
			
			if($privilege=="Student"){
				$vat = 0.12;
			}
			elseif($privilege=="Senior" || $privilege=="PWD"){
				$vat = 0;
			}
			else{
				$vat = 0.12;
			}
			return $vat;
		}
		
		function getDiscount($privilege){//gets the discount percentage
			$discount = 0;
			
			if($privilege=="Student"){
				$discount = 0.10;
			}
			elseif($privilege=="Senior" || $privilege=="PWD"){
				$discount = 0.20;
			}
			return $discount;
		}

		function getOutput(){ //outputs the receipt or confirmation of order
			
			//Declarations
			$shipping_fee = 45;
			$exempt_vat = 0;
			$amount = 0;
			$discounted_amount = 0;
			$total_amount = 0;
			$vat_value = 0;
			$discount = 0;
			
			//Calculations
			$discount = $this->getDiscount($this->customer_details->getPrivilege());
			$amount = $this->getTotalAmount();
			$discounted_amount = ($amount - ($discount*$this->getTotalAmount())) ;
			$exempt_vat = $discounted_amount / (1 + $this->getVAT($this->customer_details->getPrivilege()));
			$vat_value = $discounted_amount - $exempt_vat;
			$total_amount = $discounted_amount + $shipping_fee;
			
			//Output Details
			echo "<div class='receipt-php'>
			 ===========================<br>
			 <table class='table-php-label'>
			 <tr>
			 <td>Name: </td>
			 <td>".$this->customer_details->getName()."</td>
			 </tr>
			 <tr>
			 <td>Contact Number: </td>
			 <td>".$this->customer_details->getContact()."</td>
			 </tr>
			 <tr>
			 <td>Address: </td>
			 <td>".$this->customer_details->getAddress()."</td>
			 </tr>
			 <tr>
			 <td>Privilege: </td>
			 <td>".$this->customer_details->getPrivilege()."</td>
			 </tr>
			 <tr>
			 <td>Mode of Payment: </td>
			 <td>".$this->customer_details->getPayment()."</td>
			 </tr>
			 </table>
			 ===========================<br>";
			 echo $this->getSelectedProducts();
			 echo "===========================<br>
			 <table class='table-php-label'>
			 <tr>
			 <td>Amount: </td>
			 <td>₱".number_format($amount, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <tr>
			 <td>Discount(".$this->customer_details->getPrivilege()."): </td>
			 <td>₱".number_format($discount, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <td>Discounted Amount: </td>
			 <td>₱".number_format($discounted_amount, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <td>Exempt VAT: </td>
			 <td>₱".number_format($exempt_vat, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <td>VAT(". round((float)$this->getVAT($this->customer_details->getPrivilege()) * 100 ) ."%): </td> 
			 <td>₱".number_format($vat_value, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <td>Shipping Fee: </td>
			 <td>₱".number_format($shipping_fee, 2, '.', ',')."</td>
			 </tr>
			 <tr>
			 <td>Total Amount: </td>
			 <td>₱".number_format($total_amount, 2, '.', ',')."</td>
			 </tr>
			 </table>
			 ===========================<br>
			 </div>
			 <div class='center-this'>
			 <form method='POST' action='checkout.html'><input class='submit_button_holder' type='submit' value='Return'/></form>
			 </div>";
		}			
	}
	
	$customer = new Customer($input_name, $input_contact, $input_address, $input_privilege, $input_payment);
	$list_of_products = array();
	
	array_push($list_of_products, new Product($input_product_name[0], $input_product_price[0], $input_product_quantity[0]));
	array_push($list_of_products, new Product($input_product_name[1], $input_product_price[1], $input_product_quantity[1]));
	array_push($list_of_products, new Product($input_product_name[2], $input_product_price[2], $input_product_quantity[2]));
	array_push($list_of_products, new Product($input_product_name[3], $input_product_price[3], $input_product_quantity[3]));
	array_push($list_of_products, new Product($input_product_name[4], $input_product_price[4], $input_product_quantity[4]));
	array_push($list_of_products, new Product($input_product_name[5], $input_product_price[5], $input_product_quantity[5]));
	array_push($list_of_products, new Product($input_product_name[6], $input_product_price[6], $input_product_quantity[6]));
	array_push($list_of_products, new Product($input_product_name[7], $input_product_price[7], $input_product_quantity[7]));
	array_push($list_of_products, new Product($input_product_name[8], $input_product_price[8], $input_product_quantity[8]));
	array_push($list_of_products, new Product($input_product_name[9], $input_product_price[9], $input_product_quantity[9]));
	
	$summary = new Summary($list_of_products,$customer);
	$summary->getOutput();
	
?>

