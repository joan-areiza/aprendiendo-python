import clases

persona = clases.Persona()
persona.setNombres("Carlos")
persona.setApellidos("Perez")
persona.setAltura("170cm")
persona.setEdad("40 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("--------------------------------------------------------------")

informatico = clases.Informatico()
informatico.setNombres("Juan")
informatico.setApellidos("Garcia")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("--------------------------------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombres("Raul")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())
print("--------------------------------------------------------------")
