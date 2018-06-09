import rules


@rules.predicate
def is_page_owner(user, page):
    return user == page.owner


@rules.predicate
def page_is_locked(page):
    return page.lock


#@TODO create rule logic
@rules.predicate
def is_editor(user, page):
    return True

@rules.predicate
def can_edit_page(user, page):
    if page_is_locked(page):
        if is_editor(user, page) or is_page_owner(user, page):
            return True
        else:
            return False
    else:
        return True

rules.add_rule('can_edit_page', can_edit_page)