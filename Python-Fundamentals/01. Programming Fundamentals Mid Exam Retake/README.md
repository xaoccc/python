# Problem 1 - Computer Store

Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt.
The taxes are 20% of each part's price you receive.

If the customer is special, he has a 10% discount on the total price with taxes.

If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.

If the total price is equal to zero, you should print "Invalid order!" on the console.

### Input

•	You will receive numbers representing prices (without tax) until command "special" or "regular":

### Output

•	The receipt should be in the following format: 

"Congratulations you've just bought a new computer!

Price without taxes: {total price without taxes}$

Taxes: {total amount of taxes}$

-----------

Total price: {total price with taxes}$"

Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!

### Examples

<table style="width:516.0pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 112pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 404pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 112pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1050</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">200</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">450</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">2</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">18.50&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">16.86&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">special</span></p>
            </td>
            <td style="width: 404pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Congratulations you&apos;ve just bought a new computer!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Price without taxes: 1737.36$</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Taxes: 347.47$</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">-----------</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Total price: 1876.35$</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 516pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Comment</strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 516pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>1050 &ndash; valid price, total 1050</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>200 &ndash; valid price, total 1250</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>&hellip;</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>16.86 &ndash; valid price, total 1737.36</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>We receive&nbsp;<strong><span style="font-family:Consolas;">special</span></strong></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Price is positive number, so it is valid order&nbsp;</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Price without taxes is 1737.36</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Taxes: 20% from 1737.36 = 347.47</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Final price = 1737.36 + 347.47 = 2084.83</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Additional 10% discount for special customers</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>2084.83 &ndash; 10% = 1876.35&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 112pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 404pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 112pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1023&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">15</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:yellow;">-20</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:yellow;">-5.50</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">450</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">20&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">17.66&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">19.30</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">regular</span></p>
            </td>
            <td style="width: 404pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:yellow;">Invalid price!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:yellow;">Invalid price!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Congratulations you&apos;ve just bought a new computer!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Price without taxes: 1544.96$</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Taxes: 308.99$</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">-----------</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Total price: 1853.95$</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 112pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">regular</span></p>
            </td>
            <td style="width: 404pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">Invalid order!</span></p>
            </td>
        </tr>
    </tbody>
</table>

# Problem 2 - The Lift

Write a program that finds a place for the tourist on a lift. 

Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one with space available.
Input

•	On the first line, you will receive how many people are waiting to get on the lift

•	On the second line, you will receive the current state of the lift separated by a single space: " ".

### Output

When there is no more available space left on the lift, or there are no more people in the queue, you should print on the console the final state of the lift's wagons separated by " " and one of the following messages:

•	If there are no more people and the lift have empty spots, you should print:

"The lift has empty spots!

{wagons separated by ' '}"

•	If there are still people in the queue and no more available space, you should print:

"There isn't enough space! {people} people in a queue!

{wagons separated by ' '}"

•	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

### Examples

<table style="width:523.1pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 204.15pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 318.95pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 204.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">15</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">0 0 0 0</span></p>
            </td>
            <td style="width: 318.95pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">The lift has empty spots!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">4 4 4 3</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 523.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Comment</strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 523.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>First state -&nbsp;4 0 0 0&nbsp;-&gt; 11 people left</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Second state &ndash; 4 4 0 0 -&gt; 7 people left</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Third state&nbsp;&ndash; 4 4 4 0 -&gt; 3&nbsp;people&nbsp;left</p>
            </td>
        </tr>
        <tr>
            <td style="width: 204.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 318.95pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 204.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">20</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">0</span><span style="font-family:Consolas;">&nbsp;</span><span style="font-family:Consolas;">2</span><span style="font-family:Consolas;">&nbsp;</span><span style="font-family:Consolas;">0</span></p>
            </td>
            <td style="width: 318.95pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">There isn&apos;t enough space! 10 people in a queue!</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">4 4 4</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 523.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Comment</strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 523.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>First state -&nbsp;4&nbsp;2&nbsp;0&nbsp;&nbsp;-&gt; 16 people left</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Second state &ndash; 4 4 0 &nbsp;-&gt;&nbsp;14&nbsp;people left</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Third state &ndash; 4 4 4 -&gt; 10 people left, but there&apos;re no more wagons.</p>
            </td>
        </tr>
    </tbody>
</table>
