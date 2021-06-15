
# techlingo.fyi

 > ¿Qué significa esto?  

¿Alguna vez te has encontrado con una palabra o acrónimo que **no** sabes lo que significa? *TechLingo.fyi* está aquí para ayudarte a encontrar el significado.  

## Contribuyendo  
Hay dos formas de contribuir nuevos términos, puedes crear un nuevo [*issue*](https://github.com/fferegrino/techlingo.fyi/issues/new/choose) en GitHub o si quieres meterle mano al sistema por tu cuenta, revisa la sección de [desarrollo](#desarrollo).

## Desarrollo  
TechLingo está hecho usando **Python 3** con **pelican** como generador de sitios estáticos.  

Para comenzar, instala los requerimientos delineados en `requirements.txt` (preferentemente en un entorno virtual).

A partir de aquí puedes hacer dos cosas: 

### Agregar nuevas funcionalidades  
Ya debes tener todo listo para modificar el código fuente.

### Agregar nuevos términos  
Para hacer esto, debes modificar los archivos dentro de la carpeta `lingos`, una vez que hayas editado estos archivos, ejecuta `make fmt` antes de subir tus cambios.

### Ejecutar en un servidor local  
Ejecuta `make run` y visita `http://localhost:8000`.
