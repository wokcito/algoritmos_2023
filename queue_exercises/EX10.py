"""Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:

a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, sin perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son."""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classQueue import Queue
from classStack import Stack

queue = Queue()
stack = Stack()

notifications = [
    {
        "app": "Facebook",
        "message": "¡Feliz cumpleaños! Esperamos que tengas un día increíble.",
        "hour": "09:30"
    },
    {
        "app": "Facebook",
        "message": "Tus amigos te han etiquetado en una foto.",
        "hour": "18:15"
    },
    {
        "app": "Twitter",
        "message": "¡Nuevo seguidor! @usuario te ha seguido.",
        "hour": "11:45"
    },
    {
        "app": "Twitter",
        "message": "Salió una nueva actualización de Python!.",
        "hour": "21:05"
    },
    {
        "app": "Twitter",
        "message": "Tu tweet ha sido retwitteado por @seguidor.",
        "hour": "14:20"
    },
    {
        "app": "Instagram",
        "message": "¡Tu publicación ha recibido 100 me gusta!",
        "hour": "16:45"
    },
    {
        "app": "WhatsApp",
        "message": "Tienes un nuevo mensaje de texto.",
        "hour": "09:55"
    },
    {
        "app": "Gmail",
        "message": "Nuevo correo electrónico: ¡Descubre las últimas ofertas!",
        "hour": "12:30"
    }
]

def fillQueue():
    while queue.size() > 0:
        queue.atention()

    for notification in notifications:
        queue.arrive(notification)

# A

def deleteNotifications(app):
    fillQueue()

    counter = 0

    while counter < queue.size():
        notification = queue.on_front()

        if app == notification["app"]:
            queue.atention()
        else:
            print(queue.move_to_end())
            counter += 1

deleteNotifications("Facebook")

# B

fillQueue()

counter = 0

while counter < queue.size():
    notification = queue.move_to_end()
    counter += 1

    if notification["app"].lower() == "twitter" and "python" in notification["message"].lower():
        print(notification)
        
# C

# Paso horas:minutos a minutos que pasaron en el día
# 11:43 y 15:57 - 703 y 957

def getMinutes(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)

def getNotificationByTime(min = "00:00", max = "00:00"):
    fillQueue()

    minTime = getMinutes(min)
    maxTime = 1440 if getMinutes(max) == 0 else getMinutes(max)

    while queue.size() > 0:
        notification = queue.atention()
        time = getMinutes(notification["hour"])

        if time >= minTime and time <= maxTime:
            stack.push(notification)
    
    print(f"Las notificaciones encontradas son {stack.size()}")

getNotificationByTime("11:43", "15:57")