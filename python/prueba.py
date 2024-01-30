#!/usr/bin/python3
import re

#IMPORTANTE -> Agregar PLAY RECAP como end marker

def extract_task_output(input_text, task_name):
    start_marker = f"TASK [{task_name}]"
    end_marker = "TASK ["

    start_index = input_text.find(start_marker)
    end_index = input_text.find(end_marker, start_index + len(start_marker))

    if start_index != -1 and end_index != -1:
        extracted_text = input_text[start_index:end_index].strip()
        return extracted_text
    else:
        return None


# Ejemplo de uso
input_text = """
PLAY [Comprobar acceso a Plesk y dominio] **************************************

TASK [Gathering Facts] *********************************************************
ok: [192.190.43.17]

TASK [Comprobar acceso a Plesk] ************************************************
ok: [192.190.43.17]

TASK [Comprobar el estado de la URL "tucartomancia.com"] ***********************
ok: [192.190.43.17]

TASK [Chequeo de puertos] ******************************************************
ok: [192.190.43.17] => (item=80)
ok: [192.190.43.17] => (item=443)
ok: [192.190.43.17] => (item=8443)
failed: [192.190.43.17] (item=8447) => {"ansible_loop_var": "item", "changed": false, "elapsed": 5, "item": 8447, "msg": "Timeout when waiting for 192.190.43.17:8447"}
ok: [192.190.43.17] => (item=53)
...ignoring

TASK [Comprobar espacio en disco] **********************************************
changed: [192.190.43.17]

TASK [Mostrar resultados de la comprobación de espacio en disco] ***************
ok: [192.190.43.17] => {
    "msg": "/dev/vda1       983G  7.2G  926G   1% /"
}

TASK [Copiar archivo de plantilla resolv.conf (8.8.8.8 y 8.8.4.4)] *************
ok: [192.190.43.17]

TASK [Rendimiento web - Check First time response (Pensar que otras añadir comprobables desde la terminal)] ***
changed: [192.190.43.17]

TASK [Mostrar resultados del rendimiento web y Plesk] **************************
ok: [192.190.43.17] => {
    "msg": "Tiempo de conexión: 0.231666 segundos"
}

PLAY RECAP *********************************************************************
192.190.43.17              : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1
"""

task_name_to_extract = "Mostrar resultados del rendimiento web y Plesk"
output = extract_task_output(input_text, task_name_to_extract)

if output is not None:
    print(output)
else:
    print(f"No se encontró la tarea: {task_name_to_extract}")

