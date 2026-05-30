from highrise import BaseBot, CurrencyItem, Item, Position, Reaction, SessionMetadata, User





class Bot(BaseBot):

    

    async def send(self, text: str):
        print(text)
        await self.highrise.chat(text)

    async def on_user_join(self, user: User, position: Position) -> None:
        await self.send(f"[JOIN   ] {user.username}")

    async def on_user_leave(self, user: User) -> None:
        await self.send(f"[LEAVE  ] {user.username}")

    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        pass

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.send("[START  ]")

    async def on_chat(self, user: User, message: str) -> None:
        await self.send(f"[CHAT   ] {user.username}: {message}")

    async def on_whisper(self, user: User, message: str) -> None:
        await self.send(f"[WHISPER] {user.username}: {message}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        receptor = receiver.username if receiver else "None"
        await self.send(f"[EMOTE  ] {user.username} {emote_id} {receptor}")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        await self.send(
            f"[REACTION] {user.username} {reaction} {receiver.username}"
        )

    async def on_tip(
        self, sender: User, receiver: User, tip: CurrencyItem | Item
    ) -> None:
        cantidad = getattr(tip, "amount", "?")
        tipo = getattr(tip, "type", type(tip).__name__)

        await self.send(
            f"[TIP    ] {sender.username} {receiver.username} {tipo} {cantidad}"
        )

    async def on_user_move(self, user: User, pos) -> None:
        try:
            text = f"[MOVE   ] {user.username} {pos.x} {pos.y} {pos.z}"
        except AttributeError:
            text = f"[MOVE   ] {user.username} {pos}"

        await self.send(text)




        