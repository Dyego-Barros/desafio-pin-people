import pika
import json
import time
from dotenv import load_dotenv
from core.database import Database
from entities.entitie import Funcionario
from models.model import FuncionarioModel
import os
#Instância do banco
database = Database()

load_dotenv()

#Executa regra do worker
def callback(ch,method,properties, body):
    try:
        data = json.loads(body.decode("utf-8"))
        print("📥 Mensagem recebida:", data)
        
        #Processa os dados para enviar para IA
        
        if data.get("operacao") == "criar":
            
        
            campos=[
                FuncionarioModel.enps
            ]
            db = next(database.get_connection())
            dados = db.query(*campos).all()
            
            result = [{"enps":dado} for dado in dados]
            print(result)
            
        
    except Exception as error:
        print("❌ Erro ao processar:", error)
        # Não dá ack → Rabbit reentrega a mensagem depois
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        
def executa_worker():
    
    while True:
        try:
            print("🔌 Conectando ao RabbitMQ...")
            parametros = pika.URLParameters(os.environ.get("RABBIT_URL"))
            connection = pika.BlockingConnection(parameters=parametros)
            channel = connection.channel()
            
            channel.queue_declare(queue=os.environ.get("QUEUE_NAME"), durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=os.environ.get("QUEUE_NAME"), on_message_callback=callback)
            print(f"👂 Worker ativo! Escutando fila: {os.environ.get('QUEUE_NAME')}")
            channel.start_consuming()

        except pika.exceptions.AMQPConnectionError:
            print("⚠ Conexão perdida. Tentando reconectar em 5s...")
            time.sleep(5)
        except Exception as e:
            print("❌ Erro inesperado:", e)
            time.sleep(5)
            
if __name__ == "__main__":
    executa_worker()