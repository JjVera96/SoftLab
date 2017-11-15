function validarFormulario(){
 
        var txtNombre = document.getElementById('nombre').value;
        var txtEdad = document.getElementById('edad').value;
        var txtCorreo = document.getElementById('correo').value;
        var txtFecha = document.getElementById('fecha').value;
        var cmbSelector = document.getElementById('selector').selectedIndex;
        var chkEstado = document.getElementById('checkBox');
 
 
        //Test campo obligatorio
        if(txtNombre == null || txtNombre.length == 0 || /^\s+$/.test(txtNombre)){
            alert('ERROR: El campo nombre no debe ir vacío o lleno de solamente espacios en blanco');
            return false;
        }
 
        //Test edad
        if(txtEdad == null || txtEdad.length == 0 || isNaN(txtEdad)){
            alert('ERROR: Debe ingresar una edad');
            return false;
        }
 
        //Test correo
        if(!(/\S+@\S+\.\S+/.test(txtCorreo))){
            alert('ERROR: Debe escribir un correo válido');
            return false;
        }
 
        //Test fecha
        if(!isNaN(txtFecha)){
            alert('ERROR: Debe elegir una fecha');
            return false;
        }
 
 
        return true;
    }