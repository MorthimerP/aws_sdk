import boto3
from botocore.exceptions import NoCredentialsError

# Crear cliente S3
s3 = boto3.client('s3')

BUCKET_NAME = 'morthibucketsdk'


# 1. Subir archivo
def subir_archivo(ruta_local, nombre_s3):
    try:
        s3.upload_file(ruta_local, BUCKET_NAME, nombre_s3)
        print(f"Archivo '{ruta_local}' subido como '{nombre_s3}'")
    except FileNotFoundError:
        print("El archivo no existe")
    except NoCredentialsError:
        print("Credenciales no disponibles")


# 2. Listar archivos
def listar_archivos():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        if 'Contents' in response:
            print("Archivos en el bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print("El bucket está vacío")
    except Exception as e:
        print(f"Error al listar: {e}")


# 3. Descargar archivo
def descargar_archivo(nombre_s3, ruta_local):
    try:
        s3.download_file(BUCKET_NAME, nombre_s3, ruta_local)
        print(f"Archivo '{nombre_s3}' descargado en '{ruta_local}'")
    except Exception as e:
        print(f"Error al descargar: {e}")


# -------------------------
# Ejemplo de uso
# -------------------------
if __name__ == "__main__":
    # Subir
    subir_archivo("archivo_local.txt", "archivo_en_s3.txt")

    # Listar
    listar_archivos()

    # Descargar
    descargar_archivo("archivo_en_s3.txt", "descargado.txt")