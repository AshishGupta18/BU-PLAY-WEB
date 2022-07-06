const btn = document.querySelector('button')
btn.onclick=() => {
    
    var num1 = 50; 
    var num2 = 600;

// add two numbers
var sum = num1 + num2;
const alpha_score=document.querySelector(".alpha-score")
alpha_score.textContent=sum;
const redeem=document.querySelector(".coin-redeem")
redeem.remove()
const button=document.querySelector(".redeem")
button.remove()

}