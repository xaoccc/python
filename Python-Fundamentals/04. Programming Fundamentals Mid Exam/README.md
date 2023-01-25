# Problem 1 - Guinea Pig

Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!
### Input

•	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]

•	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]

•	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]

•	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]

### Output

•	If the food, the hay, and the cover are enough, print:

o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."

•	If one of the things is not enough, print:

o	"Merry must go to the pet store!"

The output values must be formatted to the second decimal place!

### Examples:
<table style="margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 239.6pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 21.1pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Input</strong></p>
            </td>
            <td style="width: 276.4pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 21.1pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 239.6pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 57.75pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:lime;">10</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:yellow;">5</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:aqua;">5.2</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;background:red;">1</span></p>
            </td>
            <td style="width: 276.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 57.75pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'><span style="font-family:Consolas;">Everything is fine! Puppy is happy! Food:&nbsp;</span><span style="font-family:Consolas;">1.00</span><span style="font-family:  Consolas;">, Hay: 1.</span><span style="font-family:  Consolas;">10</span><span style="font-family:Consolas;">, Cover: 1.87</span><span style="font-family:Consolas;">.</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family:Consolas;">&nbsp;</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">&nbsp;</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 516pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 2.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'>You receive food &ndash;&nbsp;<strong><span style="background:  lime;">10000</span></strong>, hay &ndash; <strong><span style="background:yellow;">5000</span></strong>, cover &ndash; <strong><span style="background:aqua;">5200</span></strong>, weight &ndash; <strong><span style="background:red;">1000</span></strong> (in grams).&nbsp;</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'>On the first day, Merry gives Puppy 300gr food &ndash;&nbsp;9700gr food left.</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'>On the second day, the food left is <strong>9400gr</strong>, so the needed hay is&nbsp;<strong>9</strong><strong>400 * 5% &nbsp;= 470</strong>,<strong>&nbsp;</strong>and the<strong>&nbsp;</strong>hay left is <strong>4530</strong><strong>.&nbsp;</strong></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'>On the third day, the cover left is <strong>4866.6</strong><strong>7</strong><strong>,&nbsp;</strong>and the food left is&nbsp;<strong>9</strong><strong>100</strong>,<strong>&nbsp;</strong>and so on.</p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'>On the last day, Merry has: food &ndash;&nbsp;1.00, hay &ndash; 1.10, and cover &ndash; 1.87.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 239.6pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 46.15pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1.5</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">3</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1.5</span></p>
            </td>
            <td style="width: 276.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 46.15pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'><span style="font-family:Consolas;">Merry must go to the pet store!</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 239.6pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 46.15pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">9</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">5</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">5.2</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1</span></p>
            </td>
            <td style="width: 276.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 46.15pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:justify;'><span style="font-family:Consolas;">Merry must go to the pet store!</span></p>
            </td>
        </tr>
    </tbody>
</table>
