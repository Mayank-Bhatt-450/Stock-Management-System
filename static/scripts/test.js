//alert ('lol');
//var x =document.querySelector('#id');//document.getElementById('id')
//alert (x.getAttribute("value"));
document.getElementById('id').onclick = function() {
    // access properties using this keyword
    if ( this.checked ) {
        // if checked ...
        alert( this.value );
    } else {
        // if not checked ...
    }
};
