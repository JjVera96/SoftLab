function validarFormulario(){
 		
 		var txtUser = document.getElementById('username').value;
        var txtPrimerNombre = document.getElementById('first_name').value;
        var txtPrimerApellido = document.getElementById('last_name').value;
        var txtSegundoApellido = document.getElementById('second_last_name').value;
        var txtCorreo = document.getElementById('email').value;
        var txtGender = document.getElementById('gender').selectedIndex;
 
 
        //Test campo obligatorio
        if(txtPrimerNombre == null || txtPrimerNombre.length == 0 || /^[a-z A-Z]+$/.test(txtPrimerNombre)){
            alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
            return false;
        }

        if(txtPrimerApellido == null || txtPrimerApellido.length == 0 || /^[a-z A-Z]+$/.test(txtPrimerApellido)){
            alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
            return false;
        }

        if(txtSegundoApellido == null || txtSegundoApellido.length == 0 || /^[a-z A-Z]+$/.test(txtSegundoApellido)){
            alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
            return false;
        }
 
        //Test correo
        if(!(/\S+@utp.edu.co/.test(txtCorreo))){
            alert('ERROR: Debe escribir un correo institucional (@utp.edu.co)');
            return false;
        }

        //Test comboBox
		if(txtGender == null || txtGender == 0){
			alert('ERROR: Debe seleccionar una opción');
			return false;
		}
 
        return true;
    }
