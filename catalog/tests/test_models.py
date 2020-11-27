from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Genre, Language, Book, BookInstance

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label,'date of birth')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_last_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/authors/1')


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Genre.objects.create(name='Non Fiction')

    def test_name_label(self):
        genre=Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_name_max_length(self):
        genre=Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_name_help_text(self):
        genre=Genre.objects.get(id=1)
        help_text = genre._meta.get_field('name').help_text
        self.assertEquals(help_text, "Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def test_name(self):
        genre=Genre.objects.get(id=1)
        expected_object_name = genre.name
        self.assertEquals(expected_object_name,str(genre))


class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Language.objects.create(name='France')

    def test_name_max_length(self):
        language=Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

    def test_name_help_text(self):
        language=Language.objects.get(id=1)
        help_text = language._meta.get_field('name').help_text
        self.assertEquals(help_text, "Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def test_name(self):
        language=Language.objects.get(id=1)
        expected_object_name = language.name
        self.assertEquals(expected_object_name,str(language))






class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Book.objects.create(title='The House')

    def test_title_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_summary_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)

    def test_summary_help_text(self):
        book=Book.objects.get(id=1)
        help_text = book._meta.get_field('summary').help_text
        self.assertEquals(help_text, "Enter a brief description of the book")

    def test_isbn_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length,13)

    def test_isbn_help_text(self):
        book=Book.objects.get(id=1)
        help_text = book._meta.get_field('isbn').help_text
        self.assertEquals(help_text, '13 Character <a href="https://www.isbn-international.org/content/what-isbn''">ISBN number</a>')

    def test_isbn_label(self):
        book=Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label,'ISBN')

    def test_genre_help_text(self):
        book=Book.objects.get(id=1)
        help_text = book._meta.get_field('genre').help_text
        self.assertEquals(help_text, "Select a genre for this book")

    def test_get_absolute_url(self):
        book=Book.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(),'/catalog/books/1')

    def test_title(self):
        book=Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name,str(book))


class BookInstanceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        BookInstance.objects.create(due_back='2020-11-20')

    def test_genre_help_text(self):
        bookinstance=BookInstance.objects.get(id=1)
        help_text = book._meta.get_field('id').help_text
        self.assertEquals(help_text, "Unique ID for this particular book across whole library")

    def test_imprint_max_length(self):
        bookinstance=BookInstance.objects.get(id=1)
        max_length = book._meta.get_field('imprint').max_length
        self.assertEquals(max_length,200)

    def test_due_back_label(self):
        bookinstance=BookInstance.objects.get(id=1)
        field_label = genre._meta.get_field('due_back').verbose_name
        self.assertEquals(field_label,'due back')

    def test_is_overdue(self):
        bookinstance=BookInstance.objects.get(id=1)
        self.assertTrue(bookinstance.is_overdue())

    def test_status_max_length(self):
        bookinstance=BookInstance.objects.get(id=1)
        max_length = book._meta.get_field('status').max_length
        self.assertEquals(max_length,1)

    def test_status_help_text(self):
        bookinstance=BookInstance.objects.get(id=1)
        help_text = book._meta.get_field('status').help_text
        self.assertEquals(help_text, "Book availability")

'''
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)
'''