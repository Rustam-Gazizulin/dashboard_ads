from rest_framework import serializers

from ads.models import Location, Category, Ads, User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField()
    author = serializers.CharField()
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Ads
        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Ads
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ads = Ads.objects.create(**validated_data)
        ads.save()
        return ads


class AdsUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    is_published = serializers.BooleanField(required=False)

    class Meta:
        model = Ads
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        return super().save()


class AdsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserRetrieveSerializer(serializers.ModelSerializer):
    location_id = LocationSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(required=False, many=True, queryset=Location.objects.all(),
                                               slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._location_id = self.initial_data.pop('location_id', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location_id:
            location_id, _ = Location.objects.get_or_create(name=loc)
            user.location_id.add(location_id)

        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age', 'password', 'location_id']


class UserUpdateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(required=False, many=True, queryset=Location.objects.all(),
                                               slug_field='name')

    def is_valid(self, *, raise_exception=False):
        self._location_id = self.initial_data.pop('location_id', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)

        for loc in self._location_id:
            location_id, _ = Location.objects.get_or_create(name=loc)
            user.location_id.add(location_id)

        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age', 'password', 'location_id']
