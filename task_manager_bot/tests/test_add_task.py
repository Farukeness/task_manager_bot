import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from commands import add_task
from database import execute_query,create_table
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_setup_module():
    await create_table()


@pytest.mark.asyncio
async def test_add_task():
    await execute_query("DELETE FROM tasks")

    deneme_ctx = AsyncMock()
    
    await add_task(deneme_ctx, description="Test Görevi")

    tasks = await execute_query("SELECT * FROM tasks WHERE task = ?", ("Test Görevi",), fetch=True)
    
    assert tasks is not None and len(tasks) > 0, "Görev veritabanına eklenmedi"
    assert tasks[0][1] == "Test Görevi", "Eklenen görev 'Test Görevi' değil"

