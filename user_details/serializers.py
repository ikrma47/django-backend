from .models import Details, PhoneNumbers, Address
from rest_framework import serializers
from authentication.serializers import RegisterUserSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'mailingAddress', 'residentialAddress']


class PhoneNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ['id', 'primaryPhoneNumber', 'secondaryPhoneNumber']


class DetailsSerializer(serializers.ModelSerializer):

    phoneNumbers = PhoneNumbersSerializer()
    address = AddressSerializer()

    class Meta:
        model = Details
        exclude = ['createdAt', 'updatedAt']
        read_only_fields = ['image']

    def create(self, validated_data):
        phoneNumbers = validated_data.pop('phoneNumbers', None)
        address = validated_data.pop('address', None)
        details = Details.objects.create(**validated_data)
        if phoneNumbers is not None:
            PhoneNumbers.objects.create(details=details, **phoneNumbers)
        if address is not None:
            Address.objects.create(details=details, ** address)
        return details

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.fatherName = validated_data.get(
            'fatherName', instance.fatherName)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.domicile = validated_data.get('domicile', instance.domicile)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.courseCategory = validated_data.get(
            'courseCategory', instance.courseCategory)
        instance.address.mailingAddress = validated_data['address'].get(
            'address', instance.address.mailingAddress)
        instance.address.residentialAddress = validated_data['address'].get(
            'address', instance.address.residentialAddress)
        instance.phoneNumbers.primaryPhoneNumber = validated_data['phoneNumbers'].get(
            'primaryPhoneNumber', instance.phoneNumbers.primaryPhoneNumber)
        instance.phoneNumbers.secondaryPhoneNumber = validated_data['phoneNumbers'].get(
            'secondaryPhoneNumber', instance.phoneNumbers.secondaryPhoneNumber)
        instance.save()
        return instance


class DetailsNestedSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()
    phoneNumbers = PhoneNumbersSerializer()
    address = AddressSerializer()

    class Meta:
        model = Details
        exclude = ['createdAt', 'updatedAt']

class ImageSerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer(read_only=True)
    phoneNumbers = PhoneNumbersSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Details
        fields = ['id','name', 'fatherName', 'dob', 'domicile', 'religion', 'image', 'courseCategory','user', 'phoneNumbers', 'address']
        read_only_fields = ('id','name', 'fatherName', 'dob', 'domicile', 'religion', 'courseCategory')

class CourseCategorySerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer(read_only=True)
    phoneNumbers = PhoneNumbersSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Details
        fields = ['id','name', 'fatherName', 'dob', 'domicile', 'religion', 'image', 'courseCategory','user', 'phoneNumbers', 'address']
        read_only_fields = ('id','name', 'fatherName', 'dob', 'domicile', 'religion', 'image')