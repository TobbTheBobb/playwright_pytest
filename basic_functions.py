""" 
Contains all the basic functions used for tests.
"""

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
    b_nav_spielerliste(page)
    b_nav_termine(page)
    b_nav_forum(page)
    b_nav_vereinsinfo(page)
    b_nav_handbuch(page)
    b_nav_verwaltung(page)

#Basic functions
def b_search_test(page):
    page.get_by_placeholder("Suche").click()
    page.get_by_placeholder("Suche").fill("test")
    page.get_by_placeholder("Suche").press("Enter")
    page.screenshot(path="./screenshots/b_search_test.png")
    target=page.locator('text=/Treffer für.+test.+/')
    assert target.is_visible(), "Fehler - Suche konnte nicht durchgeführt werden."
