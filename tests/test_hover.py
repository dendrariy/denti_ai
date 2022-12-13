from src.pages.page_hover import HoverPage


def test_hover(browser):
    page = HoverPage(browser)
    page.open()
    hovers = page.get_hovers()
    names = page.get_hovers_names()
    links = page.get_hovers_links()

    for i in range(len(hovers)):
        page.move_to_hover(hovers[i])

        assert names[i].is_displayed() is True, "Hover name is not visible"
        assert links[i].is_displayed() is True, "Hover link is not visible"
