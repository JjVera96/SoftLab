// Wait for the DOM to be ready
$(function() {

  jQuery.validator.addMethod("validatemail",
           function(email, element) {
                   return /^[A-Za-z\d=#$%]+@utp.edu.co$/.test(value);
           },
   "Nada de caracteres especiales, por favor"
);  
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='admin_registration']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      username: "required",
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        validatemail: true,
        email: true
      }, 
      first_name: "required",
      last_name: "required",
      second_last_name: "required",
      address= "required",
      
    },
    // Specify validation error messages
    messages: {
      username: "Por favor digita tu número de identificación",
      email: "Por favor digita un correo institucional (@utp.edu.co)"
      first_name: "Por favor digita tu primer nombre",
      last_name: "Por favor digita tu primer apellido",
      second_last_name:"Por favor digita tu segundo apellido",
      address: "Por favor digite su dirección"      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});