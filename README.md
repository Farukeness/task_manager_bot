Küçük ekiplerde görevleri yönetmeye yardımcı olacak bir Discord botu.
Bot, görev ekleme, silme ve görüntüleme yeteneğine sahip.
Ayrıca bot, görevleri tamamlanmış olarak işaretleyebiliyor.
Tüm veriler bir SQLite veritabanında saklanıyor.
------------------------------------------------ÖZELLİKLER--------------------------------------------
- **!add_task <description>** — Açıklaması `<description>` olan bir görev ekler.
- **!delete_task <task_id>** — `<task_id>` tanımlayıcısına sahip görevi siler.
- **!show_tasks** — Tüm görevlerin bir listesini gösterir.
- **!complete_task <task_id>** — `<task_id>` tanımlayıcısına sahip görevi tamamlandı olarak işaretler.

Projenin çalışması için aşağıdaki bağımlılıkları kurmanız gerekir. Tüm bağımlılıkları "requirements" dosyasından yükleyebilirsiniz:

pip install -r requirements.txt
