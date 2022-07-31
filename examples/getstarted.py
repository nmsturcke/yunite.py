import yunite

client = yunite.YuniteClient(yunite_api_key="YOUR-API-KEY", fortnite_api_key="YOUR-API-KEY")

print(client.id)
print(client.name)
print(", ".join(guild.name for guild in client.guilds))