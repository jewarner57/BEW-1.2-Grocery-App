from grocery_app.models import ItemCategory, GroceryStore
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, URL


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    # - title - StringField
    title = StringField('Store Name', validators=[DataRequired()])
    # - address - StringField
    address = StringField('Store Address', validators=[DataRequired()])
    # - submit button
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # - name - StringField
    name = StringField('Item Name', validators=[DataRequired()])
    # - price - FloatField
    price = FloatField('Item Price', validators=[DataRequired()])
    # - category - SelectField (specify the 'choices' param)
    category = SelectField(
        'Item Category', choices=ItemCategory.choices())
    # - photo_url - StringField (use a URL validator)
    photo_url = StringField('Photo URL', validators=[DataRequired(), URL()])
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField(
        'Store', query_factory=lambda: GroceryStore.query)
    # - submit button
    submit = SubmitField('Submit')
