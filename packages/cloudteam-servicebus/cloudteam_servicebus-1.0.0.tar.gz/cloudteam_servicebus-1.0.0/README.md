# CloudTeam_ServiceBus

## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Functions](../function.md)

## About <a name = "about"></a>

This module is a service bus module for cloudteam to simplify sending messages and reciving

## Usage <a name = "usage"></a>

in you code write the following line:    
```
from cloudteam_servicebus import cloudteam_servicebus
sb = cloudteam_servicebus.ServiceBus(<Service bus host name>,<managed identity client id>, <Logger Object>)
sb.<WANTED FUNCTION>(<needed parameters>)
```

## Functions <a name = "function"></a>
- Send_BatchMessages(queue name,list of messages) - sending a batch of messages
- Send_Message(queue,message) - sending a message
- Recive_Message(queue,numer of messages - default 1) - reciving a number of messages.