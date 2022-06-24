/* INITIALIZE PHONE INPUTS WITH THE intlTelInput FEATURE*/
let input = document.querySelector("#phone");

let iti = intlTelInput(input);

$(window).on("load", function() {
  
   intlTelInputGlobals.loadUtils("https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/15.0.1/js/utils.js");
   
   intlTelInput(input, {
      initialCountry: "us",
      separateDialCode: true,
      nationalMode: false,
      onlyCountries: ["us", "jp", "ca"]
    });

    let countryData = window.intlTelInputGlobals.getCountryData();
   
    console.log(countryData);
  
});

/* ADD A PATTERN MASK IN PHONE INPUT AND REMOVE PREVIOUS VALUE - ON COUNTRY CHANGE */
// $("#phone").on("countrychange", function(e, countryData) {
  
//   // $("#phone").val("").trigger("input");
  
//   let placeholder = $("#phone").attr("placeholder");
    
//     let pattern = placeholder.replace(/-/g, " ");
//     let phoneNumber = pattern.replace(/\d/gi, "0");

//     $("#phone").mask(phoneNumber);
  

  
// });


$("#phone").focusout( function(e, countryData) {
  
  let phone_number = $("#phone").val();
      phone_number = iti.getNumber(intlTelInputUtils.numberFormat.E164);
    
      console.log(phone_number);
});