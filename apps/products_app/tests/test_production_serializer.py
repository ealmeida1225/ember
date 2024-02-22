# Generated by CodiumAI

import datetime
import pytest
from model_bakery import baker

from apps.products_app.models import Production, Plan, Product, GroupingPackaging
from apps.products_app.serializers import ProductionSerializer


class TestProductionSerializer:
    # Serializes a valid Production object with all fields
    @pytest.mark.django_db
    def test_serializes_valid_production_with_all_fields(self):
        # Create a valid Production object with all fields
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="Test Product"),
            description="Test Description",
            plan=baker.make(Plan, name="Test Plan"),
            distribution_format=baker.make(GroupingPackaging, name="Test Format"),
            quantity=10,
            cost=5.99,
            wholesale_price=9.99,
            active=True,
            production_date=datetime.date.today(),
        )

        # Serialize the Production object
        serializer = ProductionSerializer(production)
        serialized_data = serializer.data

        # Assert that all fields are serialized correctly
        assert serialized_data["name"] == "Test Production"
        assert Product.objects.get(id=serialized_data["product"]).name == "Test Product"
        assert serialized_data["description"] == "Test Description"
        assert Plan.objects.get(id=serialized_data["plan"]).name == "Test Plan"
        assert (
            GroupingPackaging.objects.get(
                id=serialized_data["distribution_format"]
            ).name
            == "Test Format"
        )
        assert serialized_data["quantity"] == 10
        assert serialized_data["cost"] == "5.99"
        assert serialized_data["wholesale_price"] == "9.99"
        assert serialized_data["active"] is True
        assert serialized_data["production_date"] == datetime.date.today().__str__()

    @pytest.mark.django_db  # Serializes a Production object with null or blank optional fields
    def test_serializes_production_with_null_or_blank_optional_fields(self):
        # Create a Production object with null or blank optional fields
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            description=None,
            plan=None,
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=10,
            cost=None,
            wholesale_price=9.99,
            active=True,
            production_date=datetime.date.today(),
        )

        # Serialize the Production object
        serializer = ProductionSerializer(production)
        serialized_data = serializer.data

        # Assert that null or blank optional fields are serialized correctly
        assert serialized_data["description"] is None
        assert serialized_data["plan"] is None
        assert serialized_data["cost"] is None

    # Serializes a Production object with the minimum valid values for each field
    @pytest.mark.django_db
    def test_serializes_production_with_minimum_valid_values(self):
        # Create a Production object with the minimum valid values for each field
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=1,
            cost=None,
            wholesale_price=0.01,
            active=True,
            production_date=datetime.date.today(),
        )

        # Serialize the Production object
        serializer = ProductionSerializer(production)
        serialized_data = serializer.data

        # Assert that the minimum valid values are serialized correctly
        assert serialized_data["quantity"] == 1
        assert serialized_data["wholesale_price"] == "0.01"

    # Validates a Production object with an invalid plan
    @pytest.mark.django_db
    def test_validates_production_with_invalid_plan(self):
        # Create a Production object with an invalid plan
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            description="Test Description",
            plan=baker.make(Plan, name="Invalid Plan"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=10,
            cost=5.99,
            wholesale_price=9.99,
            active=True,
            production_date=datetime.date.today(),
        )

        # Validate the Production object
        serializer = ProductionSerializer(data=production)
        assert serializer.is_valid() is False

    # Serializes a Production object with active status set to False
    @pytest.mark.django_db
    def test_serializes_inactive_production(self):
        # Create a Production object with active status set to False
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            description="Test Description",
            plan=baker.make(Plan, name="test plan"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=10,
            cost=5.99,
            wholesale_price=9.99,
            active=False,
            production_date=datetime.date.today(),
        )

        # Serialize the Production object
        serializer = ProductionSerializer(production)
        serialized_data = serializer.data

        # Assert that the active status is serialized correctly as False
        assert serialized_data["active"] is False

    # Validates a Production object with an invalid product
    @pytest.mark.django_db
    def test_validates_production_with_invalid_product(self):
        # Create a Production object with an invalid product
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="Invalid Product"),
            description="Test Description",
            plan=baker.make(Plan, name="test plan"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=10,
            cost=5.99,
            wholesale_price=9.99,
            active=True,
            production_date=datetime.date.today(),
        )

        # Validate the Production object
        serializer = ProductionSerializer(data=production)
        assert serializer.is_valid() is False

    # Serializes a Production object with a future production date
    @pytest.mark.django_db
    def test_serializes_production_with_future_date(self):
        # Create a Production object with a future production date
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            description="Test Description",
            plan=baker.make(Plan, name="test plan"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=10,
            cost="5.99",
            wholesale_price="9.99",
            active=True,
            production_date=(
                datetime.date.today() + datetime.timedelta(days=1)
            ).__str__(),
        )

        # Serialize the Production object
        serializer = ProductionSerializer(production)
        serialized_data = serializer.data

        # Assert that the future date is serialized correctly
        assert (
            serialized_data["production_date"]
            == (datetime.date.today() + datetime.timedelta(days=1)).__str__()
        )

    # Validates a Production object with a negative quantity
    @pytest.mark.django_db
    def test_validates_production_with_negative_quantity(self):
        # Create a Production object with a negative quantity
        production = Production(
            name="Test Production",
            product=baker.make(Product, name="test product"),
            description="Test Description",
            plan=baker.make(Plan, name="test plan"),
            distribution_format=baker.make(GroupingPackaging, name="test format"),
            quantity=-10,
            cost=5.99,
            wholesale_price=9.99,
            active=True,
            production_date=datetime.date.today(),
        )

        # Validate the Production object
        serializer = ProductionSerializer(data=production)
        assert serializer.is_valid() is False