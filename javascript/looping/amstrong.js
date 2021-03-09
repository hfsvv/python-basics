var x=153;
r=0;

while (x>0) {
    var d=x%10;
    var r=r+d^3;
    x=x/10;

    
}
console.log(r);