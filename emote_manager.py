from highrise import User

EMOTE_MAP = {
    "relaxing": "😴 se acuesta relajadamente.",
    "rest": "🛋️ toma un descanso.",
    "ghost": "👻 se convierte en fantasma.",
    "dance": "💃 comienza a bailar.",
    "laugh": "😂 se ríe sin parar.",
    "wave": "👋 saluda a todos.",
}


async def handle_emote_command(bot, user: User, message: str) -> bool:

    msg = message.lower().strip()

    if msg in EMOTE_MAP:

        accion = EMOTE_MAP[msg]

        # Mensaje para toda la sala
        await bot.highrise.chat(
            f"🎭 {user.username} {accion}"
        )

        # Mensaje privado al usuario
        await bot.highrise.send_whisper(
            user.id,
            f"Comando detectado: {msg}"
        )

        return True

    return False