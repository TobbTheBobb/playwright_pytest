""" 
Contains all the basic functions used for tests.
"""
from playwright.sync_api import expect
#Navigate through the site...
def b_nav_aktivitaeten(page):
    page.get_by_role("link", name="Waldbühne Heessen").click()
    target=page.get_by_role("heading", name="Alle Aktivitäten")
    page.screenshot(path="./screenshots/b_nav_aktiviaeten.png")
    assert target.is_visible(), "Fehler - Aktivitätenseite konnte nicht aufgerufen werden."

def b_nav_spielerliste(page):
    page.get_by_role("link", name="Spielerliste").click()
    target=page.locator("//h2[text()='Alle Mitglieder']")
    page.screenshot(path="./screenshots/b_nav_spielerliste.png")
    assert target.is_visible(), "Fehler - Mitgliederseite konnte nicht aufgerufen werden."

def b_nav_termine(page):
    page.get_by_role("link", name="Termine").click()
    target=page.locator("//h2[text()='Alle bevorstehenden Events']")
    page.screenshot(path="./screenshots/b_nav_termine.png")
    assert target.is_visible(), "Fehler - Terminseite konnte nicht aufgerufen werden."

def b_nav_forum(page):
    page.get_by_role("link", name="Forum").click()
    target=page.locator("//h2[text()='Diskussionen']")
    page.screenshot(path="./screenshots/b_nav_forum.png")
    assert target.is_visible(), "Fehler - Forumseite konnte nicht aufgerufen werden."
    
def b_nav_vereinsinfo(page):
    page.get_by_role("link", name="Vereinsinfo").click()
    target=page.locator("//h2[text()='Vereinsinformation']")
    page.screenshot(path="./screenshots/b_nav_vereinsinfo.png")
    assert target.is_visible(), "Fehler - Vereinsinformationsseite konnte nicht aufgerufen werden."

def b_nav_handbuch(page):
    page.get_by_role("link", name="Handbuch").click()
    target=page.locator("//h2[text()='Handbuch zum Mitgliederbereich']")
    page.screenshot(path="./screenshots/b_nav_handbuch.png")
    assert target.is_visible(), "Fehler - Handbuchseite konnte nicht aufgerufen werden."    

def b_nav_verwaltung(page):
    page.get_by_role("link", name="Verwaltung", exact=True).click()
    #target=page.locator("//h2[text()='Verwaltung']")
    #assert target.is_visible(), "Fehler - Verwaltungsseite konnte nicht aufgerufen werden."
    #page.screenshot(path="./screenshots/b_nav_verwaltung.png")

def b_nav_inbox(page):
    page.get_by_role("heading", name="Inbox").click()
    target=page.locator("//h2[text()='Inbox']")
    page.screenshot(path="./screenshots/b_nav_inbox.png")
    assert target.is_visible(), "Fehler - Inboxseite konnte nicht aufgerufen werden."

def b_nav_all(page):
    b_nav_aktivitaeten(page)
    b_nav_spielerliste(page)
    b_nav_termine(page)
    b_nav_forum(page)
    b_nav_vereinsinfo(page)
    b_nav_handbuch(page)
    b_nav_verwaltung(page)

#Other functions
def b_check_basic_elements(page):
    elements=["Spielerliste","Termine","Forum","Vereinsinfo","Handbuch","Verwaltung","Account"]
    for element in elements:
        locate_string = "//span[contains(@class, 'elgg-anchor-label') and text() = '"+element+"']"
        target = page.locator(locate_string)
        assert target.first.is_visible(), "Fehler - "+element+" ist nicht auf der Seite sichtbar."

def b_search_test(page):
    page.get_by_placeholder("Suche").click()
    page.get_by_placeholder("Suche").fill("test")
    page.get_by_placeholder("Suche").press("Enter")
    page.screenshot(path="./screenshots/b_search_test.png")
    target=page.locator('text=/Treffer für.+test.+/')
    assert target.is_visible(), "Fehler - Suche konnte nicht durchgeführt werden."

def c_create(page):
    b_nav_termine(page)
    locate_string = "//span[contains(@class, 'elgg-anchor-label') and text() = 'Event hinzufügen']"
    target = page.locator(locate_string)
    assert target.first.is_visible(), "Fehler - Event hinzufügen Button ist nicht auf der Seite sichtbar."
    target.first.click()
    expect(page).to_have_url("https://web:8443/event_calendar/add")
    page.get_by_label("Titel*").fill("test")
    page.get_by_label("Ort").fill("test")
    page.get_by_label("Tags").fill("test")
    page.get_by_role("button", name="Speichern").click()
    page.screenshot(path="./screenshots/c_create.png")
    target = page.get_by_role("heading", name="test")
    assert target.is_visible(), "Fehler - Event konnte nicht erstellt werden"
    b_nav_aktivitaeten(page)
    target = page.get_by_text("fügte das Event test hinzu soeben")
    assert target.first.is_visible(), "Fehler - Event wird nicht in Aktivitäten angezeigt."
    page.get_by_role("link", name="Termine").click()
    page.get_by_role("link", name="test").first.click()
    # page.get_by_role("link", name=" ").click()
    # page.get_by_role("link", name=" Löschen").click()