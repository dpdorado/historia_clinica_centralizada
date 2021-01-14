# Sistema de gestión de historia clínica centralizada

Desarrollo de servicio web (API REST) qpara un sistema de gestión de historia clínica centralizada.

#
Requerimientos del proyecto:

1. Permitir registro de usuarios con Identificación, Email, Teléfono y contraseña.

Condiciones:

* Los tipos de usuario permitidos en registro son Hospital y Paciente.

2. Confirmación de registro por parte de usuario a través de uno de sus datos de contacto.

Condiciones:

* El usuario no podrá acceder al sistema hasta que confirme su registro.

3. Inicio de sesión de usuario utilizando Identificación y Contraseña.

4. Registro de datos básicos de usuario:

* Si el usuario es de tipo Hospital debe registrar: Nombre, Dirección, Servicios médicos que brinda.

* Si el usuario es de tipo paciente debe registrar: Nombre, Dirección, fecha de nacimiento.

5.Registro de usuario tipo Médico por parte de un usuario Hospital.

Condiciones:

* Condiciones similares al registro de los otros tipos de usuario.

* La primera vez que inicie sesión debe cambiar la contraseña y establecer una nueva contraseña.

6. Todos los usuarios deben cambiar y/o recuperar su contraseña cuando lo deseen.

7. Permitir a un usuario de Tipo Médico registrar observaciones médicas yestado de salud de un usuario de tipo Paciente.

Condiciones:

* Obligatorio indicar especialidad médicabrindada al Paciente

8. Cualquier usuario debe poder consultar todos los registros de observaciones médicas registradas. 

Condiciones: 

* Mostrar: hospital, médico, especialidad y detalle de cada registro asociado al paciente.

* Usuario Paciente, solo puede consultar sus registros.

* Usuario Médico, puede consultar registros realizados por él mismo.

* Usuario Hospital, puede consultar los registros realizados por sus Médicos.

9. Descargar archivo con todas las observaciones de un Paciente registradas en el sistema.Condiciones iguales al punto 7.

#
# Desempeño: 

La API permite realizar las siguientes funcionalidades comparadas con los requisitos: 

1. Registrar usuarios de tipo Hospital y Paciente.

2. No se implemento. Se quedo en el envio de correos; esta funcionalidad se reutiliza en el punto 6.

3. Se permite el inicio de sesión de los usuarios Hospital, Paciente y Médico con su usuario y contraseña devolviento un token de seguridad.

La contraseña de los usuarios se guarda encriptada para su seguridad.

4. Despues de haber registrado un usuario de tipo Hospital o Paciente la API permite hacer un registro de datos básicos según su tipo.

5. Despues de haber iniciado sesion con un usuario de tipo Hospital, se podrá realizar un registro de un usuario de tipo Médico.

6. No se implemento.

7. Permiti a un usuario de Tipo Médico registrar observaciones médicas y estado de salud de un usuario de tipo Paciente.

8. Permite a los usuarios consultar todos los registros de observaciones médicas registradas. 

* El Usuario Paciente,  puede consultar sus registros.

* El Usuario Médico, puede consultar registros realizados por él mismo.

* Usuario Hospital,.

9. No se implemento.

# 

> Las pruebas de ejecución de la API se pueden ver en la carpeta evidencias. Se utiliza el software Postman.



