# Third-Party Imports
from pycountry import countries
from rest_framework import serializers

# App Imports
from core import models


class OfficeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OfficeBlock
        fields = ("name", "id", "location")


class OfficeFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OfficeFloor
        fields = ("number", "block", "id")


class OfficeFloorSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OfficeFloorSection
        fields = ("name", "floor", "id")


class OfficeWorkspaceSerializer(serializers.ModelSerializer):
    floor = serializers.ReadOnlyField(source='section__floor__number')
    block = serializers.ReadOnlyField(source='section__floor__block__name')

    class Meta:
        model = models.OfficeWorkspace
        fields = ("id", "name", "section", "floor", "block")


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ("name", "id")


class AndelaCentreSerializer(serializers.ModelSerializer):
    centre_name = serializers.ReadOnlyField(source='name')
    country = serializers.SlugRelatedField(
        queryset=models.Country.objects.all(), slug_field="name"
    )

    class Meta:
        model = models.AndelaCentre
        fields = ("id", "name", "country", "created_at", "last_modified", "centre_name")

    def to_internal_value(self, data):
        country_name = data.get("country")
        if not country_name:
            raise serializers.ValidationError(
                {"country": [self.error_messages["required"]]}
            )
        try:
            query_data = {"id": int(country_name)}
        except ValueError:
            country = countries.lookup(country_name)
            query_data = {"name": country.name}
        finally:
            try:
                country = models.Country.objects.get(**query_data)
            except Exception:
                raise serializers.ValidationError(
                    {
                        "country": [
                            f'Invalid country "{country_name}" - object does not exist.'
                        ]
                    }
                )
        data_ = data.copy()
        data_["country"] = country.name
        if not data_.get("name"):
            data_["name"] = data_.get("centre_name")
        internal_value = super().to_internal_value(data_)
        return internal_value


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ("id", "name", "created_at", "last_modified")
