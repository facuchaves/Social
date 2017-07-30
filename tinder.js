for ( var k=1 ; k < 10001 ; k++ ){
	setTimeout(function(){
		document.getElementsByClassName("recsGamepad__button--like")[0].click();
	},(k*1500) );
}