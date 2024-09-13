import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from commands import show_tasks
from database import execute_query,create_table
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_setup_module():
    await create_table()

@pytest.mark.asyncio
async def test_show_tasks():
   
    await execute_query("DELETE FROM tasks")

    
    deneme_ctx = AsyncMock()
    await show_tasks(deneme_ctx)
    deneme_ctx.send.assert_called_once_with("Hiç görev yok.")    
    
    await execute_query("INSERT INTO tasks (task, completed) VALUES (?, ?)", ("Test Görevi 1", False))
    await execute_query("INSERT INTO tasks (task, completed) VALUES (?, ?)", ("Test Görevi 2", True))

    
    deneme_ctx.reset_mock()  
    await show_tasks(deneme_ctx)

    # Görev listesinin doğru şekilde gönderildiğini kontrol et
    expected_message = "Görevler:\nID: 1 - Görev: Test Görevi 1 - Tamamlandı: Hayır\nID: 2 - Görev: Test Görevi 2 - Tamamlandı: Evet"
    deneme_ctx.send.assert_called_once_with(expected_message)
    
    
    
    