<?php
if (isset($_POST['submit']))
{
$rna = $_POST['rna'];
$mrna = $_POST['mrna'];
$file = fopen("user1.txt","w+") or die("The File is not open");
$file2 = fopen("user2.txt","w+") or die("The File is not open");
$s = $rna."";
$t = $mrna."";
fputs($file,$s) or die ("Empty Data not Accepted");
fputs($file2,$t) or die ("Empty Data not Accepted");
fclose($file);
fclose($file2);
shell_exec("C:/Users/Juthi/AppData/Local/Programs/Python/Python36/python C:/wamp64/www/RNA/KMP.py");
$file3 = fopen("output.txt", "r");
print '<pre>'.file_get_contents('output.txt').'</pre>';
fclose($file3);
}

?>
<center>
<form action="#" method ="post">
RNA:<input type="text" name="rna" ><br>
MRNA:<input type="text" name="mrna" ><br>
<input type="submit" name="submit" value="Write to file"><br>
</form>
</center>