import discord
from kodlanddiscordbot1_logic import gen_pass
from kodlanddiscordbot1_logic import emoji
#gen_pass(10)
#hace contraseña

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Activa el privilegio de ver miembros
intents.members = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hemos iniciado sesión como {client.user}")

@client.event
async def on_member_join(member):  
   channel = client.get_channel(1146944130681950208) #Bot needs to be in this server with the channel btw 
   await channel.send(f"Buenas que {member.mention}, comete un ʖᔑᓵꖌ⎓ꖎ╎!¡")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("$hello"):
        await message.channel.send("Hi!")
    elif message.content.startswith("$bye"):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$cap"):
        await message.channel.send("Julien is capping (stop the cap 🧢) 🤫🧏‍♂️🗣️😁😀🗿🔒")
    elif message.content.startswith("$help"):
        await message.channel.send("Los comandos que se pueden usar son: \n 1. $hello (saludo) \n 2. $bye (despedida) \n 3. $cap (julian is cappin') \n 4. $help (este comando) \n 5. $emoji (emoji random) \n 6. $mewing (ya sabes que es esto) \n 7. $ginger (si pongo la palabra que es me banean) \n 8. $spam (para spam (max 222))" )
    elif message.content.startswith("$emoji"):
        await message.channel.send(emoji())
    elif message.content.startswith("$mewing"):
        await message.channel.send("🤫🧏‍♂️")
    elif message.content.startswith("$ginger"):
        await message.channel.send("⬛👨🏿")  
    elif  message.content.startswith('$spam'):
        if len(message.content) > 5:
            count_spam = int(message.content[5:])
        else:
            count_spam = 5
        await message.channel.send("buenasque" * count_spam)
#    else:
#        await message.channel.send("a")

client.run("hmm")
