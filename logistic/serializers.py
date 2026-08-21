<<<<<<< HEAD
from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            product_id = position.get('product')
            new_price = position.get('price')
            new_quantity = position.get('quantity')
            obj, status = StockProduct.objects.update_or_create(stock=stock,
                                                                product=product_id,
                                                                defaults={
                                                                'product':product_id,
                                                                'price': new_price,
                                                                'quantity': new_quantity
                                                                }
                                                                )
            obj.save()

        return stock
=======
from rest_framework import serializers

from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            product_id = position.get('product')
            new_price = position.get('price')
            new_quantity = position.get('quantity')
            obj, status = StockProduct.objects.update_or_create(stock=stock,
                                                                product=product_id,
                                                                defaults={
                                                                'product':product_id,
                                                                'price': new_price,
                                                                'quantity': new_quantity
                                                                }
                                                                )
            obj.save()

        return stock
>>>>>>> 30042147070ca8ae1b7d65d33bf2440b6229a2b8
