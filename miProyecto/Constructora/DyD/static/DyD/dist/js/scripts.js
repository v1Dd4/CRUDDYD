var iniciar = document.getElementById('Iniciar');
var nulo = "";
function verificar(){
    var nombre = document.getElementById('Email').value;
    var contraseña = document.getElementById('Contraseña').value;
    if(nombre == nulo){
        Swal.fire({
            icon: "info",
            title: "Oops...",
            text: "Es necesario rellenar los apartados para continuar.",
        });
    }
    else if(contraseña == nulo){
        Swal.fire({
            icon: "info",
            title: "Oops...",
            text: "Es necesario rellenar los apartados para continuar.",
        }); 
    }

}