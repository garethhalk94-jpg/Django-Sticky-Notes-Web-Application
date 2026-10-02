from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    """Unit testing class focused entirely on verifying the Note model layer."""

    def setUp(self):
        # 1. Create a dummy test note record with a signature
        Note.objects.create(
            title="Test Pinned Title",
            content="This is a whimsical text body description.",
            author="Gareth",
        )
        # 2. Create an anonymous test note record
        Note.objects.create(
            title="Anonymous Title",
            content="Testing empty signature logic flows.",
            author="",
        )

    def test_note_attributes_save_correctly(self):
        """Verify model fields correctly record and read text inputs."""
        note = Note.objects.get(title="Test Pinned Title")
        self.assertEqual(
            note.content, "This is a whimsical text body description."
        )
        self.assertEqual(note.author, "Gareth")

    def test_anonymous_note_saves_correctly(self):
        """Verify empty string author signatures commit safely to the database."""
        note = Note.objects.get(title="Anonymous Title")
        self.assertEqual(note.author, "")


class NoteViewTest(TestCase):
    """Unit testing class focused on validating HTTP responses and templates."""

    def setUp(self):
        # Seed the temporary test database registry with records
        Note.objects.create(
            title="Board Snapshot",
            content="Validating view container blocks.",
            author="Tester",
        )

    def test_note_list_dashboard_view(self):
        """Verify the main whiteboard page loads successfully with text content."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Board Snapshot")
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_detail_inspection_view(self):
        """Verify the zoomed-in single note detail view works correctly."""
        note = Note.objects.first()
        response = self.client.get(reverse("note_detail", args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Validating view container blocks.")
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_note_create_view_get(self):
        """Verify the creation page form draws the inputs correctly."""
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_delete_successful_post(self):
        """Verify that a valid POST request safely deletes a note and redirects."""
        note = Note.objects.first()
        response = self.client.post(
            reverse("note_delete", args=[str(note.id)])
        )

        # Check that it redirects back to the board list
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))

        # Verify the record is completely removed from the database
        self.assertFalse(Note.objects.filter(id=note.id).exists())

    def test_note_delete_render_detail_on_get(self):
        """Verify a GET request to delete view falls back to rendering detail."""
        note = Note.objects.first()
        response = self.client.get(reverse("note_delete", args=[str(note.id)]))

        # Should gracefully return a 200 OK status code and use the detail template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_detail.html")
