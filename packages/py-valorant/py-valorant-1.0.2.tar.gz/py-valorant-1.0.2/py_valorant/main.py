from api import ValorantAPI,ValorantAPIAsync
import asyncio


xd = ValorantAPIAsync('en-US')
# asd = ValorantAPI('en-US')
async def main():
    # contracts = await xd.contract.fetch_all()
    # event = await xd.event.fetch_from_uuid('96682481-4f7b-6322-18bb-f1a76f91a35f')
    # agent = await xd.agent.fetch_from_uuid('e370fa57-4757-3604-3648-499e1f642d3f')
    # print(agent.display_name,agent.character_tags)
    # print(event.display_name)
    # for contract in contracts:
        # print(contract.display_name,contract.use_level_vp_cost_override)
    # gamemodes = await xd.gamemode.fetch_all()
    # for gamemode in gamemodes:
    #     print(gamemode.display_name,gamemode.duration_list,gamemode.duration_range,gamemode.duration)
    # gamemodes_equipables = await xd.gamemode_equipable.fetch_all()
    # for gamemode_equipable in gamemodes_equipables:
    #     print(gamemode_equipable.category,gamemode_equipable.display_name)
    # maps = await xd.map.fetch_all(cache=True)
    # print('done')
    # print(maps[0]==maps[0],maps[0]==maps[1])
    # maps = await xd.map.fetch_all(cache=True)
    # print('done')
    # print(maps[0]==maps[0],maps[0]==maps[1])
    # maps = await xd.map.fetch_all(cache=False)
    # print('done1')
    # print(maps[0]==maps[0],maps[0]==maps[1])
    # maps = await xd.map.fetch_all(cache=False)
    # print('done')
    # print(maps[0]==maps[0],maps[0]==maps[1])
    # maps = await xd.map.fetch_all(cache=False)
    # print('done')
    # print(maps[0]==maps[0],maps[0]==maps[1])
    # agents = await xd.agent.fetch_all(cache=True)
    # for agent in agents:
    #     print(agent.display_name)
    # agents2 = asd.agent.fetch_all(True,cache=True)
    # for agent in agents2:
    #     print(agent.display_name)
    # player_cards = await xd.player_card.fetch_all()
    # for player_card in player_cards:
    #     print(player_card.display_name,player_card.image.large_art)
    player_titles = await xd.player_title.fetch_all()
    for player_title in player_titles:
        print(player_title.display_name,player_title.asset_path)


try:
    asyncio.run(main())
except RuntimeError:
    print('closed')