import logging
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

from calculate_func import beancan_grenades, satchels, explosive_ammos, \
    rockets, c4s

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

config = {
    'token': TOKEN,
    'prefix': '!',
}

bot = commands.Bot(
    command_prefix=config['prefix'],
    intents=intents,
    help_command=None
)

CURRENT_VERSION = '1.2'
CURRENT_UPDATE = """
Мне добавили возможность помочь вам научиться лутать рт, введите команду !rt
"""

HELP_COMMAND = """
!help (!h) - вывести список всех команд
!update (!up) - прочитать обновление бота
!radtown (!rt) - вывести список команд, как лутать рт

Посчитать ресурсы:
!beancan_grenade [количество] (!b [количество]) - для бобовок
!satchel [количество] (!s [количество]) - для сачелей
!explosive_ammo [количество] (!e [количество]) - для разрывных патрон
!rocket [количество] (!r [количество]) - для ракет
!c4 [количество] (!c [количество]) - для С4

Узнать сколько взрывчатки требуется на какой-либо объект:
!cost

Узнать сколько ресурсов требуется на застройку:
!furnace (!f) - для печки

Автор:
MorphEngine69, GitHub: https://github.com/MorphEngine69/RustCalculatorBot
Telegram: https://t.me/unsafe00

:sos: Внимание! Количество разрывных патрон могут разниться в меньшую сторону.
Для объекта указано количество патрон для  100% уничтожения,
патроны имеют свойство наносить разный урон постройке, например:
первая пуля в МВК стену нанесет 2 урона, вторая пуля может нанести 3.
"""


@bot.event
async def on_ready():
    """Функция для отображения активности бота."""
    logging.info('Активность для бота присвоена')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='!help'))


@bot.command(aliases=['h'])
async def help(ctx):
    """Отправка сообщения со всеми доступными командами."""
    logging.info(f'Использована команда !help пользователем - '
                 f'{ctx.message.author.nick}')
    embed = discord.Embed(
        title='Rust Helper',
        description=CURRENT_VERSION,
        color=0x3498DB,
    )
    embed.set_thumbnail(
        url='https://img.icons8.com/doodle/256/rust.png'
    )
    embed.add_field(
        name='Список команд:',
        value=HELP_COMMAND,
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['up'])
async def update(ctx):
    """Отправка сообщения с текущими обновлениями бота."""
    logging.info(f'Использована команда !update пользователем - '
                 f'{ctx.message.author.nick}')

    embed = discord.Embed(
        title='Текущая версия:',
        description=CURRENT_VERSION,
        color=0xad1457,
    )
    embed.set_thumbnail(
        url='https://img.icons8.com/doodle/256/rust.png'
    )
    embed.add_field(
        name='Последние изменения:',
        value=CURRENT_UPDATE
    )
    await ctx.send(embed=embed)
    # await ctx.reply(f'Текущая версия: {CURRENT_VERSION} {CURRENT_UPDATE}')


@bot.command(aliases=['b'])
async def beancan_grenade(ctx, amount):
    """Отправка сообщения с готовыми расчетами из beancan_grenades."""
    logging.info(f'Использована команда !beancan_grenade пользователем - '
                 f'{ctx.message.author.nick}')
    try:
        grenade = beancan_grenades(int(amount))
        embed = discord.Embed(
            title='Бобовые гранаты',
            url='https://rust.fandom.com/wiki/Beancan_Grenade',
            color=0x2ECC71
        )
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/play-rust/images/b/be/Beancan_Grenade_icon.png'
        )
        embed.add_field(
            name='Количество:',
            value=amount,
            inline=False
        )
        embed.add_field(
            name='Пороха:',
            value=grenade['total_gunpowder'],
            inline=True
        )
        embed.add_field(
            name='Металла:',
            value=grenade['total_metall'],
            inline=True
        )
        embed.add_field(
            name='Угля:',
            value=grenade['total_charcoal'],
            inline=False)
        embed.add_field(
            name='Общее количество серы:',
            value=grenade['total_sulfur'],
            inline=False
        )
        await ctx.reply(embed=embed)
    except ValueError:
        await ctx.reply('Введите количество!')


@bot.command(aliases=['s'])
async def satchel(ctx, amount):
    """Отправка сообщения с готовыми расчетами из satchels."""
    logging.info(f'Использована команда !satchel пользователем - '
                 f'{ctx.message.author.nick}')
    try:
        satchel_charge = satchels(int(amount))
        embed = discord.Embed(
            title='Сачели',
            url='https://rust.fandom.com/wiki/Satchel_Charge',
            color=0x3498DB
        )
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/play-rust/images/b/ba/Satchel_Charge_icon-0.png'
        )
        embed.add_field(
            name='Количество:',
            value=amount,
            inline=False
        )
        embed.add_field(
            name='Бобовых гранат:',
            value=satchel_charge['total_grenades'],
            inline=True
        )
        embed.add_field(
            name='Стэшей:',
            value=satchel_charge['total_stash'],
            inline=True
        )
        embed.add_field(
            name='Веревок:',
            value=satchel_charge['total_rope'],
            inline=True
        )
        embed.add_field(
            name='Пороха:',
            value=satchel_charge['total_gunpowder']['total_gunpowder'],
            inline=True
        )
        embed.add_field(
            name='Металла:',
            value=satchel_charge['total_gunpowder']['total_metall'],
            inline=True
        )
        embed.add_field(
            name='Угля:',
            value=satchel_charge['total_gunpowder']['total_charcoal'],
            inline=True
        )
        embed.add_field(
            name='Общее количество серы:',
            value=satchel_charge['total_gunpowder']['total_sulfur'],
            inline=False
        )

        await ctx.reply(embed=embed)
    except ValueError:
        await ctx.reply('Введите количество!')


@bot.command(aliases=['e'])
async def explosive_ammo(ctx, amount):
    """Отправка сообщения с готовыми расчетами из explosive_ammos."""
    logging.info(f'Использована команда !explosive_ammo пользователем - '
                 f'{ctx.message.author.nick}')
    try:
        ammo = explosive_ammos(int(amount) / 2)
        embed = discord.Embed(
            title='Разрывные патроны',
            url='https://rust.fandom.com/wiki/Explosive_5.56_Rifle_Ammo',
            color=0x9B59B6
        )
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/play-rust/images/3/31/Explosive_5.56_Rifle_Ammo_icon.png'
        )
        embed.add_field(
            name='Количество:',
            value=amount,
            inline=False
        )
        embed.add_field(
            name='Пороха:',
            value=int(ammo['total_gunpowder']),
            inline=True
        )
        embed.add_field(
            name='Металла:',
            value=int(ammo['total_metall']),
            inline=True
        )
        embed.add_field(
            name='Угля:',
            value=int(ammo['total_charcoal']),
            inline=False
        )
        embed.add_field(
            name='Общее количество cеры:',
            value=int(ammo['total_sulfur']),
            inline=False
        )
        await ctx.reply(embed=embed)
    except ValueError:
        await ctx.reply('Введите количество!')


@bot.command(aliases=['r'])
async def rocket(ctx, amount):
    """Отправка сообщения с готовыми расчетами из rockets."""
    logging.info(f'Использована команда !rocket пользователем - '
                 f'{ctx.message.author.nick}')
    try:
        rocket_charge = rockets(int(amount))
        embed = discord.Embed(
            title='Ракеты',
            url='https://rust.fandom.com/wiki/Rocket',
            color=0xED4245
        )
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/play-rust/images/9/95/Rocket_icon.png'
        )
        embed.add_field(
            name='Количество:',
            value=amount,
            inline=False
        )
        embed.add_field(
            name='Пороха:',
            value=rocket_charge['gunpowder_for_rocket'],
            inline=True
        )
        embed.add_field(
            name='Эксплозива:',
            value=rocket_charge['total_explosive'],
            inline=True
        )
        embed.add_field(
            name='Труб:',
            value=rocket_charge['total_pipe'],
            inline=True
        )
        embed.add_field(
            name='Металла:',
            value=rocket_charge['total_metall'],
            inline=True
        )
        embed.add_field(
            name='Топлива:',
            value=rocket_charge['total_fuel'],
            inline=True
        )
        embed.add_field(
            name='Угля:',
            value=rocket_charge['total_charcoal'],
            inline=True
        )
        embed.add_field(
            name='Общее количество пороха:',
            value=rocket_charge['total_gunpowder'],
            inline=True
        )
        embed.add_field(
            name='Общее количество cеры:',
            value=rocket_charge['total_sulfur'],
            inline=True
        )
        await ctx.reply(embed=embed)
    except ValueError:
        await ctx.reply('Введите количество!')


@bot.command(aliases=['c'])
async def c4(ctx, amount):
    """Отправка сообщения с готовыми расчетами из c4s."""
    logging.info(f'Использована команда !c4 пользователем - '
                 f'{ctx.message.author.nick}')
    try:
        c4_charge = c4s(int(amount))
        embed = discord.Embed(
            title='C4',
            url='https://rust.fandom.com/wiki/Timed_Explosive_Charge',
            color=0xFEE75C
        )
        embed.set_thumbnail(
            url='https://static.wikia.nocookie.net/play-rust/images/6/6c/Timed_Explosive_Charge_icon.png')
        embed.add_field(
            name='Количество:',
            value=amount,
            inline=False
        )
        embed.add_field(
            name='Эксплозива:',
            value=c4_charge['total_explosive'],
            inline=True
        )
        embed.add_field(
            name='Ткани:',
            value=c4_charge['total_cloth'],
            inline=True
        )
        embed.add_field(
            name='Микросхемы:',
            value=c4_charge['total_tech_trash'],
            inline=True
        )
        embed.add_field(
            name='Пороха:',
            value=c4_charge['total_gunpowder'],
            inline=True
        )
        embed.add_field(
            name='Металла:',
            value=c4_charge['total_metall'],
            inline=True
        )
        embed.add_field(
            name='Топлива:',
            value=c4_charge['total_fuel'],
            inline=True
        )
        embed.add_field(
            name='Угля:',
            value=c4_charge['total_charcoal'],
            inline=False
        )
        embed.add_field(
            name='Общее количество серы:',
            value=c4_charge['total_sulfur'],
            inline=False
        )
        await ctx.reply(embed=embed)
    except ValueError:
        await ctx.reply('Введите количество!')


@bot.command(aliases=['rt'])
async def radtown(ctx):
    """Отправка сообщения с доступными командами."""
    logging.info(f'Использована команда !radtown пользователем - '
                 f'{ctx.message.author.nick}')
    message = """ !satellite (!sa) - Спутниковые тарелки
    !small_harbor (!sh) - Маленький порт
    !large_harbor (!lh) - Большой порт
    !sewer_branch (!sb) - Канализационный отвод\n
    !water_treatment (!wt) - Отчистые сооружения
    !airfield (!ai) - Аэропорт
    !power_plant (!pp) - Электростанция
    !train_yard (!ty) - Депо
    !artic_base (!ab) - Арктическая база
    
    Где можно получить:
    :blue_circle: Синюю карту:
    Спутниковые тарелки, порт, канализационный отвод.
    :red_circle: Красную карту:
    Отчистные сооружения, аэропорт, электростанция, депо, арктическая база. 
    """

    embed = discord.Embed(
        title='Rust Helper',
        description=CURRENT_VERSION,
        color=0x2ecc71,
    )
    embed.set_thumbnail(
        url='https://img.icons8.com/doodle/256/rust.png'
    )
    embed.add_field(
        name='Список команд:',
        value=message
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['sa'])
async def satellite(ctx):
    """Отправка сообщения, как лутать Спутниковые тарелки."""
    logging.info(f'Использована команда !satellite пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая карта, фьюз.
    Что можно получить: синяя карта.
    1) Найти контейнер [1], вставить фьюз, зайти за контейнер и найти рычаг.
    2) Найти контейнер [2] и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/satellite/1.png'))


@bot.command(aliases=['sh'])
async def small_harbor(ctx):
    """Отправка сообщения, как лутать Маленький порт."""
    logging.info(f'Использована команда !small_harbor пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая карта, фьюз.
    Что можно получить: синяя карта.
    1) Найти контейнер [1], вставить фьюз и активировать рычаг.
    2) Подняться на второй этаж и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/small_harbor/1.png'))


@bot.command(aliases=['lh'])
async def large_harbor(ctx):
    """Отправка сообщения, как лутать Большой порт."""
    logging.info(f'Использована команда !large_harbor пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая карта, фьюз.
    Что можно получить: синяя карта.
    1) Найти контейнер [1], вставить фьюз, выйти из контейнера и найти снаружи 
    рычаг.
    2) Зайти в ангар [2] и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/large_harbor/1.png'))


@bot.command(aliases=['sb'])
async def sewer_branch(ctx):
    """Отправка сообщения, как лутать Канализационный отвод."""
    logging.info(f'Использована команда !sewer_branch пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая карта, фьюз.
    Что можно получить: синяя карта.
    1) Найти дом [1], вставить фьюз и слева найти рычаг.
    2) Спуститься в туннель [2] и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/sewer_branch/1.png'))


@bot.command(aliases=['wt'])
async def water_treatment(ctx):
    """Отправка сообщения, как лутать Водоотчистные сооружения."""
    logging.info(f'Использована команда !water_treatment пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: синяя карта, фьюз.
    Что можно получить: красная карта.
    1) Найти дом [1], с помощью вентиля открыть ворота, подняться на второй 
    этаж, вставить фьюз и активировать рычаг.
    2) Зайти в ангар [2] и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/water_treatment/1.png'))


@bot.command(aliases=['ai'])
async def airfield(ctx):
    """Отправка сообщения, как лутать Аэропорт."""
    logging.info(f'Использована команда !airfield пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая и синяя карта, 2 фьюза.
    Что можно получить: красная карта.
    1) Найти офис [1], в левой части (со стороны ангаров) найти комнату, 
    вставить фьюз и активировать таймер(действует: 2:10).
    2) Спуститься в туннель [2] между ангарами 2 и 3 и активировать зеленую 
    карту.
    3) Справа вставить фьюз и активировать синюю карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/airfield/1.png'))


@bot.command(aliases=['pp'])
async def power_plant(ctx):
    """Отправка сообщения, как лутать Электростанцию."""
    logging.info(f'Использована команда !power_plant пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая и синяя карта, фьюз.
    Что можно получить: красная карта.
    1) Найти трехэтажный дом [1], подняться на второй этаж и под лестницей 
    найти рычаг.
    2) Найти дом [2], активировать рычаг и таймер(действует: 1:05).
    3) Найти трехэтажный дом [3] в центре и активировать зеленую карту.
    4) На первом этаже, в правой части дома, со стороны ворот, найти рычаг на 
    приборах и активировать.
    5) Подняться на третий этаж, вставить фьюз справа от двери и активировать 
    синюю карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/power_plant/1.png'))


@bot.command(aliases=['ty'])
async def train_yard(ctx):
    """Отправка сообщения, как лутать Депо."""
    logging.info(f'Использована команда !train_yard пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: зеленая(по желанию) и синяя карта, фьюз.
    Что можно получить: красная карта.
    1) Найти трехэтажный дом [1], подняться на второй этаж и активировать 
    рычаг.
    2) Найти вышку [2], подняться на последний этаж и на балконе 
    активировать рычаг.
    3) Найти здание [3], подняться на второй этаж, вставить фьюз и 
    активировать рычаг.
    4) Подняться на третий или четвертый этаж и активировать нужную карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/train_yard/1.png'))


@bot.command(aliases=['ab'])
async def artic_base(ctx):
    """Отправка сообщения, как лутать Арктическую базу."""
    logging.info(f'Использована команда !artic_base пользователем - '
                 f'{ctx.message.author.nick}')
    message = """
    Что потребуется: синяя карта.
    Что можно получить: красная карта.
    1) Найти гараж [1] и активировать карту.
    """

    await ctx.send(message, file=discord.File(
        'image/radtowns/artic_base/1.png'))


@bot.command()
async def cost(ctx):
    """Отправка сообщения с таблицей сколько взрывчатки нужно на объект."""
    logging.info(f'Использована команда !cost пользователем - '
                 f'{ctx.message.author.nick}')
    image_list = [
        discord.File('image/cost1.png'),
        discord.File('image/cost2.png'),
    ]

    await ctx.reply(files=image_list)
    # await ctx.reply(file=discord.File('image/cost1.png'))
    # await ctx.reply(file=discord.File('image/cost2.png'))


@bot.command(aliases=['f'])
async def furnace(ctx):
    """Отправка сообщения сколько ресурсов потребуется на печь"""
    logging.info(f'Использована команда !furnace пользователем - '
                 f'{ctx.message.author.nick}')
    embed = discord.Embed(
        title='Застройка печки',
        color=0x3498DB,
    )
    embed.add_field(name='Дерево', value=1438, inline=True)
    embed.add_field(name='Камень', value=6825, inline=True)
    embed.add_field(name='Металл', value=600, inline=True)
    embed.set_image(url='https://i.ytimg.com/vi/zE0QSZGG60Y/maxresdefault.jpg')
    await ctx.reply(embed=embed)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(
                os.path.abspath('main.log'), mode='a', encoding='UTF-8'),
            logging.StreamHandler(stream=sys.stdout)],
        format='%(asctime)s, %(levelname)s, %(funcName)s, '
               '%(lineno)s, %(name)s, %(message)s'
    )
    try:
        logging.info('Бот успешно запущен!')
        bot.run(config['token'])
    except ConnectionError:
        logging.critical('Возникли проблемы с запуском бота')
        print('Возникли проблемы с запуском бота')
