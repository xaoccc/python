# Problem 1 - Black Flag 

Pirates are invading the sea, and you're tasked to help them plunder  
Create a program that checks if target plunder is reached. First, you will receive how many days the pirating lasts. Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.  
Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder. Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.  
If the gained plunder is more or equal to the target, print the following:  
**"Ahoy! {totalPlunder} plunder gained."**  
If the gained plunder is less than the target. Calculate the percentage left and print the following:   
**"Collected only {percentage}% of the plunder."**  
Both numbers should be formatted to the 2nd decimal place.
### Input
*	On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
*	On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
*	On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
### Output
•	 In the end, print whether the plunder was successful or not, following the format described above.
### Examples
<table style="width:515.65pt;margin-left:8.5pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 253.5pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong>Input</strong></p>
            </td>
            <td style="width: 262.15pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 253.5pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 20.65pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">5<br>40<br>100</span></p>
            </td>
            <td style="width: 262.15pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 20.65pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Ahoy! 154.00 plunder gained.</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 17.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Comments</strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 68.1pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'>The days are 5, and the daily plunder is 40. On the third day, the total plunder is 120, and since it is a third day, they gain an additional 50% from the daily plunder, which adds up to 140. On the fifth day, the plunder is 220, but they battle with a warship and lose 30% of the collected cargo, and the total becomes 154. That is more than expected.</p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 21.1pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 253.5pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 14.05pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">10</span>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">20</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">380</span></p>
            </td>
            <td style="width: 262.15pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 14.05pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Collected only 36.29% of the plunder.</span></p>
            </td>
        </tr>
    </tbody>
</table>

# Problem 2 - Treasure Hunt

The pirates need to carry a treasure chest safely back to the ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".  
"{loot1}|{loot2}|{loot3} … {lootn}"  
The following lines represent commands until "Yohoho!" which ends the treasure hunt:  
*	"Loot {item1} {item2}…{itemn}":
    *	Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
    *	If an item is already contained, don't insert it.
*	"Drop {index}":
    *	Remove the loot at the given position and add it at the end of the treasure chest. 
    *	If the index is invalid, skip the command.
*	"Steal {count}":
    *	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are. 
    *	Print the stolen items separated by ", ":  
"{item1}, {item2}, {item3} … {itemn}"  
In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."
### Input
*	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
*	On the following lines, until "Yohoho!", you will be receiving commands.
### Output
*	Print the output in the format described above.
### Constraints
*	The loot items will be strings containing any ASCII code.
*	The indexes will be integers in the range [-200…200]
•	The count will be an integer in the range [1….100]
### Examples
<table style="width:515.65pt;margin-left:8.5pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 198.25pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong>Input</strong></p>
            </td>
            <td style="width: 317.4pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 198.25pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 117.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Gold|Silver|Bronze|Medallion|Cup</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Loot Wood Gold Coins</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Loot Silver Pistol</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Drop 3</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Steal 3</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Yohoho!</span></p>
            </td>
            <td style="width: 317.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 117.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="line-height:150%;font-family:Consolas;">Medallion, Cup, Gold</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="line-height:150%;font-family:Consolas;">Average treasure gain: 5.40 pirate credits.</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 17.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Comments</strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 99.35pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:5.0pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>The first command&nbsp;<strong><span style="font-family:Consolas;">&quot;Loot Wood Gold Coins&quot;</span></strong> adds <strong>Wood</strong> and <strong>Coins</strong> to the chest but <strong>omits</strong> Gold since it is already contained. The chest now has the following items:</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="font-family:Consolas;">Coins Wood Gold Silver Bronze Medallion Cup</span></strong></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'>The <strong>second</strong> command adds <strong>only Pistol</strong> to the chest</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'>The <strong>third</strong> command <strong>&quot;</strong><strong><span style="font-family:Consolas;">Drop 3</span></strong><strong>&quot;</strong> removes the <strong>Gold</strong> from the chest, but immediately adds it at the <strong>end</strong>:</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="font-family:Consolas;">Pistol Coins Wood Silver Bronze Medallion Cup Gold</span></strong></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'>The <strong>fourth</strong> command <strong>&quot;Steal 3&quot;&nbsp;</strong>removes the <strong>last 3</strong> items <strong>Medallion</strong>, <strong>Cup</strong>, <strong>Gold</strong> from the chest and prints them.&nbsp;</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'>In the end calculate the average treasure gain which is the sum of all items length Pistol(<strong>6</strong>) + Coins(<strong>5</strong>) + Wood(<strong>4</strong>) &nbsp;+ Silver(<strong>6</strong>) + Bronze(<strong>6</strong>) = <strong>27</strong> and <strong>divide</strong> it by the count 27 / 5 = <strong>5.4</strong> and format it to the <strong>second decimal</strong> point.</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 515.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 21.1pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><strong>Input &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 198.25pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 117.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Diamonds|Silver|Shotgun|Gold</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Loot Silver Medals Coal</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Drop -1</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Drop 1</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Steal 6</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Yohoho!</span></p>
            </td>
            <td style="width: 317.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 117.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="line-height:150%;font-family:Consolas;">Coal, Diamonds, Silver, Shotgun, Gold, Medals</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  150%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="line-height:150%;font-family:Consolas;">Failed treasure hunt.</span></p>
            </td>
        </tr>
    </tbody>
</table>
