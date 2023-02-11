import random
from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation


laudatory_phrases = ('Молодец!', 'Отлично!', 'Хвалю!', 'Приятно удивляет!', 'Так держать!', 'Супер!')


def get_schoolkid(schoolkid_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return child
    except Schoolkid.DoesNotExist:
        print('Проверьте, правильно ли вы написали фамилию и имя, такого ученика нет')
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько совпадений, введите более точные данные')


def fix_marks(schoolkid_name='Фролов Иван'):
    schoolkid = get_schoolkid(schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid_name='Фролов Иван'):
    schoolkid = get_schoolkid(schoolkid_name)
    child_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    child_chastisement.delete()


def create_commendation(schoolkid_name='Фролов Иван', subject_name='Математика'):
    schoolkid = get_schoolkid(schoolkid_name)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject_name).order_by('-date').first()
    Commendation.objects.create(
        text=random.choice(laudatory_phrases),
        created=lessons.date,
        schoolkid=schoolkid,
        subject=lessons.subject,
        teacher=lessons.teacher
    )
