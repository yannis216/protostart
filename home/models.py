from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(help_text="Dieser Text wird in der Übersicht aller Events eventuell abgeschnitten (Die ersten 100 Wörter) präsentiert und nur auf der Detailansicht vollständig angezeigt. Die wichtigsten Fakten also am Anfang")
    location = models.CharField(max_length=100, help_text="Bitte in dem Format: NameDesVeranstaltungsortes, Straße, Stadt, Beispiel: Protostart Firmenzentrale, Hausdorffstraße 34, Bonn")
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now, help_text="WICHTIG! Hier zumindest einen Schätzwert angeben. Genaue Uhrzeit und Datum werden eh nirgendwo angezeigt, aber Events die ein falsches Enddatum haben werden eventuell in einer falschen kategorie , z.B. Vergangene und nicht zukünftige Events angezeigt")
    created_date = models.DateTimeField(default=timezone.now)
    cooperation_partners = models.TextField(blank=True, help_text="Für eventuelle Partner wie die mitorganisierende Hochschule")
    logo = models.CharField(max_length=100, default="protostart_logo_website-min.png", help_text="Den Dateinamen des zu verwendenen Bildes, mit Endung wie .jpg hier einfügen und das Bild dann mit Angabe der betreffenden Veranstaltung an Yannis senden")
    eventbrite_link = models.CharField(max_length=200, blank=True, help_text="Den gesamten Eventbrite Link, über den Besucher auf das Event kommen hier einfügen")
    facebook_link = models.CharField(max_length=200, blank=True, help_text="Den gesamten Facebook Link, über den Besucher auf das Event kommen hier einfügen")

    def __str__(self):
        return self.title
