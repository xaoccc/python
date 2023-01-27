# Problem 1 - Bonus Scoring System

Create a program that calculates bonus points for each student enrolled in a course. On the first line, you are going to receive the number of the students. On the second line, you will receive the total number of lectures in the course. The course has an additional bonus, which you will receive on the third line. On the following lines, you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:  
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})  
Find the student with the maximum bonus and print them, along with his attendances, in the following format:  
"Max Bonus: {max bonus points}."  
"The student has attended {student attendances} lectures."  
Round the bonus points at the end to the nearest larger number.

### Input / Constrains

•	On the first line, you are going to receive the number of the students – an integer in the range [0…50]  
•	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].  
•	On the third line, you will receive the additional bonus – an integer number in the range [0….100].  
•	On the following lines, you will be receiving the attendance of each student.  
•	There will never be students with equal bonuses.

### Output

•	Print the maximum bonus points and the attendances of the given student, rounded to the nearest larger number, scored by a student in this course in the format described above.

### Examples  
<table style="width:545.75pt;margin-left:-.25pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 248.1pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.2pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 297.65pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 22.2pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 248.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 117pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><span style="font-family:Consolas;">5<br>25<br>30<br>12<br>19<br>24<br>16<br>20</span></p>
            </td>
            <td style="width: 297.65pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 117pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><span style="font-family:Consolas;">Max Bonus: 34.</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><span style="font-family:Consolas;">The student has attended 24 lectures.</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 545.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;height: 17.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style="line-height:115%;">Comments</span></strong></p>
            </td>
        </tr>
        <tr>
            <td colspan="2" style="width: 545.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 67.45pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>First, we receive the <strong>number of students</strong> enrolled in the course &ndash; <strong>5</strong>. The total count of the lectures is <strong>25,</strong> and the additional bonus is <strong>30</strong>. Then we calculate the bonus of the student with 12 attendances, which is <strong>16.8</strong>. We continue calculating <strong>each of the student&apos;s bonuses</strong>. The one <strong>with 24 attendances</strong> has the <strong>highest bonus &ndash; 33.6 (34 rounded)</strong>, so we print the appropriate message on the console.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 248.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 117pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;background:white;'><span style="font-family:Consolas;">10<br>30<br>14<br>8<br>23<br>27<br>28<br>15<br>17<br>25<br>26<br>5<br>18</span></p>
            </td>
            <td style="width: 297.65pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 117pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><span style="font-family:Consolas;">Max Bonus:&nbsp;</span><span style="line-height:150%;font-family:Consolas;">18.</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;text-align:  justify;'><span style="line-height:  150%;font-family:Consolas;">The student has attended 28 lectures.</span></p>
            </td>
        </tr>
    </tbody>
</table>

# Problem 2. Mu Online

You have **initial health 100 and initial bitcoins 0**. You will be given a **string representing the dungeon's rooms**. Each room is separated with '|' (vertical bar): **"room1|room2|room3…"**  
Each room contains **a command and a number**, separated by space. The command can be:  
*	"potion"
    *	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
    *	First print: "You healed for {amount} hp."
    *	After that, print your current health: "Current health: {health} hp."
*	"chest"
    *	You've found some bitcoins, the number in the second part.
    *	Print: "You found {amount} bitcoins."
*	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
    *	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
    *	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines:  
**"You've made it!"**  
**"Bitcoins: {bitcoins}"**  
**"Health: {health}"**  
### Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
### Output
Print the corresponding messages described above.
### Examples
<table style="width: 88%; border-collapse: collapse; border: none; margin-right: calc(12%);">
    <tbody>
        <tr>
            <td style="width: 67.9139%; border: 1pt solid windowtext; background: rgb(217, 217, 217); padding: 2.85pt 4.25pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Input</strong></p>
            </td>
            <td style="width: 31.9536%; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; background: rgb(217, 217, 217); padding: 2.85pt 4.25pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 67.9139%; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 2.85pt 4.25pt; height: 20.3pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000</span></p>
            </td>
            <td style="width: 31.9536%; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 2.85pt 4.25pt; height: 20.3pt; vertical-align: top;">
                <p style="line-height: 1; font-size: 15px; font-family: Calibri, sans-serif; margin: 0in;"><span style="font-family: Consolas; line-height: 1;">You slayed rat.<br>You slayed bat.<br>You healed for 10 hp.<br>Current health:&nbsp;80 hp.<br>You slayed rat.<br>You found 100 bitcoins.<br>You died! Killed by boss.<br>Best room: 6</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 67.9139%; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; background: rgb(217, 217, 217); padding: 2.85pt 4.25pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Input</strong></p>
            </td>
            <td style="width: 31.9536%; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; background: rgb(217, 217, 217); padding: 2.85pt 4.25pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 67.9139%; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 2.85pt 4.25pt; height: 20.3pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">cat 10|potion&nbsp;</span><span style="font-family:  Consolas;">30</span><span style="font-family:Consolas;">|orc&nbsp;10|chest 10|</span><span style="font-family:  Consolas;">snake</span><span style="font-family:Consolas;">&nbsp;25|chest 110</span></p>
            </td>
            <td style="width: 31.9536%; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 2.85pt 4.25pt; height: 20.3pt; vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:150%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">You slayed cat.<br>You healed for 10 hp.<br>Current health: 100 hp.<br>You slayed orc.<br>You found 100 bitcoins.<br>You slayed snake.<br>You found 110 bitcoins.<br>You&apos;ve made it!<br>Bitcoins: 120<br>Health: 65</span></p>
            </td>
        </tr>
    </tbody>
</table>
