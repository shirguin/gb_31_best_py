import datetime

from django.core.management import BaseCommand
import json

from news.models import News
from users.models import Role, User
from search.models import Languages, LanguageLevels, Employments, WorkSchedules, MainSkills, Category

JSON_PATH_NEWS = 'news/fixtures/'
JSON_PATH_SEARCH = 'search/fixtures/'

def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Запуск после создания пользователя.
        news = load_from_json(JSON_PATH_NEWS + 'news.json')
        News.objects.all().delete()
        today = datetime.datetime.now(tz=datetime.timezone.utc)

        for n in news:
            j_news = n.get('fields')
            j_news['id'] = n.get('pk')
            author_id = j_news.get('author')
            author = User.objects.get(id=int(author_id))
            j_news['author'] = author
            j_news['created'] = today
            j_news['updated'] = today
            new_news = News(**j_news)
            new_news.save()

        languages = load_from_json(JSON_PATH_SEARCH + 'languages.json')
        Languages.objects.all().delete()

        for l in languages:
            j_lang = {}
            j_lang['code'] = l.get('code')
            j_lang['language'] = l.get('language')
            new_lang = Languages(**j_lang)
            new_lang.save()

        levels = load_from_json(JSON_PATH_SEARCH + 'languagelevel.json')
        LanguageLevels.objects.all().delete()

        for l in levels:
            j_level = {}
            j_level['code'] = l.get('code')
            j_level['level'] = l.get('level')
            new_level = LanguageLevels(**j_level)
            new_level.save()

        employments = load_from_json(JSON_PATH_SEARCH + 'employments.json')
        Employments.objects.all().delete()

        for e in employments:
            j_empl = {}
            j_empl['code'] = e.get('code')
            j_empl['employment'] = e.get('employment')
            new_empl = Employments(**j_empl)
            new_empl.save()

        schedules = load_from_json(JSON_PATH_SEARCH + 'work_schedules.json')
        WorkSchedules.objects.all().delete()

        for sch in schedules:
            j_sch = {}
            j_sch['code'] = sch.get('code')
            j_sch['schedule'] = sch.get('schedule')
            new_sch = WorkSchedules(**j_sch)
            new_sch.save()

        skills = load_from_json(JSON_PATH_SEARCH + 'main_skills.json')
        MainSkills.objects.all().delete()

        for s in skills:
            j_skill = {}
            j_skill['code'] = s.get('code')
            j_skill['skill'] = s.get('skill')
            new_skill = MainSkills(**j_skill)
            new_skill.save()

        categories = load_from_json(JSON_PATH_SEARCH + 'categories.json')
        Category.objects.all().delete()

        for c in categories:
            j_cat = {}
            j_cat['code'] = c.get('code')
            j_cat['name'] = c.get('name')
            new_cat = Category(**j_cat)
            new_cat.save()