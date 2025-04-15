async function AgregarPersona() {
    const nombre = document.getElementById("nombre").value
    const apellido = document.getElementById("apellido").value
    const dni = document.getElementById("dni").value
    const telefonosInput = document.getElementById("teléfonos").value
    const hijosInput = document.getElementById("nombre_hijos").value

    const telefonos = telefonosInput.split(",").map(t => t.trim())
    const hijos = hijosInput.split(",").map(h => h.trim())

    const persona = {nombre, apellido, dni, telefonos, hijos}

    await fetch("/agregar",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(persona)
    })

    document.getElementById("nombre").value = ""
    document.getElementById("apellido").value = ""
    document.getElementById("dni").value = ""
    document.getElementById("teléfonos").value = ""
    document.getElementById("nombre_hijos").value = ""
}

async function MostrarPersona() {
    const res = await fetch("/mostrar") 
    const data = await res.json()

    const resultado = document.getElementById("resultado")
    resultado.textContent = JSON.stringify(data, null, 2)
}

async function buscarPorDni() {
    const dni = document.getElementById("buscarDni").value
    const resultado = document.getElementById("resultadoBusqueda")
    
    const res = await fetch(`/buscar/${dni}`)
    const persona = await res.json()

    if (res.ok){
        resultado.textContent = 
       `Nombre: ${persona.Nombre} \nApellido: ${persona.Apellido}\nTelefonos:${persona.Telefonos} \nHijos: ${persona.Hijos}`
    }else{
        resultado.textContent = "No se encontro una persona con ese dni"
    }
}