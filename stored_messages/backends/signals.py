from django.dispatch import Signal

inbox_stored = Signal(providing_args=["user", "message"])
inbox_deleted = Signal(providing_args=["user", "message_id"])
inbox_read = Signal(providing_args=["user", "message_id"])
inbox_all_read = Signal(providing_args=["user"])
inbox_purged = Signal(providing_args=["user"])

archive_stored = Signal(providing_args=["user", "message"])
