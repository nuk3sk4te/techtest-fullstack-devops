# Introducción
Esta es una aplicación web que consta de un backend en Python y un frontend en HTML/CSS. El backend maneja la lógica de la aplicación y el frontend sirve la interfaz de usuario. La aplicación permite a los usuarios interactuar con una base de datos de imágenes.

## Funcionalidades
- Backend en Python que maneja la lógica de la aplicación.
- Frontend en HTML/CSS servido por Nginx.
- Persistencia de datos utilizando volúmenes de Docker.

# Requisitos previos
Para ejecutar esta aplicación, necesitarás tener instalado el siguiente software:
- Docker
- Docker Compose

# Instrucciones de instalación y ejecución

## Ejecutar la aplicación en local con Docker
1. Clona el repositorio:
    ```sh
    git clone https://github.com/nuk3sk4te/techtest-fullstack-devops.git
    cd techtest-fullstack-devops
    ```

2. Construye y levanta los contenedores:
    ```sh
    docker-compose up --build
    ```

3. Accede a la aplicación:
    - Frontend: `http://localhost:8080`

# Pipeline CI/CD
El pipeline CI/CD está configurado para automatizar las siguientes acciones:
- **Build**: Construcción de las imágenes Docker para el backend y el frontend.
- **Test**: Ejecución de pruebas automatizadas para asegurar la calidad del código.
- **Deploy**: Despliegue automático de la aplicación en un entorno de producción.

## Descripción del pipeline
1. **Build**: Se construyen las imágenes Docker utilizando los Dockerfiles definidos.
2. **Test**: Se ejecutan pruebas unitarias y de integración.
3. **Deploy**: Se despliegan las imágenes Docker en el entorno de producción.

# Despliegue en la nube
## Configuración de la instancia
Para desplegar la aplicación en la nube, se ha utilizado una instancia de AWS EC2 con la siguiente configuración:
- Sistema operativo: Ubuntu 22.04
- Docker y Docker Compose instalados

## Justificación de las decisiones
- **AWS EC2**: Se eligió AWS EC2 por su flexibilidad y escalabilidad.
- **Docker**: Se utilizó Docker para asegurar la consistencia del entorno de ejecución y facilitar el despliegue en cualquier entorno ya sea en el equipo local del desarrollador o en un entorno cloud.


## UPDATE
- Hemos creado la infraestructura en un ECS, para desplegar los contenedores, utilando como repositorio de imagenes ECR y un pipeline de Github Actions para el despliegue de los contenedores en ECS.

Por falta de tiempo no hemos desplegado utilizando Terraform y hemos desplegado de manera automática con aws-cli algunos de los recursos: 

Resumen de comandos
1. Crear la definición de tarea:
   ```
    aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
2. Crear el clúster de ECS.
   ```
   aws ecs create-cluster --cluster-name techtest-fullstack-devops_cluster
   ```
3. Crear el servicio de ECS asociado a la task-definition creado anteriormente
    ```
    aws ecs create-service \
    --cluster techtest-fullstack-devops_cluster \
    --service-name techtest-fullstack-devops-service \
    --task-definition my-task \
    --desired-count 1 \
    --launch-type EC2 \
    --network-configuration "awsvpcConfiguration={subnets=[subnet-12345678],securityGroups=[sg-12345678],assignPublicIp=ENABLED}"
   ```
4. Modificar las variables de entorno del pipeline Github Actions.
Revisar la configuración en el directorio. 
   ```
   .github/workflows/aws.yml
   ```
5. Descripcion Github Actions Pipeline
# Deploy to Amazon ECS

Este workflow de GitHub Actions está configurado para desplegar una aplicación en Amazon ECS cada vez que se realiza un push a la rama `main`.

## Introducción

El workflow realiza las siguientes acciones:
1. Configura las credenciales de AWS.
2. Inicia sesión en Amazon ECR.
3. Construye, etiqueta y sube una imagen Docker a Amazon ECR.
4. Actualiza la definición de tarea de ECS con la nueva imagen.
5. Despliega la nueva definición de tarea en un servicio de ECS.

## Requisitos previos

Para ejecutar este workflow, necesitarás:
- Una cuenta de AWS con permisos para ECS, ECR y IAM.
- Un repositorio de ECR creado.
- Un clúster y servicio de ECS configurados.
- Configurar los secretos `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY` en tu repositorio de GitHub.

## Variables de entorno

El workflow utiliza las siguientes variables de entorno:

- `AWS_REGION`: La región de AWS donde se encuentra tu infraestructura (por ejemplo, `eu-south-2`).
- `ECR_REPOSITORY`: El nombre del repositorio de ECR (por ejemplo, `techtest-fullstack-devops`).
- `ECS_SERVICE`: El nombre del servicio de ECS (por ejemplo, `techtest-fullstack-devops-service`).
- `ECS_CLUSTER`: El nombre del clúster de ECS (por ejemplo, `techtest-fullstack-devops_cluster`).
- `ECS_TASK_DEFINITION`: La ruta al archivo de definición de tarea de ECS (por ejemplo, `frontend-techtest`).
- `CONTAINER_NAME`: El nombre del contenedor en la sección `containerDefinitions` de tu definición de tarea (por ejemplo, `my-docker-image`).

## Instrucciones de instalación y ejecución

1. Configura los secretos en GitHub:
    - Ve a tu repositorio en GitHub.
    - Haz clic en "Settings" (Configuración).
    - En el menú de la izquierda, selecciona "Secrets and variables" y luego "Actions".
    - Añade los secretos `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`.

2. Modifica las variables de entorno en el archivo de workflow `.github/workflows/aws.yml` según tu configuración.

3. Realiza un push a la rama `main` para activar el workflow:
    ```sh
    git add .
    git commit -m "Configurar despliegue a Amazon ECS"
    git push origin main
    ```

# Referencias externas utilizadas
- [Documentación de Docker](https://docs.docker.com/)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)
- [Guía de AWS EC2](https://docs.aws.amazon.com/ec2/)