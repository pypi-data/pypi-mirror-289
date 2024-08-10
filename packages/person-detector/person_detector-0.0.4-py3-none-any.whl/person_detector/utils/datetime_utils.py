"""This module contains utilities for datetime operations.

Classes:
    DateTimeUtils: A class containing datetime utility methods."""

import datetime


class DateTimeUtils:
    """A class with convenient datetime utility methods.

    This class provides methods to:

        - Converting datetime objects to unix timestamps in milliseconds.
        - Converting unix timestamps in milliseconds to datetime objects.

    Attributes:
        None.

    Methods:

        datetime_to_timestamp(
            date_time: datetime.datetime
        ) -> int:
            Converts a datetime object to a unix timestamp in milliseconds.

        timestamp_to_datetime(
            timestamp: int
        ) -> datetime.datetime:
            Creates a unix timestamp in milliseconds to a datetime object.
        
    """

    @staticmethod
    def datetime_to_timestamp(date_time: datetime.datetime) -> int:
        """Converts a datetime object to a unix timestamp in milliseconds.
        
        Args:
            date_time (datetime.datetime): Python datetime object.
            
        Returns:
            int: Unix timestamp in milliseconds."""
        
        timestamp = int(date_time.timestamp() * 1000)

        return timestamp

    @staticmethod
    def timestamp_to_datetime(timestamp: int) -> datetime.datetime:
        """Converts a unix timestamp in milliseconds to a datetime object
        
        Args:
            timestamp (int): Unix timestamp in milliseconds.
            
        Returns:
            datetime.datetime: Python datetime object"""
        
        timestamp_seconds = timestamp / 1000.0

        date_time = datetime.datetime.fromtimestamp(
            timestamp_seconds, 
            tz=datetime.timezone.utc
        )

        return date_time
        