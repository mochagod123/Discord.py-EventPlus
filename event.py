from discord.ext import commands
import discord
import traceback
import sys
import logging
import random
import time
import asyncio
import re
from functools import partial
import time

class EventPlusCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print(f"init -> EventPlusCog")

    @commands.Cog.listener("on_member_update")
    async def on_member_update_role(self, before: discord.Member, after: discord.Member):
        try:
            before_roles = set(before.roles)
            after_roles = set(after.roles)

            added_roles = after_roles - before_roles
            removed_roles = before_roles - after_roles

            if added_roles:
                self.bot.dispatch("on_member_role_add", before, after)

            if removed_roles:
                self.bot.dispatch("on_member_role_remove", before, after)
        except:
            return

    @commands.Cog.listener("on_interaction")
    async def on_interaction_button(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 2:
                self.bot.dispatch("on_interaction_button", interaction)
        except:
            return

    @commands.Cog.listener("on_interaction")
    async def on_interaction_select(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 3:
                self.bot.dispatch("on_interaction_select", interaction)
        except:
            return

    @commands.Cog.listener("on_interaction")
    async def on_interaction_select_user(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 5:
                self.bot.dispatch("on_interaction_select_user", interaction)
        except:
            return

    @commands.Cog.listener("on_interaction")
    async def on_interaction_select_role(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 6:
                self.bot.dispatch("on_interaction_select_role", interaction)
        except:
            return
        
    @commands.Cog.listener("on_interaction")
    async def on_interaction_select_mention(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 7:
                self.bot.dispatch("on_interaction_select_mention", interaction)
        except:
            return
        
    @commands.Cog.listener("on_interaction")
    async def on_interaction_select_channel(self, interaction: discord.Interaction):
        try:
            if interaction.data['component_type'] == 8:
                self.bot.dispatch("on_interaction_select_channel", interaction)
        except:
            return

async def setup(bot):
    await bot.add_cog(EventPlusCog(bot))