document.getElementById("formulario").addEventListener("submit", function(e) {
    e.preventDefault();

    const ecuacion = document.getElementById("ecuacion").value;
    const x0 = parseFloat(document.getElementById("x0").value);
    const y0 = parseFloat(document.getElementById("y0").value);
    const h = parseFloat(document.getElementById("h").value);
    const n = parseInt(document.getElementById("n").value);

    fetch("/calcular", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ecuacion, x0, y0, h, n })
    })
    .then(response => response.json())
    .then(data => {
        // Tabla
        const tabla = document.getElementById("tabla-resultados");
        tabla.innerHTML = "";
        data.tabla.forEach(fila => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${fila.n}</td>
                <td>${fila.xn}</td>
                <td>${fila.yn}</td>
                <td>${fila.yreal}</td>
                <td>${fila.error}</td>
            `;
            tabla.appendChild(tr);
        });

        // Gráfica
        const ctx = document.getElementById('grafica').getContext('2d');
        if (window.miGrafica) window.miGrafica.destroy(); // evitar superposición

        window.miGrafica = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.grafica.x,
                datasets: [
                    {
                        label: 'Euler Mejorado',
                        data: data.grafica.y_aprox,
                        borderColor: 'blue',
                        fill: false
                    },
                    {
                        label: 'Solución Exacta',
                        data: data.grafica.y_exact,
                        borderColor: 'green',
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Comparación de Resultados'
                    }
                }
            }
        });
    });
});
//!Pestañas
function openTab(event, tabName) {
    var i, tabContent, tabButtons;
    tabContent = document.querySelectorAll(".tab-content");
    tabButtons = document.querySelectorAll(".tab-button");

    tabContent.forEach(tab => tab.style.display = "none");
    tabButtons.forEach(button => button.classList.remove("active-btn"));

    document.getElementById(tabName).style.display = "block";
    event.currentTarget.classList.add("active-btn");
}

// Mostrar el primer contenido por defecto
document.getElementById("info").style.display = "block";