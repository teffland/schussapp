<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=Generator content="Microsoft Word 11 (filtered)">
<title>Schussmeisters Ski Club, Inc</title>
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:"Arial Black";
	panose-1:2 11 10 4 2 1 2 2 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	margin-bottom:.0001pt;
	font-size:12.0pt;
	font-family:"Times New Roman";}
@page Section1
	{size:566.65pt 5.0in;
	margin:.1in .3in .1in .3in;}
div.Section1
	{page:Section1;}
-->
</style>

</head>

<body lang=EN-US>
{% with pass.member as member %}
<div class=Section1>

<p class=MsoNormal align=center style='text-align:center'><b><i><span
style='font-size:18.0pt;font-family:"Arial Black"'>Schussmeisters Ski Club,
Inc.</span></i></b></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-size:18.0pt;font-family:Arial'>{{pass.season}}</span></p>

<table border="0" cellpadding="0" cellspacing="0" style="text-align:center">
   <tr>
   	<td><p class=MsoNormal><span style='font-family:Arial'>IDNUMBER:</span></p></td>
   	<td><p class=MsoNormal><span style='font-family:Arial'>&nbsp;&nbsp;&nbsp;&nbsp;CARD NUMBER:</span></p></td>
   </tr>
   <tr>
   	<td><p class=MsoNormal><b><u><span style='font-family:Arial'>{{member.id}}</span></u></b></p></td>
   	<td><p class=MsoNormal><b><b><u><span style='font-family:Arial'>{{pass.active_id}}</span></u></b></td>
   </tr>
</table>

<p class=MsoNormal><b><u><span style='font-family:Arial'><span style='text-decoration:none'>&nbsp;</span></span></u></b></p>

<p class=MsoNormal><span style='font-family:Arial'>Name:                         <b>{{member.first_name}}  {{member.last_name}}</b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Email:                          <b>{{member.email}}</b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Local Address:          <b>{{member.local_address}}</b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>City/ST/Zip:                <b>{{member.city}}, {{member.state}} {{member.zip_code}}</b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Birthdate:                   <b>{{member.birthday}}</b>                Telephone:
<b>{{member.phone}}</b>     Sex:<b>{{member.gender}}</b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Type:                           <b><?=$member_type?></b>                   Date Joined: <b><?=substr($created,0,10)?></b></span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Price:                          <b>$<?=$signup_price?></b>                      </span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>Received By:                                                 </span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

<p class=MsoNormal><span style='font-family:Arial'>___________</span></p>

<p class=MsoNormal><span style='font-family:Arial'>&nbsp;</span></p>

</div>

</body>

</html>
