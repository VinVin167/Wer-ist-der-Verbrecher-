from pathlib import Path
import sys

root = Path(sys.argv[1])

replacements = {
    "src/main/java/de/vincent/tvd/command/TvdCommands.java": [
        ('player.displayClientMessage(Component.literal(message), false);', 'player.sendSystemMessage(Component.literal(message));'),
        ('player.displayClientMessage(Component.literal("TVD-Status: " + status + time + blood), false);', 'player.sendSystemMessage(Component.literal("TVD-Status: " + status + time + blood));'),
    ],
    "src/main/java/de/vincent/tvd/vampire/VampireManager.java": [
        ('SoundEvents.GENERIC_DRINK,', 'SoundEvents.GENERIC_DRINK.value(),'),
        ('player.serverLevel().sendParticles(', '((net.minecraft.server.level.ServerLevel) player.level()).sendParticles('),
        ('player.displayClientMessage(Component.literal(message).withStyle(formatting), false);', 'player.sendSystemMessage(Component.literal(message).withStyle(formatting));'),
    ],
    "src/main/java/de/vincent/tvd/vampire/VampireEvents.java": [
        ('player.displayClientMessage(\n                        net.minecraft.network.chat.Component.literal(\n                                "Du bist noch im Übergang. Verbleibend: " + VampireManager.formatRemainingTime(player)\n                        ).withStyle(net.minecraft.ChatFormatting.RED),\n                        false\n                );', 'player.sendSystemMessage(\n                        net.minecraft.network.chat.Component.literal(\n                                "Du bist noch im Übergang. Verbleibend: " + VampireManager.formatRemainingTime(player)\n                        ).withStyle(net.minecraft.ChatFormatting.RED)\n                );'),
    ],
    "src/main/java/de/vincent/tvd/vampire/BloodManager.java": [
        ('player.displayClientMessage(Component.literal("Dein Blutvorrat wird knapp.").withStyle(ChatFormatting.RED), false);', 'player.sendSystemMessage(Component.literal("Dein Blutvorrat wird knapp.").withStyle(ChatFormatting.RED));'),
        ('player.displayClientMessage(Component.literal("Du bist fast vollständig ausgehungert.").withStyle(ChatFormatting.DARK_RED), false);', 'player.sendSystemMessage(Component.literal("Du bist fast vollständig ausgehungert.").withStyle(ChatFormatting.DARK_RED));'),
        ('player.displayClientMessage(Component.literal("Du bist ausgehungert. Trinke Menschenblut.").withStyle(ChatFormatting.DARK_RED), false);', 'player.sendSystemMessage(Component.literal("Du bist ausgehungert. Trinke Menschenblut.").withStyle(ChatFormatting.DARK_RED));'),
        ('ServerBossEvent created = new ServerBossEvent(\n                    Component.literal("Blut"),', 'ServerBossEvent created = new ServerBossEvent(\n                    UUID.randomUUID(),\n                    Component.literal("Blut"),'),
    ],
}

for relative, pairs in replacements.items():
    path = root / relative
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in text:
            raise RuntimeError(f"Expected source fragment missing in {relative}: {old[:80]}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
