"""
Employee class tests.
"""
import pytest

from hotel.db.db_interface import DataObject
from hotel.operations.bookings import create_booking
from hotel.operations.models import BookingCreateData


class RoomInterface:
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()


class BookingInterface:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()


class TestBooking:
    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date="2020-01-01",
            to_date="2020-01-02",
        )
        self.booking = create_booking(booking_data, RoomInterface(), BookingInterface())
        assert self.booking.price == 150_00

    def test_date_value_error(self):
        wrong_booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date="2020-01-01",
            to_date="2020-01-01",
        )
        assert pytest.raises(
            ValueError,
            create_booking,
            wrong_booking_data,
            RoomInterface(),
            BookingInterface(),
        )


if __name__ == "__main__":
    pytest.main()
