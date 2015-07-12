var count=5;

var counter=setInterval(timer, 1000); //1000 will run it every 1 second

function timer()
{
  count=count-1;
  if (count <= -1)
  {
     clearInterval(counter);
     //counter ended, do something here
     document.getElementById("agenda-message").innerHTML="<p class='close-header'><strong>Thank You for Participating!<br/>Today's Campaign Selection is Now Closed</strong><br/><br/>Selections will be reviewed by Town Hall<br/>for appropriate language and behavior.<br/>If all looks good, we'll tweet them out tonight!";
  }

  //Do code for showing the number of seconds here
 document.getElementById("timer").innerHTML=count + " secs"; // watch for spelling
}