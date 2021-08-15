
async function generarMatriz() {
    let n = document.getElementById("n").value;
    if ( n ){
        let valores = await eel.generarEstadoInicial(n)();
        console.log(Array.from(valores));

        var table_body_nueva = document.createElement('tbody');
        indice = 0

        for (var i = 0; i < n; i++){
            var tr = document.createElement('tr');
            for (var j = 0; j < n; j++){
                var td = document.createElement('td');
                var text = document.createTextNode(valores[indice]);
                td.appendChild(text);
                tr.appendChild(td);
                indice++;
            }
            table_body_nueva.appendChild(tr);
        }
        table_body_nueva.classList.add("text-center");
        table_body_nueva.setAttribute("id", "tabla_inicial_body");
        var tabla_body_original = document.getElementById("tabla_inicial_body");
        var tabla = document.getElementById("tabla_inicial");
        tabla.replaceChild(table_body_nueva, tabla_body_original)
    }
    else{
        alert("Ingrese un valor para N")
    }
}

async function buscarResolucion(){
    let algoritmo = document.getElementById("algotritmo").value;
    let n = document.getElementById("n").value;
    // BUSCAR FORMA DE OBTENER EL ESTADO INICIAL Y VALIDAR QUE YA SE HAYA GENERADO
    // SEPARAR PARA ELEGIR VARIOS ALGORITMOS

}