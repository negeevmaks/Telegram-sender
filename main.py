from telethon import TelegramClient, events
from telethon.tl.types import InputFile

import config

import openpyxl
import asyncio

import datetime
import time


num = config.num_aks
clients_data = []

for i in range(1, num+1):
    clients_data.append(
        TelegramClient(
            getattr(config, f'phone_{i}'),
            getattr(config, f'api_id_{i}'),
            getattr(config, f'api_hash_{i}')
            )
        )

time_1 = [datetime.time(h, m).strftime('%H:%M') for h, m in [(8, 0), (8, 30), (9, 0), (9, 30), (10, 0), (10, 30), (11, 0), (11, 30),
                                                             (12, 0), (12, 30), (13, 0), (13, 30), (14, 0), (14, 30), (15, 0), (15, 30),
                                                             (16, 0), (16, 30), (17, 0), (17, 30), (18, 0), (18, 30), (19, 0), (19, 30), (20, 0),
                                                             (20, 30), (21, 0), (21, 30), (22, 0)]]
                                                             
time_2 = [datetime.time(h, m).strftime('%H:%M') for h, m in [(9, 20), (11, 20), (13, 20), (15, 20), (17, 20), (19, 20), (22, 20)]]
time_3 = datetime.time(10, 20).strftime('%H:%M')

def chech_excel(file):
    ws_input = openpyxl.load_workbook(file).active
    data_array = [row[0] for row in ws_input.iter_rows(values_only=True)]
    return data_array

file_1 = chech_excel('input_1.xlsx')
file_2 = chech_excel('input_2.xlsx')
file_3 = chech_excel('input_3.xlsx')

async def send_text(client, text, file, mesa, mass):
    temp = 0
    lead = len(mass)

    await client.start()

    for i in range(min(mesa, lead)):
        entity = await client.get_entity(mass[temp])

        try:
            if file:
                await client.send_message(entity, text, file=file)
            else:
                await client.send_message(entity, text)

            await asyncio.sleep(15)
            print(True)

        except Exception as e:
            print(False)
            print(mass[temp])
            print(e)

        temp += 1

    lead -= mesa
    await client.disconnect()

async def sen_message(senders):
    text_1, files_1 = senders[0]
    text_2, files_2 = senders[1]
    text_3, files_3 = senders[2]

    print('Program is running!')

    while True:
        current_time = datetime.datetime.now().time().strftime('%H:%M')

        if current_time in time_1:
            print('Start 1')
            await asyncio.gather(*(send_text(client, text_1, files_1, 15, file_1) for client in clients_data))
            print('End 1')

        if current_time in time_2:
            print('Start 2')
            await asyncio.gather(*(send_text(client, text_2, files_2, 10, file_2) for client in clients_data))
            print('End 2')

        if current_time == time_3:
            print('Start 3')
            await asyncio.gather(*(send_text(client, text_3, files_3, 10, file_3) for client in clients_data))
            print('End 3')

        await asyncio.sleep(66)

if __name__ == '__main__':
    asyncio.run(sen_message(config.data))