from rest_marshmallow import Schema, fields
from marshmallow import validate
from .models import Twitters


class BaseSchema(Schema):
    id = fields.Integer()
    removed = fields.Boolean()
    created_date = fields.DateTime()


class TwittersSchema(BaseSchema):
    tweetdate = fields.DateTime()
    nick = fields.String(
        required=True,
        validate=[validate.Length(min=3, max=15)],
    )
    tweet = fields.String(
        required=True,
        validate=[validate.Length(min=0, max=50)],
    )

    def create(self, validated_data):
        return Twitters.objects.create(**validated_data)
