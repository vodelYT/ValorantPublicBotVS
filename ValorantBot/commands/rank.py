from util import methods, sql
import discord


async def rank(ctx, rank, bot):
    if ctx.channel == methods.get_channel_commands(bot):
        if rank is not None:
            if type(rank) == discord.role.Role:
                dcUser = ctx.author
                if any(ext in rank.name for ext in methods.valid_roles):
                    role = rank

                    if sql.user_exists(dcUser.id):
                        await methods.set_rank(dcUser, role)
                        await ctx.send("Your rank has been updated.")
                    else:
                        await ctx.send("You have to register first.")
                else:
                    await ctx.send("You can't give yourself this role.")
            else:
              await ctx.send("You have to mention this role with @")
        else:
            await ctx.send("You have to enter a rank.")
    else:
        await methods.get_channel_support(bot).send(content=ctx.author.mention + " you can't use this command here, got to " + methods.get_channel_commands(bot), delete_after=30)
        await ctx.channel.purge(limit=1)


