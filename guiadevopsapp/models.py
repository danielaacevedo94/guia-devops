"""Aquí se definen los modelos de la base de datos que se van a utilizar en la aplicación"""
from datetime import datetime
from django.db import models
from django.utils import timezone


# pylint: disable=missing-class-docstring
class Usuariomodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    tipoEmpresa = models.TextField()
    numeroEmpleados = models.IntegerField()
    numeroProyectos = models.IntegerField()
    class Meta:
        get_latest_by = ['fecha']

# Modelo de la tabla Planificacion
class Planificaciontareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    task1PM11 = models.BooleanField(default=False, verbose_name="PM.1.1 Revisar la Declaración de Trabajo.")
    task1PM12 = models.BooleanField(default=False, verbose_name="PM.1.2 Definir con el Cliente las Instrucciones de Entrega de cada uno de los Entregables especificados en la Declaración de Trabajo.")
    task1PM13 = models.BooleanField(default=False, verbose_name="PM.1.3 Identificar las Tareas específicas a realizar para producir los Entregables y sus Componentes de Software identificados en la Declaración de Trabajo. Incluir Tareas en el proceso SI junto con verificación, validación y revisiones con Tareas del Cliente y del Equipo de Trabajo para asegurar la calidad de los productos de trabajo. Identificar las Tareas para realizar las Instrucciones de Entrega. Documente las tareas.")
    task1PM14 = models.BooleanField(default=False, verbose_name="PM.1.4 Establecer la Duración Estimada para realizar cada tarea.")
    task1PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar y documentar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task1PM16 = models.BooleanField(default=False, verbose_name="PM.1.6 Establecer la Composición del Equipo de Trabajo asignando roles y responsabilidades de acuerdo a los Recursos.")
    task1PM17 = models.BooleanField(default=False, verbose_name="PM.1.7 Asignar fechas estimadas de inicio y finalización de cada una de las Tareas para crear el Cronograma de las Tareas del Proyecto teniendo en cuenta los Recursos asignados, secuencia y dependencia de las Tareas.")
    task1PM18 = models.BooleanField(default=False, verbose_name="PM.1.8 Calcular y documentar el Esfuerzo y Costo Estimado del proyecto.")
    task1PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar y documentar los riesgos que puedan afectar el proyecto.")
    task1PM110 = models.BooleanField(default=False, verbose_name="PM.1.10 Documentar la Estrategia de Control de Versiones en el Plan del Proyecto.")
    task1PM111 = models.BooleanField(default=False, verbose_name="PM.1.11 Generar el Plan del Proyecto integrando los elementos previamente identificados y documentados.")
    task1PM112 = models.BooleanField(default=False, verbose_name="PM.1.12 Incluir descripción del producto, alcance, objetivos y entregables en el plan del proyecto.")
    task1PM113 = models.BooleanField(default=False, verbose_name="PM.1.13 Verificar y obtener la aprobación del Plan del Proyecto.")
    task1PM114 = models.BooleanField(default=False, verbose_name="PM.1.14 Revisar y aceptar el Plan del Proyecto.")
    task1PM115 = models.BooleanField(default=False, verbose_name="PM.1.15 Establecer el Repositorio de Proyectos utilizando la Estrategia de Control de Versiones.")
    task1PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task1PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar y evaluar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task1PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task1PM24 = models.BooleanField(default=False, verbose_name="PM.2.4 Realizar reuniones de revisión con el Cliente, registrar acuerdos.")
    task1PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task1PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task1PM31 = models.BooleanField(default=False, verbose_name="PM.3.1 Evaluar el progreso del proyecto con respecto al Plan del Proyecto, comparando: - Tareas reales con las Tareas planificadas - Resultados reales con los Objetivos establecidos del proyecto - Asignación de recursos reales con los Recursos planificados - Costo real con las estimaciones presupuestarias - Tiempo real con el cronograma planificado - Riesgo real contra previamente identificado.")
    task1PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Establecer acciones para corregir desviaciones o problemas y riesgos identificados relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task1PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task1PM41 = models.BooleanField(default=False, verbose_name="PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.")
    task1PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task1IS11 = models.BooleanField(default=False, verbose_name="SI.1.1 Revisión del Plan de Proyecto vigente con los miembros del Equipo de Trabajo para lograr un entendimiento común y lograr su compromiso con el proyecto.")
    task1IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task1IS21 = models.BooleanField(default=False, verbose_name="SI.2.1 Asignar Tareas a los miembros del Equipo de Trabajo de acuerdo con su rol, con base en el Plan de Proyecto vigente.")
    task1IS22 = models.BooleanField(default=False, verbose_name="SI.2.2 Documentar o actualizar la Especificación de Requisitos.")
    task1IS23 = models.BooleanField(default=False, verbose_name="SI.2.3 Verificar y obtener la aprobación de la Especificación de Requisitos.")
    task1IS24 = models.BooleanField(default=False, verbose_name="SI.2.4 Validar y obtener aprobación de la Especificación de Requisitos")
    task1IS25 = models.BooleanField(default=False, verbose_name="SI.2.5 Documentar la versión preliminar de la *Documentación de Usuario del Software o actualizar el presente manual, si corresponde. *(Opcional)")
    task1IS26 = models.BooleanField(default=False, verbose_name="SI.2.6 Verificar y obtener aprobación de la *Documentación del Usuario del Software, en su caso. *(Opcional)")
    task1IS27 = models.BooleanField(default=False, verbose_name="SI.2.7 Incorporar la Especificación de Requisitos y la *Documentación de Usuario del Software a la Configuración del Software en la línea base. *(Opcional)")
    task1IS31 = models.BooleanField(default=False, verbose_name="SI.3.1 Asignar Tareas a los miembros del Equipo de Trabajo relacionadas con su rol de acuerdo al Plan de Proyecto vigente.")
    task1IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task1IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task1IS34 = models.BooleanField(default=False, verbose_name="SI.3.4 Verificar y obtener aprobación del Diseño de Software.")
    task1IS35 = models.BooleanField(default=False, verbose_name="SI.3.5 Establecer o actualizar Casos de Prueba y Procedimientos de Prueba para pruebas de integración basados ​​en la Especificación de Requisitos y el Diseño de Software. El cliente proporciona datos de prueba, si es necesario.")
    task1IS36 = models.BooleanField(default=False, verbose_name="SI.3.6 Verificar y obtener aprobación de los Casos de Prueba y Procedimientos de Prueba.")
    task1IS37 = models.BooleanField(default=False, verbose_name="SI.3.7 Actualizar el Registro de Trazabilidad incorporando los Casos de Prueba y Procedimientos de Prueba.")
    task1IS38 = models.BooleanField(default=False, verbose_name="SI.3.8 Incorporar el Diseño del Software y Registro de Trazabilidad a la Configuración del Software como parte de la línea base. Incorporar los Casos de Prueba y Procedimientos de Prueba al Repositorio de Proyectos.")
    task1IS41 = models.BooleanField(default=False, verbose_name="SI.4.1 Asignar Tareas a los miembros del Equipo de Trabajo relacionadas con su rol, de acuerdo al Plan de Proyecto vigente.")
    task1IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task1IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task1IS44 = models.BooleanField(default=False, verbose_name="SI.4.4 Diseñar o actualizar casos de prueba unitarios.")
    task1IS46 = models.BooleanField(default=False, verbose_name="SI.4.6 Actualizar el Registro de Trazabilidad incorporando Componentes de Software construidos o modificados.")
    task1IS47 = models.BooleanField(default=False, verbose_name="SI.4.7 Incorporar Componentes de Software y Registro de Trazabilidad a la Configuración del Software como parte de la línea base.")
    task1IS51 = models.BooleanField(default=False, verbose_name="SI.5.1 Asignar Tareas a los miembros del equipo de trabajo relacionadas con su rol, de acuerdo al Plan de Proyecto vigente.")
    task1IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task1IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Actualiza casos de prueba y procedimientos de prueba para pruebas de integración, según sea necesario.")
    task1IS56 = models.BooleanField(default=False, verbose_name="SI.5.6 Actualiza el Registro de Trazabilidad, si corresponde.")
    task1IS57 = models.BooleanField(default=False, verbose_name="SI.5.7 Documentar la *Guía de Operación del Producto o actualizar la guía actual, si corresponde. *(Opcional)")
    task1IS58 = models.BooleanField(default=False, verbose_name="SI.5.8 Verificar y obtener aprobación de la *Guía de Operación del Producto, si corresponde (ver SI.5.7)")
    task1IS59 = models.BooleanField(default=False, verbose_name="SI.5.9 Documentar la *Documentación de Usuario del Software o actualizar la actual, si corresponde. *(Opcional)")
    task1IS510 = models.BooleanField(default=False, verbose_name="SI.5.10 Verificar y obtener aprobación de la *Documentación del Usuario del Software, si corresponde (ver SI.5.9)")
    task1IS511 = models.BooleanField(default=False, verbose_name="SI.5.11 Incorporar los Casos de Prueba y Procedimientos de Prueba, Software, Registro de Trazabilidad, Informe de Prueba, *Guía de Operación del Producto y *Documentación del Usuario del Software a la Configuración del Software como parte de la línea base. *(Opcional)")
    task1IS61 = models.BooleanField(default=False, verbose_name="SI.6.1 Asignar Tareas a los miembros del equipo de trabajo relacionadas con su rol, de acuerdo al Plan de Proyecto vigente.")
    task1IS62 = models.BooleanField(default=False, verbose_name="SI.6.2 Comprender la configuración del software.")
    task1IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    task1IS64 = models.BooleanField(default=False, verbose_name="SI.6.4 Verificar y obtener la aprobación de la Documentación de Mantenimiento.")
    task1IS65 = models.BooleanField(default=False, verbose_name="SI.6.5 Incorporar la Documentación de Mantenimiento como base para la Configuración del Software.")
    class Meta:
        get_latest_by = ['fecha']

class Planificacionherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolGT = models.BooleanField(default=False, verbose_name="Gestión de Tareas (GitLab, Jira software, ClickUP, Bitrix24, Assana, Trello)")
    class Meta:
        get_latest_by = ['fecha']


class Codificaciontareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    task2PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task2PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task2PM110 = models.BooleanField(default=False, verbose_name="PM.1.10 Documentar la Estrategia de Control de Versiones en el Plan del Proyecto.")
    task2PM115 = models.BooleanField(default=False, verbose_name="PM.1.15 Establecer el Repositorio de Proyectos utilizando la Estrategia de Control de Versiones.")
    task2PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task2PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task2PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task2PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task2PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task2PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task2PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task2PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task2IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task2IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task2IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task2IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task2IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task2IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task2IS47 = models.BooleanField(default=False, verbose_name="SI.4.7 Incorporar Componentes de Software y Registro de Trazabilidad a la Configuración del Software como parte de la línea base.")
    task2IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task2IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task2IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task2IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    class Meta:
        get_latest_by = ['fecha']
    
class Codificacionherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolCV = models.BooleanField(default=False, verbose_name="Control de Versiones (Git, GitHub, GitLab, Mercurial, Subversion (SVN), BitBucket Atlassian)")
    toolIDE = models.BooleanField(default=False, verbose_name="Entorno de Desarrollo Integrado (IDE) (Visual Studio Code, Eclipse, NetBeans, Android Studio)")
    class Meta:
        get_latest_by = ['fecha']

class Construcciontareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task3PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task3PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task3PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task3PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task3PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task3PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task3PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task3PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task3PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task3PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task3IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task3IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task3IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task3IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task3IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task3IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task3IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task3IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    class Meta:
        get_latest_by = ['fecha']

class Construccionherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolCE = models.BooleanField(default=False, verbose_name="Compilación o empaquetado (Maven, Gradle, Apache Ant, Make, Webpack, CMake, MSBuild)")
    class Meta:
        get_latest_by = ['fecha']

class Pruebastareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task4PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task4PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task4PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task4PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task4PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task4PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task4PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task4PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task4PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task4PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task4IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task4IS23 = models.BooleanField(default=False, verbose_name="SI.2.3 Verificar y obtener la aprobación de la Especificación de Requisitos.")
    task4IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task4IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task4IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task4IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task4IS44 = models.BooleanField(default=False, verbose_name="SI.4.4 Aplicar los casos de pruebas unitarias para verificar que los Componentes de Software implementen la parte detallada del Diseño de Software.")
    task4IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task4IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task4IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task4IS54 = models.BooleanField(default=False, verbose_name="SI.5.4 Realice pruebas de software utilizando casos de prueba y procedimientos de prueba para la integración y documente los resultados en el informe de prueba.")
    task4IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task4IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    class Meta:
        get_latest_by = ['fecha']

class Pruebasherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolA = models.BooleanField(default=False, verbose_name="Automatización (Selenium, Jasmine, Karma, Appium, Postman, Robot Framework)")
    toolCP = models.BooleanField(default=False, verbose_name="Creación de Pruebas (PyTest, Junit, NUnit, TestNG, Cucumber, Jasmine, Robot Framework, Appium, Postman)")
    toolAEC = models.BooleanField(default=False, verbose_name="Análisis estático de código (ESLint, Pylint, RuboCop, Stylelint, Flake8, SonarQube)")
    toolPU = models.BooleanField(default=False, verbose_name="Pruebas Unitarias (JUnit, NUnit, TestNG, PyTest, Jasmine, Karma)")
    toolPI = models.BooleanField(default=False, verbose_name="Pruebas de Integración (PyTest, TestNG, Postman, Appium, Robot Framework)")
    toolPR = models.BooleanField(default=False, verbose_name="Pruebas de Regresión (JUnit, TestNG)")
    class Meta:
        get_latest_by = ['fecha']

class Liberaciontareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task5PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task5PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task5PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task5PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task5PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task5PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task5PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task5PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task5PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task5PM41 = models.BooleanField(default=False, verbose_name="PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.")
    task5PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task5IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task5IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task5IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task5IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task5IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task5IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task5IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task5IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task5IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task5IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    class Meta:
        get_latest_by = ['fecha']

class Liberacionherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolCI = models.BooleanField(default=False, verbose_name="Integración Continua (Jenkins, Travis CI, CircleCI, GitLab CI, Atlassian Bamboo, CodeShip, BitBucket Cloud Atlassian, Puppet Pipelines for Applications)")
    toolGA = models.BooleanField(default=False, verbose_name="Gestión de Artefactos (Sonatype Nexus Repository, JFrog Artifactory, GitHub Packages, AWS CodeArtifact)")
    class Meta:
        get_latest_by = ['fecha']

class Desplieguetareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task6PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task6PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task6PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task6PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task6PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task6PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task6PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task6PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task6PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task6PM41 = models.BooleanField(default=False, verbose_name="PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.")
    task6PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task6IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task6IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task6IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task6IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task6IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task6IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task6IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task6IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task6IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task6IS62 = models.BooleanField(default=False, verbose_name="SI.6.2 Comprender la configuración del software.")
    task6IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    task6IS66 = models.BooleanField(default=False, verbose_name="SI.6.6 Realizar la entrega según las Instrucciones de Entrega.")
    class Meta:
        get_latest_by = ['fecha']
    
class Despliegueherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolCD = models.BooleanField(default=False, verbose_name="Despliegue Continuo (GitLab, CodeShip, BitBucket Pipelines, Puppet Pipelines for Applications, Atlassian Bamboo, AWS OpsWorks)")
    toolGC = models.BooleanField(default=False, verbose_name="Gestión de la Configuración (Ansible, Puppet, Chef, AWS Opsworks, SaltStack)")
    toolIaC = models.BooleanField(default=False, verbose_name="Infraestructura como Código (Chef, Terraform, Ansible, Pulumi, AWS CloudFormation, Azure ARM Templates, Google Cloud Deployment Manager)")
    toolC = models.BooleanField(default=False, verbose_name="Contenedorización (Docker, Podman)")
    toolSN = models.BooleanField(default=False, verbose_name="Servicios en la Nube (Heroku, Microsoft Azure, AWS, Google Cloud Platform, Oracle Cloud, OpenShift)")
    class Meta:
        get_latest_by = ['fecha']

class Operacionestareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task7PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task7PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task7PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Registre los datos reales en el Registro de estado de progreso.")
    task7PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task7PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.")
    task7PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task7PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task7PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.")
    task7PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.")
    task7PM41 = models.BooleanField(default=False, verbose_name="PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.")
    task7PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task7IS12 = models.BooleanField(default=False, verbose_name="SI.1.2 Establecer o actualizar el entorno de implementación.")
    task7IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task7IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task7IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task7IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task7IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task7IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task7IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task7IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task7IS62 = models.BooleanField(default=False, verbose_name="SI.6.2 Comprender la configuración del software.")
    task7IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    task7IS66 = models.BooleanField(default=False, verbose_name="SI.6.6 Realizar la entrega según las Instrucciones de Entrega.")
    class Meta:
        get_latest_by = ['fecha']

class Operacionesherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolOC = models.BooleanField(default=False, verbose_name="Orquestación de Contenedores (Kubernetes, MESOSPHERE DC/OS, Docker Enterprise (Swarm))")
    toolGC = models.BooleanField(default=False, verbose_name="Gestión de la Configuración (Ansible, Puppet, Chef, AWS Opsworks, SaltStack)")
    toolIaC = models.BooleanField(default=False, verbose_name="Infraestructura como Código (Chef, Terraform, Ansible, Pulumi, AWS CloudFormation, Azure ARM Templates, Google Cloud Deployment Manager)")
    toolGS = models.BooleanField(default=False, verbose_name="Gestión de Servicios (Atlassian Jira Service Management)")
    toolGI = models.BooleanField(default=False, verbose_name="Gestión de Incidentes (Atlassian Jira Service Management, BigPanda, VictorOps, PagerDuty, OpsGenie)")
    class Meta:
        get_latest_by = ['fecha']
    
class Monitoreotareasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)

    task8PM15 = models.BooleanField(default=False, verbose_name="PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.")
    task8PM19 = models.BooleanField(default=False, verbose_name="PM.1.9 Identificar los riesgos que puedan afectar el proyecto.")
    task8PM21 = models.BooleanField(default=False, verbose_name="PM.2.1 Monitoree la ejecución del plan del proyecto y registre los datos reales en el Registro de estado de progreso.")
    task8PM22 = models.BooleanField(default=False, verbose_name="PM.2.2 Analizar y evaluar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.")
    task8PM23 = models.BooleanField(default=False, verbose_name="PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos y seguirlos hasta el cierre.")
    task8PM24 = models.BooleanField(default=False, verbose_name="PM.2.4 Seguir hasta el cierre los problemas y riesgos identificados junto a los acuerdos realizados provenientes de las reuniones realizadas.")
    task8PM25 = models.BooleanField(default=False, verbose_name="PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.")
    task8PM26 = models.BooleanField(default=False, verbose_name="PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.")
    task8PM31 = models.BooleanField(default=False, verbose_name="PM.3.1 Evaluar el avance del proyecto con respecto al Plan del Proyecto, comparando: - Tareas reales frente a tareas planificadas - resultados reales frente a los objetivos establecidos del proyecto - asignación de recursos reales frente a los recursos planificados - costo real frente a estimaciones presupuestarias - tiempo real frente al cronograma planificado - riesgo real frente a los previamente identificados.")
    task8PM32 = models.BooleanField(default=False, verbose_name="PM.3.2 Establecer acciones para corregir desviaciones o problemas y riesgos identificados relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección y darles seguimiento hasta su cierre.")
    task8PM33 = models.BooleanField(default=False, verbose_name="PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio y darles seguimiento hasta su cierre.")
    task8PM41 = models.BooleanField(default=False, verbose_name="PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.")
    task8PM42 = models.BooleanField(default=False, verbose_name="PM.4.2 Actualizar el Repositorio de Proyectos.")
    task8IS23 = models.BooleanField(default=False, verbose_name="SI.2.3 Verificar y obtener la aprobación de la Especificación de Requisitos.")
    task8IS32 = models.BooleanField(default=False, verbose_name="SI.3.2 Comprender la especificación de requisitos.")
    task8IS33 = models.BooleanField(default=False, verbose_name="SI.3.3 Documentar o actualizar el Diseño del Software.")
    task8IS42 = models.BooleanField(default=False, verbose_name="SI.4.2 Comprender el diseño de software.")
    task8IS43 = models.BooleanField(default=False, verbose_name="SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.")
    task8IS44 = models.BooleanField(default=False, verbose_name="SI.4.4 Aplicar los casos de pruebas unitarias para verificar que los Componentes de Software implementen la parte detallada del Diseño de Software.")
    task8IS45 = models.BooleanField(default=False, verbose_name="SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).")
    task8IS52 = models.BooleanField(default=False, verbose_name="SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.")
    task8IS53 = models.BooleanField(default=False, verbose_name="SI.5.3 Integra el Software mediante Componentes de Software.")
    task8IS54 = models.BooleanField(default=False, verbose_name="SI.5.4 Realice pruebas de software utilizando casos de prueba y procedimientos de prueba para la integración y documente los resultados en el informe de prueba.")
    task8IS55 = models.BooleanField(default=False, verbose_name="SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.")
    task8IS62 = models.BooleanField(default=False, verbose_name="SI.6.2 Comprender la configuración del software.")
    task8IS63 = models.BooleanField(default=False, verbose_name="SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.")
    class Meta:
        get_latest_by = ['fecha']

class Monitoreoherramientasmodel(models.Model):
    userId = models.TextField()
    fecha = models.DateTimeField(default=datetime.now)
    toolMR = models.BooleanField(default=False, verbose_name="Monitoreo de Redes (ManageEngine OpManager, Nagios, New Relic, Microsoft SCOM, Sensu, DataDog, ExtraHop, SignalFX, SumoLogic)")
    toolAD = models.BooleanField(default=False, verbose_name="Análisis de Datos (ManageEngine OpManager , Splunk, ELK Stack, New Relic, Microsoft SCOM, DataDog, SignalFX, SumoLogic)")
    toolGL = models.BooleanField(default=False, verbose_name="Gestión de Logs (ManageEngine OpManager , Splunk, ELK Stack, New Relic, Microsoft SCOM, SumoLogic, Scalyr, Loggly)")
    toolAPM = models.BooleanField(default=False, verbose_name="Monitoreo de Aplicaciones (New Relic, Microsoft SCOM, Sensu, DataDog, ExtraHop, SignalFX, Dynatrace, AppDynamics)")
    toolUXM = models.BooleanField(default=False, verbose_name="Monitoreo de Experiencia de Usuario (ManageEngine OpManager, New Relic, ExtraHop, Dynatrace, AppDynamics)")
    class Meta:
        get_latest_by = ['fecha']
