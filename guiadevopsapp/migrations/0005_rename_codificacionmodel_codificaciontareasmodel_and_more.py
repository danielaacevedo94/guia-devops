# Generated by Django 5.0.6 on 2024-08-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiadevopsapp', '0004_codificacionherramientasmodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='codificacionModel',
            new_name='Codificaciontareasmodel',
        ),
        migrations.RenameModel(
            old_name='construccionModel',
            new_name='Construcciontareasmodel',
        ),
        migrations.RenameModel(
            old_name='operacionesModel',
            new_name='Desplieguetareasmodel',
        ),
        migrations.RenameModel(
            old_name='liberacionModel',
            new_name='Liberaciontareasmodel',
        ),
        migrations.RenameModel(
            old_name='monitoreoModel',
            new_name='Monitoreotareasmodel',
        ),
        migrations.RenameModel(
            old_name='despliegueModel',
            new_name='Operacionestareasmodel',
        ),
        migrations.RenameModel(
            old_name='planificacionModel',
            new_name='Planificaciontareasmodel',
        ),
        migrations.RenameModel(
            old_name='pruebasModel',
            new_name='Pruebastareasmodel',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS12',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS32',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS33',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS42',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS43',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS45',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS52',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS53',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS55',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS62',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS63',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7IS66',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM15',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM19',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM21',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM22',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM23',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM25',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM26',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM32',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM33',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM41',
        ),
        migrations.RemoveField(
            model_name='desplieguetareasmodel',
            name='task7PM42',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS12',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS32',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS33',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS42',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS43',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS45',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS52',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS53',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS55',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS62',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS63',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6IS66',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM15',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM19',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM21',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM22',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM23',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM25',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM26',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM32',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM33',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM41',
        ),
        migrations.RemoveField(
            model_name='operacionestareasmodel',
            name='task6PM42',
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS12',
            field=models.BooleanField(default=False, verbose_name='SI.1.2 Establecer o actualizar el entorno de implementación.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS32',
            field=models.BooleanField(default=False, verbose_name='SI.3.2 Comprender la especificación de requisitos.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS33',
            field=models.BooleanField(default=False, verbose_name='SI.3.3 Documentar o actualizar el Diseño del Software.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS42',
            field=models.BooleanField(default=False, verbose_name='SI.4.2 Comprender el diseño de software.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS43',
            field=models.BooleanField(default=False, verbose_name='SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS45',
            field=models.BooleanField(default=False, verbose_name='SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS52',
            field=models.BooleanField(default=False, verbose_name='SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS53',
            field=models.BooleanField(default=False, verbose_name='SI.5.3 Integra el Software mediante Componentes de Software.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS55',
            field=models.BooleanField(default=False, verbose_name='SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS62',
            field=models.BooleanField(default=False, verbose_name='SI.6.2 Comprender la configuración del software.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS63',
            field=models.BooleanField(default=False, verbose_name='SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6IS66',
            field=models.BooleanField(default=False, verbose_name='SI.6.6 Realizar la entrega según las Instrucciones de Entrega.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM15',
            field=models.BooleanField(default=False, verbose_name='PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM19',
            field=models.BooleanField(default=False, verbose_name='PM.1.9 Identificar los riesgos que puedan afectar el proyecto.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM21',
            field=models.BooleanField(default=False, verbose_name='PM.2.1 Registre los datos reales en el Registro de estado de progreso.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM22',
            field=models.BooleanField(default=False, verbose_name='PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM23',
            field=models.BooleanField(default=False, verbose_name='PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM25',
            field=models.BooleanField(default=False, verbose_name='PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM26',
            field=models.BooleanField(default=False, verbose_name='PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM32',
            field=models.BooleanField(default=False, verbose_name='PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM33',
            field=models.BooleanField(default=False, verbose_name='PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM41',
            field=models.BooleanField(default=False, verbose_name='PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.'),
        ),
        migrations.AddField(
            model_name='desplieguetareasmodel',
            name='task6PM42',
            field=models.BooleanField(default=False, verbose_name='PM.4.2 Actualizar el Repositorio de Proyectos.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS12',
            field=models.BooleanField(default=False, verbose_name='SI.1.2 Establecer o actualizar el entorno de implementación.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS32',
            field=models.BooleanField(default=False, verbose_name='SI.3.2 Comprender la especificación de requisitos.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS33',
            field=models.BooleanField(default=False, verbose_name='SI.3.3 Documentar o actualizar el Diseño del Software.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS42',
            field=models.BooleanField(default=False, verbose_name='SI.4.2 Comprender el diseño de software.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS43',
            field=models.BooleanField(default=False, verbose_name='SI.4.3 Construir o actualizar Componentes de Software con base en la parte detallada del Diseño de Software.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS45',
            field=models.BooleanField(default=False, verbose_name='SI.4.5 Corrija los defectos encontrados hasta que se logre una prueba unitaria exitosa (alcanzando los criterios de salida).'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS52',
            field=models.BooleanField(default=False, verbose_name='SI.5.2 Comprender los casos de prueba y los procedimientos de prueba. Establezca o actualice el entorno de prueba.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS53',
            field=models.BooleanField(default=False, verbose_name='SI.5.3 Integra el Software mediante Componentes de Software.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS55',
            field=models.BooleanField(default=False, verbose_name='SI.5.5 Corregir los defectos encontrados y realizar pruebas de regresión hasta alcanzar los criterios de salida.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS62',
            field=models.BooleanField(default=False, verbose_name='SI.6.2 Comprender la configuración del software.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS63',
            field=models.BooleanField(default=False, verbose_name='SI.6.3 Documentar la Documentación de Mantenimiento o actualizar la actual.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7IS66',
            field=models.BooleanField(default=False, verbose_name='SI.6.6 Realizar la entrega según las Instrucciones de Entrega.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM15',
            field=models.BooleanField(default=False, verbose_name='PM.1.5 Identificar los Recursos: humanos, materiales, equipos y herramientas, estándares, incluyendo la capacitación requerida del Equipo de Trabajo para realizar el proyecto. Incluya en el cronograma las fechas en las que se necesitarán recursos y capacitación.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM19',
            field=models.BooleanField(default=False, verbose_name='PM.1.9 Identificar los riesgos que puedan afectar el proyecto.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM21',
            field=models.BooleanField(default=False, verbose_name='PM.2.1 Registre los datos reales en el Registro de estado de progreso.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM22',
            field=models.BooleanField(default=False, verbose_name='PM.2.2 Analizar la Solicitud de Cambio en términos de costo, cronograma e impacto técnico.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM23',
            field=models.BooleanField(default=False, verbose_name='PM.2.3 Realizar reuniones de revisión con el Equipo de Trabajo, identificar problemas, revisar estado de riesgos, registrar acuerdos.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM25',
            field=models.BooleanField(default=False, verbose_name='PM.2.5 Realizar respaldo de acuerdo a la Estrategia de Control de Versiones.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM26',
            field=models.BooleanField(default=False, verbose_name='PM.2.6 Realizar la recuperación del Repositorio de Proyectos utilizando la Copia de Seguridad del Repositorio de Proyectos, si es necesario.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM32',
            field=models.BooleanField(default=False, verbose_name='PM.3.2 Identificar riesgos relacionados con el cumplimiento del plan, según sea necesario, documentarlos en el Registro de Corrección.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM33',
            field=models.BooleanField(default=False, verbose_name='PM.3.3 Identificar cambios a los requisitos y/o Plan del Proyecto para abordar desviaciones importantes, riesgos potenciales o problemas relacionados con el cumplimiento del plan, documentarlos en Solicitud de Cambio.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM41',
            field=models.BooleanField(default=False, verbose_name='PM.4.1 Formalizar la finalización del proyecto de acuerdo con las Instrucciones de Entrega establecidas en el Plan de Proyecto, brindando soporte de aceptación y firma del Acta de Aceptación.'),
        ),
        migrations.AddField(
            model_name='operacionestareasmodel',
            name='task7PM42',
            field=models.BooleanField(default=False, verbose_name='PM.4.2 Actualizar el Repositorio de Proyectos.'),
        ),
    ]
