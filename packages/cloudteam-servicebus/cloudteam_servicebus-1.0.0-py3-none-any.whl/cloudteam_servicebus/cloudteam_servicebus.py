from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import ManagedIdentityCredential
from cloudteam_logger import cloudteam_logger


class ServiceBus:
    def __init__(self,ServiceBusHostName,ClientId,LoggerObj: cloudteam_logger.ct_logging):
        """
        The function initializes a ServiceBusClient with the provided ServiceBusHostName and ClientId, along
        with a LoggerObj for logging purposes.
        
        :param ServiceBusHostName: ServiceBusHostName is the fully qualified namespace of the Azure Service
        Bus instance that you want to connect to. This typically looks like
        "{yournamespace}.servicebus.windows.net"
        :param ClientId: The `ClientId` parameter in the `__init__` method is typically used to specify the
        client ID for authentication purposes. In this case, it is being used to create a
        `ManagedIdentityCredential` object for authentication when interacting with the Service Bus client.
        The client ID is a unique identifier associated
        :param LoggerObj: The `LoggerObj` parameter in the `__init__` method is an instance of the
        `cloudteam_logger.ct_logging` class. This parameter is used to pass a logging object to the class
        constructor, which can be used for logging messages and errors within the class methods
        :type LoggerObj: cloudteam_logger.ct_logging
        """
        cred = ManagedIdentityCredential(Client_id = ClientId)
        self.client = ServiceBusClient(fully_qualified_namespace = ServiceBusHostName, credential = cred)
        self.logger = LoggerObj

    
    def Send_BatchMessages(self,queueName,messageList):
        """
        The function `sendBatchMessages` sends a batch of messages to a specified queue using the Azure
        Service Bus client.
        
        :param queueName: The `queueName` parameter is the name of the queue to which the messages will be
        sent. A queue is a storage location where messages are held until they can be processed by a
        receiver
        :param messageList: The `messageList` parameter is a list of messages that you want to send in a
        batch. Each message in the list should be a string or a dictionary that can be converted to a string
        """
        sender = self.client.get_queue_sender(queueName)
        batch = sender.create_message_batch()
        for message in messageList:
            try:
                batch.add_message(ServiceBusMessage(message))
            except ValueError as e:
                self.logger.error(f'Unable to add message to batch: {e}')
        try: 
            sender.send_messages(batch)
        except Exception as e:
            self.logger.error(f'Unable to send batch messages: {e}')
            return
        self.logger.info("sent batch message successfuly")
        


    def Send_Message(self,queueName,message):
        """
        The function `SendMessage` sends a message to a specified queue using the Azure Service Bus client.
        
        :param queueName: The `queueName` parameter is the name of the queue to which you want to send the
        message. It is a string that identifies the specific queue in the service bus
        :param message: The `message` parameter is the content of the message that you want to send to the
        specified queue. It can be a string or any other data type that can be serialized into a string
        :return: a boolean value. If the message is successfully sent, it will return True. If there is an
        exception or error during the sending process, it will return False.
        """
        sender = self.client.get_queue_sender(queueName)
        messageobj = ServiceBusMessage(message)
        with sender:
            try:
                sender.send_messages(messageobj)
            except Exception as e:
                self.logger.error(f'Unable to send message: {e}')
        self.logger.info("message sent successfuly")
    
    def Recive_Message(self,queueName,numberOfMessages=1):
        """
        The `reciveMessage` function receives a specified number of messages from a queue and returns them
        as a list.
        
        :param queueName: The `queueName` parameter is the name of the queue from which you want to receive
        messages. It is a string that identifies the specific queue you want to receive messages from
        :param numberOfMessages: The `numberOfMessages` parameter specifies the maximum number of messages
        to receive from the queue
        :return: a list of messages received from the specified queue.
        """
        receiver = self.client.get_queue_receiver(queueName)
        messagelist = []
        with receiver:
            try:
                messages = receiver.receive_messages(max_message_count=numberOfMessages, max_wait_time=5)
                for message in messages:
                    messagelist.append(str(message))
                    receiver.complete_message(message)
                return messagelist
            except Exception as e:
                self.logger.error(f'Unable to recive message: {e}')
        self.logger.info("Recived message successfuly")



