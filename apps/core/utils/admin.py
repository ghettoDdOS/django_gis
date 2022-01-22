from django.forms import Textarea


class SuperUserAdminMixin:
    """
    Добавляет поля, которые не доступны пользователю
    если он не являются суперпользователем
    """

    list_readonly_not_superuser_fields = ()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            for field in self.list_readonly_not_superuser_fields:
                if field in form.base_fields:
                    form.base_fields[field].disabled = True

        return form


class TextareaAdminMixin:
    list_textarea_fields = ()

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in self.list_textarea_fields:
            kwargs["widget"] = Textarea()
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)


BaseAdminMixin = type(
    "ModelAdmin",
    (
        TextareaAdminMixin,
        SuperUserAdminMixin,
    ),
    {},
)
