# api_minecraft_flash
JSON EXAMPLE
{
"name": "Zombie Horse",
"type": "Unused mob",
"java": "false",
"bedrock": "false",
"education": "false",
"img": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/46/ZombieHorseFace.png/revision/latest/scale-to-width-down/64?cb=20200223042320",
"wiki_url": "https://minecraft.gamepedia.com/Zombie_Horse"
}

TEST API
https://minecraft-api-utch.herokuapp.com/test

WIKI MINECRAFT
https://minecraft-api-utch.herokuapp.com/api_minecraft/wiki

GET ALL MOBS
https://minecraft-api-utch.herokuapp.com/api_minecraft/mobs/

GET ONE MOB
https://minecraft-api-utch.herokuapp.com/api_minecraft/mob/{name}

NEW MOB
https://minecraft-api-utch.herokuapp.com/api_minecraft/new_mob/{token}

UPDATE A MOB
https://minecraft-api-utch.herokuapp.com/api_minecraft/mobs/update/{name}/{token}
	NEED A JSON

DELETE A MOB
https://minecraft-api-utch.herokuapp.com/api_minecraft/mobs/del/{name}/{token}

WRITE A MOB NAME WITH A SPACE IN A URL
Replace de space with a %20, for example:
https://minecraft-api-utch.herokuapp.com/api_minecraft/mobs/update/Beast%20Boy/{token}
