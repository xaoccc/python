<h1 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:27px;font-family:"Calibri",sans-serif;color:#642D08;text-align:center;'>Lab: Functions</h1>
<div style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ol style="margin-bottom:0in;list-style-type: decimal;margin-left:11.3px;">
        <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
            <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Absolute Values</h2>
        </li>
    </ol>
</div>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Write a program that receives a sequence of numbers, separated by a single space, and <strong>prints</strong> their <strong>absolute value&nbsp;</strong>as a list. Use <strong><span style="font-family:Consolas;">abs()</span></strong>.</p>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'>Example</h3>
<table style="width:267.95pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 111.1pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.65pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 156.85pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.65pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 111.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">1 2.5 -3 -4.5</span></p>
            </td>
            <td style="width: 156.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">[1.0, 2.5, 3.0, 4.5]</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 111.1pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;height: 1.8pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:  Consolas;">-0 1 10 -6.66</span></p>
            </td>
            <td style="width: 156.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;height: 1.8pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">[</span><span style="font-family:Consolas;">0</span><span style="font-family:Consolas;">.0,&nbsp;</span><span style="font-family:Consolas;">1</span><span style="font-family:Consolas;">.</span><span style="font-family:Consolas;">0</span><span style="font-family:Consolas;">,&nbsp;</span><span style="font-family:Consolas;">10</span><span style="font-family:Consolas;">.0,&nbsp;</span><span style="font-family:Consolas;">6</span><span style="font-family:Consolas;">.</span><span style="font-family:Consolas;">66</span><span style="font-family:Consolas;">]</span></p>
            </td>
        </tr>
    </tbody>
</table>
<div style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ol style="margin-bottom:0in;list-style-type: undefined;">
        <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
            <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Grades</h2>
        </li>
    </ol>
</div>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Write a function that <strong>receives a grade</strong> between <strong>2.00</strong> and <strong>6.00</strong> and <strong>prints the corresponding grade in words</strong>.</p>
<ul class="decimal_type" style="list-style-type: disc;">
    <li>2.00 &ndash; 2.99 - &quot;<strong><span style="font-family:Consolas;">Fail</span></strong>&quot;</li>
    <li>3.00 &ndash; 3.49 - &quot;<strong><span style="font-family:Consolas;">Poor</span></strong>&quot;</li>
    <li>3.50 &ndash; 4.49 - &quot;<strong><span style="font-family:Consolas;">Good</span></strong>&quot;</li>
    <li>4.50 &ndash; 5.49 - &quot;<strong><span style="font-family:Consolas;">Very Good</span></strong>&quot;</li>
    <li>5.50 &ndash; 6.00 - &quot;<strong><span style="font-family:Consolas;">Excellent</span></strong>&quot;</li>
</ul>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'>Examples</h3>
<table style="width:134.45pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 56.4pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 78pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 56.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">3.33</span></p>
            </td>
            <td style="width: 78pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Poor</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 56.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">4.50</span></p>
            </td>
            <td style="width: 78pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Very Good</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 56.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">2.99</span></p>
            </td>
            <td style="width: 78pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:  normal;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">Fail</span></p>
            </td>
        </tr>
    </tbody>
</table>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'><br></h3>
<div style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ol style="margin-bottom:0in;list-style-type: undefined;">
        <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
            <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Calculations</h2>
        </li>
    </ol>
</div>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Create a function that <strong>receives</strong> three parameters, <strong>calculates</strong> a result depending on the given operator, and <strong>returns</strong> it. Print the result of the function.</p>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>The input comes as three parameters &ndash; an <strong>operator as a string</strong> and <strong>two integer numbers</strong>. The operator can be one of the following: &nbsp;<span style="font-family:Consolas;">&quot;<strong>multiply</strong>&quot;</span>, <span style="font-family:Consolas;">&quot;<strong>divide</strong>&quot;</span>, <span style="font-family:Consolas;">&quot;<strong>add</strong>&quot;</span>, <span style="font-family:Consolas;">&quot;<strong>subtract</strong>&quot;</span>.</p>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'>Example</h3>
<table style="width:109.75pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 62.95pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 46.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 62.95pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">subtract</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">5</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">4</span></p>
            </td>
            <td style="width: 46.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">1</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 62.95pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">divide</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">8</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">4</span></p>
            </td>
            <td style="width: 46.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">2</span></p>
            </td>
        </tr>
    </tbody>
</table>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'><br></h3>
<ul style="list-style-type: disc;">
    <li>Print the result by calling the function and passing the given parameters.</li>
    <li>
        <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Repeat String</h2>
    </li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Write a function that receives a <strong>string&nbsp;</strong>and a <strong>counter</strong> <strong><span style="font-family:Consolas;">n</span></strong>. The function should <strong>return</strong> a new string &ndash; the result of repeating the old string <strong>n</strong> times. Print the result of the function. Try using <strong>lambda</strong>.</p>
<p style='margin-top:6.0pt;margin-right:0in;margin-bottom:4.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="font-size:21px;line-height:115%;color:#8F400B;">Examples</span></strong></p>
<table style="width:138.0pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 50.85pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 87.1pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 50.85pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">abc</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">3</span></p>
            </td>
            <td style="width: 87.1pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">abcabcabc</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 50.85pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">String</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">2</span></p>
            </td>
            <td style="width: 87.1pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">StringString</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style="margin-top:6.0pt;margin-right:0in;margin-bottom:4.0pt;margin-left:7.05pt;line-height:115%;font-size:15px;font-family:&quot;Calibri&quot;,sans-serif;"></p>
<ol style="margin-bottom:0in;list-style-type: undefined;">
    <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
        <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Orders</h2>
    </li>
</ol>
<p></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Write a function that <strong>calculates</strong> the <strong>total</strong> <strong>price</strong> of an order and <strong>returns</strong> it. The function should receive one of the following products: &quot;<strong><span style="font-family:Consolas;">coffee&quot;</span></strong>,<strong>&nbsp;&quot;</strong><strong><span style="font-family:Consolas;">coke</span></strong><strong>&quot;</strong>,<strong>&nbsp;&quot;</strong><strong><span style="font-family:Consolas;">water</span></strong><strong>&quot;</strong>,<strong>&nbsp;</strong>or<strong>&nbsp;&quot;</strong><strong><span style="font-family:Consolas;">snacks</span></strong><strong>&quot;</strong>, and a <strong>quantity</strong> of the product. The <strong>prices</strong> for a single piece of each product are:&nbsp;</p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style="margin-top:0in;margin-bottom:10.0pt;">coffee - 1.50</li>
    <li style="margin-top:0in;margin-bottom:10.0pt;">water - 1.00</li>
    <li style="margin-top:0in;margin-bottom:10.0pt;">coke - 1.40</li>
    <li style="margin-top:0in;margin-bottom:10.0pt;">snacks - 2.00</li>
</ul>
<p style="margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:.5in;">&nbsp;</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Print the result <strong>formatted</strong> to the <strong>second</strong> <strong>decimal</strong> <strong>place</strong>.</p>
<p style='margin-top:6.0pt;margin-right:0in;margin-bottom:4.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="font-size:21px;line-height:115%;color:#8F400B;">Example</span></strong></p>
<table style="width:91.1pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 44.3pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 46.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 44.3pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">water</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">5</span></p>
            </td>
            <td style="width: 46.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">5.00</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 44.3pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">coffee</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">2</span></p>
            </td>
            <td style="width: 46.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">3.00</span></p>
            </td>
        </tr>
    </tbody>
</table>
<div style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ol style="margin-bottom:0in;list-style-type: undefined;">
        <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
            <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Calculate Rectangle Area</h2>
        </li>
    </ol>
</div>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'>Create a function that <strong>calculates</strong> and <strong>returns</strong> the <strong>area of a rectangle</strong> by given <strong>width</strong> and <strong>height</strong>. <strong>Print the result&nbsp;</strong>on the console.</p>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'>Examples</h3>
<table style="width:85.25pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 38.4pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 46.85pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 0.9pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 38.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">3</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">4</span></p>
            </td>
            <td style="width: 46.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">12</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 38.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">6</span></p>
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">2</span></p>
            </td>
            <td style="width: 46.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:4.0pt;margin-right:0in;margin-bottom:.0001pt;margin-left:0in;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;margin:0in;'><span style="font-family:Consolas;">12</span></p>
            </td>
        </tr>
    </tbody>
</table>
<div style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ol style="margin-bottom:0in;list-style-type: undefined;margin-left:11.3px;">
        <li style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>
            <h2 style='margin-top:10.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:.25in;text-indent:-.25in;line-height:115%;font-size:24px;font-family:"Calibri",sans-serif;color:#7C380A;'>Rounding</h2>
        </li>
    </ol>
</div>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Write a program that <strong>rounds</strong> all the given numbers, separated by a single space, and <strong>prints the result</strong> as a list. Use <strong><span style="font-family:Consolas;">round()</span></strong>.</p>
<h3 style='margin-top:6.0pt;margin-right:0in;margin-bottom:2.0pt;margin-left:0in;line-height:115%;font-size:21px;font-family:"Calibri",sans-serif;color:#8F400B;'>Example</h3>
<table style="width:253.75pt;margin-left:1.15pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 133.6pt;border: 1pt solid windowtext;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 4.25pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Input</strong></p>
            </td>
            <td style="width: 120.15pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;background: rgb(217, 217, 217);padding: 2.85pt 4.25pt;height: 4.25pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong>Output</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 133.6pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">1.0 2.5 3.0 4.5</span></p>
            </td>
            <td style="width:120.15pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:2.85pt 4.25pt 2.85pt 4.25pt;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">[1, 2, 3, 4]</span></p>
            </td>
        </tr>
        <tr>
            <td style="width: 133.6pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 2.85pt 4.25pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">2.56 1.9 -3.4 8.1</span></p>
            </td>
            <td style="width:120.15pt;border-top:none;border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;padding:2.85pt 4.25pt 2.85pt 4.25pt;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><span style="font-family:Consolas;">[3, 2, -3, 8]</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:4.0pt;margin-right:0in;margin-bottom:6.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
