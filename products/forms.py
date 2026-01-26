from django import forms
from .models import Product, AttributeType, AttributeValue, ProductAttribute, ProductImage


# AI tools were used to assist with the initial implementation. I reviewed and adapted the code to fit the project.

class ProductForm(forms.ModelForm):
    new_image = forms.ImageField(label='Add New Image', required=False)

    class Meta:
        model = Product
        exclude = ('time_created',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically create fields per AttributeType
        for attr_type in AttributeType.objects.all():
            field_name = f"attr_{attr_type.slug}"

            self.fields[field_name] = forms.ModelMultipleChoiceField(
                queryset=AttributeValue.objects.filter(attribute_type=attr_type),
                required=False,
                label=attr_type.name,
                widget=forms.CheckboxSelectMultiple
            )

            # Preselect existing values
            if self.instance.pk:
                self.fields[field_name].initial = list(
                    self.instance.attributes.filter(
                        attribute_value__attribute_type=attr_type
                    ).values_list('attribute_value_id', flat=True)
                )

    def save(self, commit=True):
        product = super().save(commit=False)

        if commit:
            product.save()

            # Clear old attributes
            product.attributes.all().delete()

            # Save grouped attributes
            for attr_type in AttributeType.objects.all():
                field_name = f"attr_{attr_type.slug}"
                values = self.cleaned_data.get(field_name, [])
                for val in values:
                    ProductAttribute.objects.create(
                        product=product,
                        attribute_value=val
                    )

            # Save new image (unchanged logic)
            new_img = self.cleaned_data.get('new_image')
            if new_img:
                ProductImage.objects.create(product=product, image=new_img)

        return product
