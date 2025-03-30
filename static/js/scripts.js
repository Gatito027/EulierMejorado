document.getElementById("form-calcular").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const data = {
        Ecuacion: formData.get("Ecuacion"),
        valorY: formData.get("valorY"),
        valorX: formData.get("valorX"),
        valorH: formData.get("valorH"),
    };
    
    try {
        const response = await fetch("/calcular", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        
        if (!response.ok) {
            throw new Error("Error en la solicitud");
        }
        
        const jsonRes = await response.json();
        const tbody = document.getElementById("tabla-resultados");
        tbody.innerHTML = ""; // Limpia las filas previas
        
        jsonRes.forEach(row => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${row.n}</td>
                <td>${row.xn}</td>
                <td>${row.yn}</td>
                <td>${row.yreal}</td>
                <td>${row.error}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error("Error:", error);
    }
});
