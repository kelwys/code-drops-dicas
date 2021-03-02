
# Model
class Person(models.Model):
    GENDER_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False)


    def __str__(self):
        return self.name
        
# Serializer
class PersonSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Person

    def get_gender(self,obj):
        return obj.get_gender_display()

    # for the latest DRF (3.6.3) - easiest method is:
    gender = serializers.CharField(source='get_gender_display')