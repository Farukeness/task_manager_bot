import aiosqlite

async def create_table():
    async with aiosqlite.connect("tasks.db") as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY,task TEXT, completed BOOLEAN)"
        )
        await db.commit()

async def execute_query(query, params=(), fetch=False):
    async with aiosqlite.connect("tasks.db") as db:
        async with db.execute(query, params) as cursor:
            if fetch:
                result = await cursor.fetchall()
                return result
            await db.commit()
            return cursor  

