from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
POST_DATA = '{text:.15}, {date:%Y-%m-%d}, {author}, {group}'
FOLLOW_DATA = '{user} подписан на {following}'


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    class Meta:
        ordering = ('pub_date')

    def __str__(self):
        return POST_DATA.format(
            text=self.text,
            date=self.pub_date,
            author=self.author.username,
            group=self.group
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('created')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        unique=False,
        related_name='following',
        verbose_name='Автор постов',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_subscription'
            )
        ]

    def __str__(self):
        return FOLLOW_DATA.format(
            user=self.user.username,
            following=self.following.username
        )
