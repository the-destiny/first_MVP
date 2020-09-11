from django.db import models
from django.utils.text import slugify

class Lecture(models.Model):

    class MainCategory(models.TextChoices):
        코딩 = '코딩', '코딩'
        미술 = '미술', '미술'
        디자인_편집 = '디자인/편집', '디자인/편집'

    class SubCategory(models.TextChoices):
        Python = 'Python', 'Python'
        HTML_CSS = 'HTML/CSS', 'HTML/CSS'
        Javascript = 'Javascript', 'Javascript'
        C = 'C', 'C'
        Java = 'Java', 'Java'
        Git = 'Git', 'Git'
        연필 = '연필', '연필'
        디지털드로잉 = '디지털드로잉', '디지털드로잉'
        색연필 = '색연필', '색연필'
        수채화 = '수채화', '수채화'
        펜 = '펜', '펜'
        캘리그래피 = '캘리그래피', '캘리그래피'
        아크릴 = '아크릴', '아크릴'
        Premiere_Pro = 'Premiere Pro', 'Premiere Pro'
        Photoshop = 'Photoshop', 'Photoshop'
        After_Effect = 'After Effect', 'After Effect'
        InDesign = 'InDesign', 'InDesign'
        Illustrator = 'Illustrator', 'Illustrator'
        Sketch = 'Sketch', 'Sketch'
        
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='제목',
    )
    video = models.URLField(
        max_length=200,
        unique=True,
        verbose_name='강의출처',
    )
    description = models.TextField(
        blank=True,
        verbose_name='강의설명',
    )
    lecturer = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='강사',
    )
    main_category = models.CharField(
        max_length=16,
        choices=MainCategory.choices,
        blank=True,
        verbose_name='대분류',
    )
    sub_category = models.CharField(
        max_length=18,
        choices=SubCategory.choices,
        blank=True,
        verbose_name='중분류',
    )
    slug = models.SlugField(
        max_length=18, 
        allow_unicode=True, 
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_clicked = models.BooleanField(
        default=False,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sub_category)
        super(Lecture, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = '강의'
        verbose_name_plural = '강의'
        ordering = [
            'title',
        ]

    def __str__(self):
        return '{title}/{main_category}/{sub_category}'.format(
            title=self.title,
            main_category=self.main_category,
            sub_category=self.sub_category,
        )
