
async function generarMatriz() {
    let n = parseInt(document.getElementById("n").value);
    let algoritmo = parseInt(document.getElementById("algoritmo").value);
    if ( n ){
        let valores = await eel.generarEstadoInicial(n)();
        console.log(Array.from(valores));

        var table_body_nueva = document.createElement("tbody");
        var indice = 0
        for (var i = 0; i < n; i++){
            var tr = document.createElement("tr");
            for (var j = 0; j < n; j++){
                var td = document.createElement("td");
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

        if(algoritmo == 0){
            let resultado = await eel.iniciar_bfs(valores, n)();
            console.log(resultado);
            if(resultado) {
                var div_resultados = document.createElement("div");
                div_resultados.classList.add("d-flex");
                div_resultados.classList.add("flex-column");
                div_resultados.classList.add("align-items-center");
                div_resultados.setAttribute("id", "div_resultados");
                var tabla_body = crearBodyTabla(n, resultado["matriz_fin"]);

                var div_tablas = document.getElementById("tablas");
                var h1 = document.createElement("h1");
                h1.classList.add("display-6");
                var text_estado_final = document.createTextNode("Estado Final");
                h1.appendChild(text_estado_final)
                div_resultados.appendChild(h1);

                var tabla = document.createElement("table");
                tabla.classList.add("table");
                tabla.classList.add("table-bordered");
                tabla.classList.add("w-25");
                tabla.classList.add("table-dark");
                tabla.setAttribute("id", "tabla_fin");
                tabla.appendChild(tabla_body);
                div_resultados.appendChild(tabla);

                var span_tiempo = document.createElement("span");
                var text_tiempo = document.createTextNode("El tiempo transcurrido en milisegundos para encontrar la solucion fue de: " + resultado["tiempo"].toString());
                span_tiempo.appendChild(text_tiempo);
                div_resultados.appendChild(span_tiempo);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("La cantidad de nodos expandidos fue de: " + resultado["cant_nodos"].toString());
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("El camino de solucion es: " + resultado["solucion"]);
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);
                if(document.getElementById("div_resultados") == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    var div_viejo = document.getElementById("div_resultados");
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            } else {
                alert("La busqueda tardo mas de 30 segundos y no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                var div_tablas = document.getElementById("tablas");
                var div_resultados = document.createElement("div");
                div_resultados.setAttribute("id", "div_resultados");
                var span_sin_solucion = document.createElement("span");
                var texto_mas_30_seg = document.createTextNode("La busqueda tardo mas de 30 segundos o no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                span_sin_solucion.appendChild(texto_mas_30_seg);
                div_resultados.appendChild(span_sin_solucion);

                var div_viejo = document.getElementById("div_resultados");
                if(div_viejo == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            }
        }
        else if(algoritmo == 1){
            let resultado = await eel.iniciar_busqueda_con_a(valores, n, true)();
            console.log(resultado);
            if(resultado) {
                var div_resultados = document.createElement("div");
                div_resultados.classList.add("d-flex");
                div_resultados.classList.add("flex-column");
                div_resultados.classList.add("align-items-center");
                div_resultados.setAttribute("id", "div_resultados");
                var tabla_body = crearBodyTabla(n, resultado["matriz_fin"]);

                var div_tablas = document.getElementById("tablas");
                var h1 = document.createElement("h1");
                h1.classList.add("display-6");
                var text_estado_final = document.createTextNode("Estado Final");
                h1.appendChild(text_estado_final)
                div_resultados.appendChild(h1);

                var tabla = document.createElement("table");
                tabla.classList.add("table");
                tabla.classList.add("table-bordered");
                tabla.classList.add("w-25");
                tabla.classList.add("table-dark");
                tabla.setAttribute("id", "tabla_fin");
                tabla.appendChild(tabla_body);
                div_resultados.appendChild(tabla);

                var span_tiempo = document.createElement("span");
                var text_tiempo = document.createTextNode("El tiempo transcurrido en milisegundos para encontrar la solucion fue de: " + resultado["tiempo"].toString());
                span_tiempo.appendChild(text_tiempo);
                div_resultados.appendChild(span_tiempo);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("La cantidad de nodos expandidos fue de: " + resultado["cant_nodos"].toString());
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("El camino de solucion es: " + resultado["solucion"]);
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);
                if(document.getElementById("div_resultados") == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    var div_viejo = document.getElementById("div_resultados");
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            } else {
                alert("La busqueda tardo mas de 5 minutos y no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                var div_tablas = document.getElementById("tablas");
                var div_resultados = document.createElement("div");
                div_resultados.setAttribute("id", "div_resultados");
                var span_sin_solucion = document.createElement("span");
                var texto_mas_30_seg = document.createTextNode("La busqueda tardo mas de 5 minutos y no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                span_sin_solucion.appendChild(texto_mas_30_seg);
                div_resultados.appendChild(span_sin_solucion);

                var div_viejo = document.getElementById("div_resultados");
                if(div_viejo == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            }
        }
        else if(algoritmo == 2){
            let resultado = await eel.iniciar_busqueda_con_a(valores, n, false)();
            console.log(resultado);
            if(resultado) {
                var div_resultados = document.createElement("div");
                div_resultados.classList.add("d-flex");
                div_resultados.classList.add("flex-column");
                div_resultados.classList.add("align-items-center");
                div_resultados.setAttribute("id", "div_resultados");

                var tabla_body = crearBodyTabla(n, resultado["matriz_fin"]);

                var div_tablas = document.getElementById("tablas");
                var h1 = document.createElement("h1");
                h1.classList.add("display-6");
                var text_estado_final = document.createTextNode("Estado Final");
                h1.appendChild(text_estado_final)
                div_resultados.appendChild(h1);

                var tabla = document.createElement("table");
                tabla.classList.add("table");
                tabla.classList.add("table-bordered");
                tabla.classList.add("w-25");
                tabla.classList.add("table-dark");
                tabla.setAttribute("id", "tabla_fin");
                tabla.appendChild(tabla_body);
                div_resultados.appendChild(tabla);

                var span_tiempo = document.createElement("span");
                var text_tiempo = document.createTextNode("El tiempo transcurrido en milisegundos para encontrar la solucion fue de: " + resultado["tiempo"].toString());
                span_tiempo.appendChild(text_tiempo);
                div_resultados.appendChild(span_tiempo);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("La cantidad de nodos expandidos fue de: " + resultado["cant_nodos"].toString());
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);

                var span_nodos = document.createElement("span");
                var text_nodos = document.createTextNode("El camino de solucion es: " + resultado["solucion"]);
                span_nodos.appendChild(text_nodos);
                div_resultados.appendChild(span_nodos);
                if(document.getElementById("div_resultados") == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    var div_viejo = document.getElementById("div_resultados");
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            } else {
                alert("La busqueda tardo mas de 5 minutos y no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                var div_tablas = document.getElementById("tablas");
                var div_resultados = document.createElement("div");
                div_resultados.setAttribute("id", "div_resultados");
                var span_sin_solucion = document.createElement("span");
                var texto_mas_30_seg = document.createTextNode("La busqueda tardo mas de 5 minutos y no se pudo encontrar una solucion. Intente nuevamente o utilize otro algoritmo.");
                span_sin_solucion.appendChild(texto_mas_30_seg);
                div_resultados.appendChild(span_sin_solucion);

                var div_viejo = document.getElementById("div_resultados");
                if(div_viejo == null){
                    div_tablas.appendChild(div_resultados);
                }else{
                    div_tablas.replaceChild(div_resultados, div_viejo)
                }
            }
        }
    }
    else{
        alert("Ingrese un valor para N")
    }
}

function crearBodyTabla(n, valores){
    var table_body_nueva = document.createElement("tbody");
    var indice = 0
    for (var i = 0; i < n; i++){
        var tr = document.createElement("tr");
        for (var j = 0; j < n; j++){
            var td = document.createElement("td");
            var text = document.createTextNode(valores[indice]);
            td.appendChild(text);
            tr.appendChild(td);
            indice++;
        }
        table_body_nueva.appendChild(tr);
    }
    return table_body_nueva;
}