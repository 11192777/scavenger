from kafka import KafkaConsumer


class Consumer:
    def __init__(self):
        self.consumer = KafkaConsumer('toplog', bootstrap_servers=['192.168.2.215:9092'])

    def poll(self):
        res = self.consumer.poll()
        for message in self.consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, str(message.value, 'utf-8')))


if __name__ == '__main__':
    ll = '''
PID    COMMAND          %CPU TIME     #TH   #WQ #PORTS MEM   PURG  CMPRS PGRP  PPID  STATE    BOOSTS       %CPU_ME %CPU_OTHRS UID FAULTS   COW   MSGSENT    MSGRECV   SYSBSD    SYSMACH    CSW        PAGEINS IDLEW    POWER INSTRS CYCLES USER                  #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
'''
    for line in ll.splitlines():
        for item in line.split():
            print("                `{}`       varchar(255) NULL,".format(str(item).lower()))

    DBU
