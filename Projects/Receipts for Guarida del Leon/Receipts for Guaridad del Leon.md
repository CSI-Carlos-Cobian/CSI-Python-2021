<div style="text-align:center">
        <img    src="https://pbs.twimg.com/media/DHM9sZbXoAACVIY?format=jpg&name=4096x4096"
                title="Python" 
                width="60%" 
                height="40%" />
</div>
<br>

# Receipts for Guarida del León
With your knowledge of programming, we're going to build a script to help speed up the process of creating receipts for students that shop at Guarida del León. 

In this project, you will be storing names and prices of the Guarida del León catalog n variables.  You will process the total price and item list of customers, printing them to the output terminal. 

## Let's start. 

1. Create a Python script name Receipts-Guarida-Leon.py.
2. Add the first item, the best sale, the hoodie.  Create a variable called `lion_hoodie_description` and assign to it the following string: 
>Black soft hoodie. 50% cotton and 50% polyester.
3. After that, create a price for the hoodie. Create a variable `lion_hoodie_price` and set it equal to 45.00
4. Extend the inventory with 3 more items available in Guarida del León. Create a variable and assign to it a string with the item's description.  After that, create a variable and set it equal to its sale price.  You should have 4 variables with item's description and 4 variables with item's sale price. 
5. You should also calculate the sales tax and set it equal to `.115` . That is 11.5%. Name it `sales_tax`.
6. Your first customer or student is making its purchase!  You should keep a running tally of his expenses by defining a variable called `student_one_total`. Since student one hasn't purchased anything yet, set that variable equals to `0` for now. 
7. You should also keep a list of the descriptions of things that student is purchasing.  Create a variable called `student_one_items` and set that equal to the empty string "".  You'll tack on the description to this as he shop. 
8. When the student is ready to check out, you should calculate sales tax.  Create a variable called `student_one_tax` and set it equal to `student_one_total` times `sales_tax`. 
9. Add the `sales_tax` to the `student_one_total`. 
10. In the receipt, you should print out the heading or phrase `Student One Items:`. Print `student_one_items`. 
11. Now add a heading for total cost. Print out `Student One Total`. Now print his total. 
12. Repeat the steps to add the purchase for student two. 



<br>

### Example output:
<br>

```python
Student One:

Items: Black soft hoodie. 50% cotton and 50% polyester. New Balance Backpack. From gym clothes and school supplies to personal electronics, the CSI Backpack can accommodate everything you need to keep up with your on-the-go lifestyle.

Student One Total:
$105.925  
```

## Rubric

| Criteria | Points | 
|-----------|--------|
|The script includes the following variables: item descriptions, item prices, sale tax, students items, student totals ant student taxes.| <p style="text-align: center" >`25 points`</p>|
|When compiled and run, the program outputs a receipt with a detailed descriptions of the item purchased by Student One and the sale total in the Python console.| <p style="text-align: center" >`5 points`</p>|
|When compiled and run, the program outputs a receipt with a detailed descriptions of the item purchased by Student Two and the sale total in the Python console.| <p style="text-align: center" >`5 points`</p>|
| Name the file using the Receipts-Guarida-Leon.py |<p style="text-align: center" >`2 points`</p> |
| Take a screenshot of your terminal's output. Save it in the Project directory. Name the file using the following convention: `CSI-Jose-Quintana-Receipts-Guarida.png` | <p style="text-align: center" >`3 points`</p> |
|Total:|<p style="text-align: center" >`40 points`|

