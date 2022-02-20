from init import ma


class PersonSchema(ma.Schema):
    class Meta:
        fields = ("id", "email")


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
