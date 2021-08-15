
async function generarMatriz() {
    let n = document.getElementById("n").value;
    if ( n ){
        let valores = await eel.generarEstadoInicial(n)();
        console.log(Array.from(valores));
        
    }
    else{
        alert("Ingrese un valor para N")
    }
}