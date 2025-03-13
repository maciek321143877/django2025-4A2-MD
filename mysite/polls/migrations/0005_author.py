import django.db.models.deletion
from django.db import migrations, models
 
 
class Migration(migrations.Migration):
 
    dependencies = [
        ('polls', '0004_choice'),
    ]
 
    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
            ],
        ),
    ]