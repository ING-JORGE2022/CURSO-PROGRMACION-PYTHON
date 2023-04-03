// Selecciona el botón de enviar y los campos del formulario
const submitButton = document.querySelector('.button');
const tipoDocumento = document.querySelector('#tipo_documento');
const numeroDocumento = document.querySelector('#numero_documento');
const password = document.querySelector('#password');

// Agrega un event listener al botón de enviar
submitButton.addEventListener('click', (event) => {
  event.preventDefault(); // Previene el comportamiento por defecto del formulario
  
  let valid = true; // Inicializa la variable valid en true
  
  // Valida si los campos están vacíos
  if (tipoDocumento.value === "" || numeroDocumento.value === "" || password.value === "") {
    // Si los campos están vacíos, muestra el mensaje de error en rojo
    const mensaje = document.createElement('p');
    mensaje.style.color = 'red';
    
    mensaje.textContent = 'Rellene los campos vacíos para poder continuar';
    
    const formList = document.querySelector('.form_list');
    formList.appendChild(mensaje);
    
    valid = false; // Cambia la variable valid a false
  }
  
  if (valid) {
    // Si todos los campos están completos, redirecciona a la página deseada
    window.location.href = 'busco.html';
  }
});

// el código valida los campos de un formulario y redirige al usuario a otra página si el formulario es válido.