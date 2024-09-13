# commands.py

from discord.ext import commands
from database import execute_query

async def add_task(ctx, description: str):
    await execute_query("INSERT INTO tasks (task, completed) VALUES (?, ?)", (description, False))
    await ctx.send(f"Görev eklendi: {description}")

async def delete_task(ctx, task_id: int):
    result = await execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))
    if result.rowcount == 0:
        await ctx.send("Bu ID'ye sahip bir görev bulunamadı.")
    else:
        await ctx.send(f"Görev silindi: ID {task_id}")

async def show_tasks(ctx):
    tasks = await execute_query("SELECT id, task, completed FROM tasks", fetch=True)
    if not tasks:
        await ctx.send("Hiç görev yok.")
        return
    task_list = "\n".join([f"ID: {task[0]} - Görev: {task[1]} - Tamamlandı: {'Evet' if task[2] else 'Hayır'}" for task in tasks])
    await ctx.send(f"Görevler:\n{task_list}")

async def complete_task(ctx, task_id: int):

    result = await execute_query("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
    if result.rowcount == 0:
        await ctx.send(f"Bu ID'ye sahip bir görev bulunamadı: {task_id}")
    else:
        await ctx.send(f"Görev tamamlandı: ID {task_id}")

def setup_commands(bot: commands.Bot):
    bot.add_command(commands.Command(add_task, name="add_task"))
    bot.add_command(commands.Command(delete_task, name="delete_task"))
    bot.add_command(commands.Command(show_tasks, name="show_tasks"))
    bot.add_command(commands.Command(complete_task, name="complete_task"))
