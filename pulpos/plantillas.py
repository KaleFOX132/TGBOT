from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_start = """<b><a href="tg://resolve?domain=AbigailRexBot">ᴀʙɪɢᴀɪʟ • [ 🌻 ]</a>          <code>⎚ {hora}</code>

⎚ Estado         <code> {estado}</code>
⎚ ID                  <code> {user_id} </code> 
⎚ Alias                <code>AbigailRexBot</code>
⎚ Version          <code>1.4</code>
━━━━━━━━━━━━━
⎚ Fecha            <code>{tiempo}</code> 
⎚ Create           <b><a href="tg://resolve?domain=RexAwait">𝗿𝗲𝘅 hᴀᴡᴀɪɪ |「💻」</a></b>
</b>
"""


_cmd = """<b><b><a href="tg://resolve?domain=RexAwait">List comand ☁️</a></b>

⎚ GaterWays                   <code>8</code>
⎚ status                          <code>ON ✅</code>
━━━━━━━━━
⎚Tools                             <code>14</code>
⎚ status                          <code>ON ✅</code></b>
━━━━━━━━━
</b>
"""

_cmdbotons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "Gates",
                            callback_data="gates"
                        ),
                        InlineKeyboardButton(
                            "Tools",
                            callback_data="tools"
                        ),
                    ],
                    [
                        InlineKeyboardButton( 
                            "Canal",
                            url="https://t.me/AbigailRexChannel"),
                        InlineKeyboardButton( 
                            "Grupo",
                            url="https://t.me/+JpjrNHZEeS9lODc5"
                        ),
                    ],
                ]
            )

_Call_Gateways = """<b> <b><a href="tg://resolve?domain=">Gates | Gateway 🌑</a></b>

⎚ Chill | Stripe Charge <code>[FREE]</code>
⎚ Usar <code>/str card</code> On [ ✅ ]
━━━━━━━━━
⎚ Xilisio | Stripe Auth <code>[FREE]</code>
⎚ Usar <code>/xi card</code> On [ ✅ ]
━━━━━━━━━
⎚ Mass | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/mass cards</code> On [ ✅ ]
━━━━━━━━━
⎚ Alga | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/cr card</code> On [ ✅ ]
━━━━━━━━━
⎚ Yupi | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/yu card</code> OFF [ x ]
━━━━━━━━━
⎚ Abigail | Stripe Charge <code>[PTRMIUM]</code>
⎚ Usar <code>/br card</code> On [ ✅ ]
━━━━━━━━━
⎚ AsteKa | Stripe Charge <code>[PTRMIUM]</code>
⎚ Usar <code>/az card</code> On [ ✅ ]
━━━━━━━━━
</b>"""

_Call_Tools = """<b><b> <b><a href="tg://resolve?domain=">Herramientas | Tools 🌑</a></b>

⎚ Bin - <code>FREE</code>
⎚ Usar <code>/bin 456789</code>
━━━━━━━━━
⎚ Gen Ccs - <code>FREE</code>
⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code> 
━━━━━━━━━
⎚ Gen Mass Ccs <code>FREE</code>
⎚ Usar <code>/genmass 456789|rnd|rnd|rnd</code>
━━━━━━━━━
⎚ Extra <code>FREE</code>
⎚ Usar <code>/extra 456789|rnd|rnd|rnd</code>
━━━━━━━━━
⎚ Pasty <code>PREMIUM</code>
⎚ Usar <code>/paster texto a subir a pasti</code>
━━━━━━━━━
⎚ Code img <code>PREMIUM</code>
⎚ Usar <code>/code texto a subir a Imagen code</code>
━━━━━━━━━
⎚ Ip - <code>FREE</code>
⎚ Usar <code>/ip 1.1.1.1</code>
━━━━━━━━━
⎚ Tu informacion - <code>FREE</code>
⎚ Usar <code>/info </code>
━━━━━━━━━
⎚ Info Del bot user - <code>FREE</code>
⎚ Usar <code>/me</code>
━━━━━━━━━
⎚ Rand - <code>FREE</code>
⎚ Usar <code>/rand </code> 
━━━━━━━━━
⎚ Rand Pais - <code>PREMIUM</code>
⎚ Usar <code>/rdn ar</code>
━━━━━━━━━
⎚ Zip code Postal - <code>FREE</code>
⎚ Usar <code>/zip 10020</code>
━━━━━━━━━
</b>"""

_Call_Gateways_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Atras ",
                    callback_data="home"
                ),
                InlineKeyboardButton(
                    "Cerrar",
                    callback_data="exit"
                ),
        ]
        ]
    )
