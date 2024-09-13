import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from commands import delete_task
from database import execute_query,create_table
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_setup_module():
    await create_table()


@pytest.mark.asyncio
async def test_delete_task():
    await execute_query("DELETE FROM tasks")
    
    await execute_query("INSERT INTO tasks (task, completed) VALUES (?, ?)", ("Test Görevi", False))
    
    deneme_ctx = AsyncMock()
    
    await delete_task(deneme_ctx, task_id=1)  
    
    tasks = await execute_query("SELECT * FROM tasks WHERE id = ?", (1,), fetch=True)
    assert len(tasks) == 0, "Görev silinmedi"
    
    