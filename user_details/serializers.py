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

    phoneNumber = PhoneNumbersSerializer()
    address = AddressSerializer()

    class Meta:
        model = Details
        exclude = ['createdAt', 'updatedAt']
        read_only_fields = ['image', 'courseCategory']

    def update(self, instance, validated_data):
        phoneNumber = instance.phoneNumber
        address = instance.address
        instance.name = validated_data.get('name', instance.name)
        instance.fatherName = validated_data.get(
            'fatherName', instance.fatherName)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.domicile = validated_data.get('domicile', instance.domicile)
        instance.religion = validated_data.get('religion', instance.religion)
        instance.courseCategory = validated_data.get(
            'courseCategory', instance.courseCategory)
        address.mailingAddress = validated_data['address'].get(
            'mailingAddress', address.mailingAddress)
        address.residentialAddress = validated_data['address'].get(
            'residentialAddress', address.residentialAddress)
        phoneNumber.primaryPhoneNumber = validated_data['phoneNumber'].get(
            'primaryPhoneNumber', phoneNumber.primaryPhoneNumber)
        phoneNumber.secondaryPhoneNumber = validated_data['phoneNumber'].get(
            'secondaryPhoneNumber', phoneNumber.secondaryPhoneNumber)
        address.save()
        phoneNumber.save()
        instance.save()
        return instance


class DetailsNestedSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer(read_only=True)
    phoneNumber = PhoneNumbersSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Details
        exclude = ['createdAt', 'updatedAt']


class ImageSerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer(read_only=True)
    phoneNumber = PhoneNumbersSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Details
        fields = ['id', 'name', 'fatherName', 'dob', 'domicile', 'religion',
                  'image', 'courseCategory', 'user', 'phoneNumbers', 'address']
        read_only_fields = ('id', 'name', 'fatherName', 'dob',
                            'domicile', 'religion', 'courseCategory')


class CourseCategorySerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer(read_only=True)
    phoneNumber = PhoneNumbersSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Details
        fields = ['id', 'name', 'fatherName', 'dob', 'domicile', 'religion',
                  'image', 'courseCategory', 'user', 'phoneNumbers', 'address']
        read_only_fields = ('id', 'name', 'fatherName',
                            'dob', 'domicile', 'religion', 'image')
