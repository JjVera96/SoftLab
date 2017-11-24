function validarFormulario(){
 
    var txtUsername = document.getElementById('username').value;
    var txtCorreo = document.getElementById('email').value;
    var txtFirstName = document.getElementById('first_name').value;
    var txtLastName = document.getElementById('last_name').value;
    var txtSecontLastName = document.getElementById('second_last_name').value;
    var txtAddress = document.getElementById('address').value;
    var txtCity = document.getElementById('city').value;
 
    //Test Username
    if(txtUsername == null || txtUsername.length == 0 || !(/^\d+$/.test(txtUsername))){
      alert('ERROR: El campo nombre no debe ir vacío,lleno de solamente espacios en blanco y debe contener solo digitos');
      return false;
    }
 
 
    //Test correo
    if(!(/^[a-z A-Z]+@utp.edu.co$/.test(txtCorreo))){
      alert('ERROR: Debe escribir un correo institucional (@utp.edu.co)');
      return false;
    }
 
    if(txtFirstName == null || txtFirstName.length == 0 || /^\s+$/.test(txtFirstName) !(/^[a-z A-Z]]+$/.test(txtFirstName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtLastName == null || txtLastName.length == 0 || /^\s+$/.test(txtLastName) || !(/^[a-z A-Z]]+$/.test(txtLastName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtSecontLastName == null || txtSecontLastName.length == 0 || /^\s+$/.test(txtSecontLastName) || !(/^[a-z A-Z]]+$/.test(txtSecontLastName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtAddress == null || txtAddress.length == 0 || /^\s+$/.test(txtAddress)){
      alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
      return false;
    }

    if(txtCity == null || txtCity.length == 0 || /^\s+$/.test(txtSecontLastName) || !(/^[a-z A-Z]]+$/.test(txtSecontLastName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }
 
    return true;
  }



  function validarFormularioEgre(){
 
    var txtUsername = document.getElementById('username').value;
    var txtCorreo = document.getElementById('email').value;
    var txtFirstName = document.getElementById('first_name').value;
    var txtLastName = document.getElementById('last_name').value;
    var txtSecontLastName = document.getElementById('second_last_name').value;
    var txtGraduate = document.getElementById('graduation').value;
    var txtBorn = document.getElementById('birthdate').value;
 
    //Test Username
    if(txtUsername == null || txtUsername.length == 0 || !(/^\d+$/.test(txtUsername))){
      alert('ERROR: El campo nombre no debe ir vacío,lleno de solamente espacios en blanco y debe contener solo digitos');
      return false;
    }
 
 
    //Test correo
    if(!(/^[a-z A-Z]+@utp.edu.co$/.test(txtCorreo))){
      alert('ERROR: Debe escribir un correo institucional (@utp.edu.co)');
      return false;
    }
 
    if(txtFirstName == null || txtFirstName.length == 0 || /^\s+$/.test(txtFirstName) !(/^[a-z A-Z]]+$/.test(txtFirstName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtLastName == null || txtLastName.length == 0 || /^\s+$/.test(txtLastName) || !(/^[a-z A-Z]]+$/.test(txtLastName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtSecontLastName == null || txtSecontLastName.length == 0 || /^\s+$/.test(txtSecontLastName) || !(/^[a-z A-Z]]+$/.test(txtSecontLastName))){
      alert('ERROR: El campo nombre no debe ir vacío, lleno de solamente espacios en blanco o con numeros');
      return false;
    }

    if(txtGraduate == null || txtGraduate.length == 0 || /^\s+$/.test(txtGraduate)){
      alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
      return false;
    }

    if(txtBorn == null || txtBorn.length == 0 || /^\s+$/.test(txtBorn)){
      alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
      return false;
    }

    if(txtBorn >= txtGraduate ){
      alert('ERROR: Los campos de fecha de nacimiento y graduación no son lógicos');
      return false;
    }
 
    return true;
  }