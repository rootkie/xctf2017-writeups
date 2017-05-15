<?php

$session="757365723d6a6f686e7c706173733d373065306636636261393335313337356431656333343430633665326135653431333839643932633633326261613161323863613364393330633461356130357c61646d696e3d30";
$session_hash="7e2967c611fc7e66b2e75a2fcb4ef80cdc75c91c8967ef058203d99688a146ab";

function String2Hex($string){
	$hex='';
	for ($i=0; $i < strlen($string); $i++){
		$hex .= dechex(ord($string[$i]));
	}
	return $hex;
}

function Hex2String($hex){
	$string='';
	for ($i=0; $i < strlen($hex)-1; $i+=2){
		$string .= chr(hexdec($hex[$i].$hex[$i+1]));
	}
	return $string;
}


$temp = Hex2String($session);

#$session_hash =  hash("sha256", "asdf".$temp);
    
while($f = fgets(STDIN)){
    if(hash("sha256",trim($f).$temp) === $session_hash) {
        echo $f;
    }
}

?>
